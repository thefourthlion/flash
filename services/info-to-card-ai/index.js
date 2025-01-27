const express = require("express");
const axios = require("axios");
const bodyParser = require("body-parser");
const cors = require("cors");
require('dotenv').config();

// Verify API URL exists
if (!process.env.API_URL) {
  console.error('API_URL environment variable is not set');
  process.exit(1);
}

// Set your OpenAI API key here
const apiKey =
  "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";

// Create Express app
const app = express();

app.use(
  cors({
    origin: [
      "http://localhost:3000",
      "http://localhost:3001",
      "https://flash.portkeylabs.net",
      "https://flash.portkeylabs.net/pages/add-card",
    ],
    methods: ["GET", "POST"],
    allowedHeaders: ["Content-Type", "Authorization"],
    credentials: true,
  })
);

app.use(bodyParser.json());

// Increase chunk size and process chunks in parallel
function splitText(text, chunkSize = 1000) {
  const chunks = [];
  let startIndex = 0;
  while (startIndex < text.length) {
    let endIndex = startIndex + chunkSize;
    if (endIndex < text.length) {
      const nextPeriod = text.indexOf('.', endIndex);
      if (nextPeriod !== -1 && nextPeriod - endIndex < 100) {
        endIndex = nextPeriod + 1;
      }
    }
    if (endIndex > text.length) endIndex = text.length;
    chunks.push(text.substring(startIndex, endIndex));
    startIndex = endIndex;
  }
  return chunks;
}

// Function to make a request to OpenAI API and get flashcards
async function generateFlashcards(prompt) {
  try {
    const chunks = splitText(prompt);
    console.log(`📄 Split text into ${chunks.length} chunks`);
    let allFlashcards = [];

    // Process chunks in parallel instead of sequentially
    const chunkPromises = chunks.map(async (chunk, i) => {
      console.log(`🔄 Starting chunk ${i + 1}/${chunks.length}`);
      try {
        const response = await axios.post(
          "https://api.openai.com/v1/chat/completions",
          {
            model: "gpt-3.5-turbo-1106",
            messages: [
              {
                role: "system",
                content: 'You are an AI that creates flashcards. Respond only with a JSON array of flashcards in this format: [{"question": "Q", "answer": "A"}]'
              },
              {
                role: "user",
                content: `Create as many detailed flashcards as possible from this text to get all of the relevant information for study, no more, no less. Format your response as a JSON array of flashcards in this exact format: [{"question": "Q", "answer": "A"}]. Only respond with the JSON array, no other text: ${chunk}`
              }
            ],
            max_tokens: 1024,
            temperature: 0.7,
          },
          {
            headers: {
              Authorization: `Bearer ${apiKey}`,
              "Content-Type": "application/json",
            },
          }
        );

        let flashcards = response.data.choices[0].message.content.trim();
        flashcards = flashcards.replace(/```json|```/g, "").replace(/^\s*\n/gm, "").trim();
        
        const startIdx = flashcards.indexOf('[');
        const endIdx = flashcards.lastIndexOf(']');
        
        if (startIdx === -1 || endIdx === -1) {
          console.error(`❌ Invalid JSON format received for chunk ${i + 1}`);
          return [];
        }

        flashcards = flashcards.substring(startIdx, endIdx + 1);
        const parsedFlashcards = JSON.parse(flashcards);
        
        if (Array.isArray(parsedFlashcards)) {
          console.log(`✅ Successfully parsed ${parsedFlashcards.length} flashcards from chunk ${i + 1}`);
          return parsedFlashcards;
        }
        return [];
      } catch (error) {
        console.error(`❌ Error processing chunk ${i + 1}:`, error.message);
        return [];
      }
    });

    // Wait for all chunks to be processed
    const results = await Promise.all(chunkPromises);
    allFlashcards = results.flat();

    console.log(`📊 Total flashcards generated: ${allFlashcards.length}`);
    return allFlashcards.length > 0 ? allFlashcards : null;

  } catch (error) {
    console.error(
      "Error generating flashcards:",
      error.response ? error.response.data : error.message
    );
    return null;
  }
}

// API endpoint to generate flashcards and save to MongoDB
app.post("/api/ai-flashcards/create", async (req, res) => {
  console.log("📝 Create flashcards endpoint hit");
  console.log("Request body:", req.body);
  
  const { title, description, information, author } = req.body;

  if (!title || !description || !information || !author) {
    console.log("❌ Missing required fields:", { title, description, information, author });
    return res
      .status(400)
      .json({
        error: "Please provide title, description, information, and author.",
      });
  }

  console.log("🤖 Generating flashcards...");
  const flashcards = await generateFlashcards(information);

  if (!flashcards) {
    console.log("❌ Failed to generate flashcards");
    return res.status(500).json({ error: "Failed to generate flashcards." });
  }
  console.log(`✅ Generated ${flashcards.length} flashcards`);

  const timestamp = new Date().toISOString().split("T")[0];

  const data = {
    title,
    description,
    information,
    author,
    timestamp: timestamp,
    cards: flashcards,
  };

  console.log("📦 Prepared data for saving:", data);

  try {
    console.log('📤 Attempting to save to:', `${process.env.API_URL}/api/flashcards/create/`);
    
    const response = await axios.post(
      `${process.env.API_URL}/api/flashcards/create/`,
      data,
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    console.log("✅ Save successful. Response:", response.data);
    res.json({ message: "Flashcards saved successfully", data: response.data });
  } catch (error) {
    console.error("❌ Error saving flashcards to MongoDB:");
    console.error("Error message:", error.message);
    if (error.response) {
      console.error("Error response data:", error.response.data);
      console.error("Error response status:", error.response.status);
    }
    res.status(500).json({ error: "Failed to save flashcards to MongoDB" });
  }
});

// API endpoint to edit flashcards by adding more cards
app.post("/api/ai-flashcards/edit", async (req, res) => {
  console.log("📝 Edit flashcards endpoint hit");
  const { id, information } = req.body;
  console.log("Received ID:", id);
  console.log("Received information:", information);

  try {
    console.log("🤖 Generating new flashcards...");
    const newFlashcards = await generateFlashcards(information);
    console.log("Generated flashcards:", newFlashcards);

    if (!newFlashcards) {
      console.log("❌ Failed to generate flashcards");
      return res.status(500).json({ error: "Failed to generate new flashcards." });
    }

    console.log("📥 Fetching existing flashcards from:", `${process.env.API_URL}/api/flashcards/read/${id}`);
    const getResponse = await axios.get(
      `${process.env.API_URL}/api/flashcards/read/${id}`,
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );

    const existingData = getResponse.data;
    console.log("Existing flashcards:", existingData);
    
    const updatedCards = [...existingData.cards, ...newFlashcards];
    console.log("Combined flashcards count:", updatedCards.length);

    console.log("📤 Updating flashcards at:", `${process.env.API_URL}/api/flashcards/update/${id}`);
    const updateResponse = await axios.post(
      `${process.env.API_URL}/api/flashcards/update/${id}`,
      {
        ...existingData,
        cards: updatedCards,
      },
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    console.log("Update response:", updateResponse.data);

    res.json({ 
      message: "Flashcards updated successfully", 
      data: updateResponse.data,
      newCards: newFlashcards 
    });
  } catch (error) {
    console.error("❌ Error updating flashcards:");
    console.error("Error message:", error.message);
    if (error.response) {
      console.error("Error response data:", error.response.data);
      console.error("Error response status:", error.response.status);
    }
    res.status(500).json({ error: "Failed to update flashcards" });
  }
});

// Start the server
const PORT = process.env.PORT || 3003;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});