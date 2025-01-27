const express = require('express');
const axios = require('axios'); // <-- Make sure to import axios here
const app = express();
app.use(express.json());

// Mock generateFlashcards function - replace with your actual implementation
const generateFlashcards = async (information) => {
  // Replace this with your actual logic to generate flashcards from 'information'
  return [
    { question: "What does 'ls' command do?", answer: "List files and directories." },
    { question: "What does 'cd' command do?", answer: "Change directory." }
  ]; // Mock flashcards for testing
};

// POST endpoint to create flashcards
app.post("/api/ai-flashcards/create", async (req, res) => {
  const { title, description, information } = req.body;

  // Check if required fields are provided
  if (!title || !description || !information) {
    return res.status(400).json({ error: "Please provide title, description, and information." });
  }

  try {
    // Generate flashcards based on the 'information' provided
    const flashcards = await generateFlashcards(information);

    // Log the generated flashcards to see if they are being created correctly
    console.log("Generated Flashcards:", flashcards);

    // If no flashcards are generated, return an error
    if (!flashcards || flashcards.length === 0) {
      return res.status(500).json({ error: "Failed to generate flashcards." });
    }

    // Prepare data to be saved to MongoDB
    const data = {
      title,
      description,
      information,
      timestamp: new Date().toISOString(),
      cards: flashcards, // Assign generated flashcards
    };

    // Log the data being sent to MongoDB
    console.log("Data being saved to MongoDB:", data);

    // Send a POST request to MongoDB API to save the flashcards
    const response = await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/api/flashcards/create/`, data, {
      headers: {
        "Content-Type": "application/json",
      },
    });

    // Log the response from MongoDB API
    console.log("MongoDB Response:", response.data);

    // Send success message if everything goes well
    return res.json({ message: "Flashcards saved successfully", data: response.data });

  } catch (error) {
    // Log the error for debugging purposes
    console.error("Error saving flashcards to MongoDB:", error.message);

    // Send an error response
    return res.status(500).json({ error: "Failed to save flashcards to MongoDB" });
  }
});

// Start the server
const PORT = 3003;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
