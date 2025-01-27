const fs = require("fs");
const path = require("path");
const OpenAI = require("openai");
// Ensure you have this module installed (npm install openai)

// Initialize OpenAI client with API key
const openai = new OpenAI({
  apiKey: "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" // You can store the API key in an environment variable
});

// Example flashcards
const cards = [
  {
    "question": "What is Binary (Base-2) notation?",
    "answer": "Understanding how binary numbers represent data in computing systems; converting between binary and decimal.",
    "_id": "66f9f4c23f6585666d536cf4"
  },
  {
    "question": "What is Hexadecimal (Base-16) notation used for?",
    "answer": "Usage in memory addressing and color codes; converting between hexadecimal and other notational systems.",
    "_id": "66f9f4c23f6585666d536cf5"
  },
  {
    "question": "What is the role of Decimal (Base-10) in computing?",
    "answer": "It is the standard numbering system used in daily life.",
    "_id": "66f9f4c23f6585666d536cf6"
  }
];

// Function to generate TTS for each card
async function generateTTSForCard(card) {
  try {
    // Generate TTS for the answer
    const mp3 = await openai.audio.speech.create({
      model: "tts-1",  // Use the "tts-1-hd" model if you need higher quality
      voice: "nova",   // Specify the voice you want to use (e.g., "nova")
      input: card.answer, // You can use either card.question or card.answer as the text
    });

    // Define the file path for each card's audio
    const speechFile = path.resolve(`./audio/${card._id}.mp3`);

    // Create buffer and save the file
    const buffer = Buffer.from(await mp3.arrayBuffer());
    await fs.promises.writeFile(speechFile, buffer);
    
    console.log(`Audio for card "${card.question}" saved as ${speechFile}`);
  } catch (error) {
    console.error(`Error generating TTS for card "${card.question}":`, error);
  }
}

// Main function to loop through cards and generate TTS
async function main() {
  for (const card of cards) {
    await generateTTSForCard(card);
  }
}

main();
