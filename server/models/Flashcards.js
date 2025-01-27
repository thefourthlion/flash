const mongoose = require("mongoose");

// Utility function to return only the date (YYYY-MM-DD) without time
const getCurrentDateOnly = () => {
  const today = new Date();
  // Format the date to YYYY-MM-DD by extracting the date part only
  return new Date(today.toISOString().split('T')[0]);
};

const flashcardSchema = new mongoose.Schema({
  title: {
    type: String,
    required: [true, "Please provide title"],
  },
  description: {
    type: String,
    required: [true, "Please provide description"],
  },
  information: {
    type: String,
    required: [true, "Please provide information"],
  },
  author: {
    type: String,
    required: [true, "Please provide author"],
  },
  votes: {
    type: Number,
    default: 0,
  },
  subscribers: {
    type: Number,
    default: 0,
  },
  tags: {
    type: [String],
  },
  cards: [
    {
      question: {
        type: String,
        required: [true, "Please provide question"],
        validate: {
          validator: function(v) {
            return v && v.trim().length > 0;
          },
          message: "Question cannot be empty"
        }
      },
      answer: {
        type: String,
        required: [true, "Please provide answer"],
        validate: {
          validator: function(v) {
            // If it's an array, join it with commas
            if (Array.isArray(v)) {
              return v.join(', ').trim().length > 0;
            }
            return v && v.trim().length > 0;
          },
          message: "Answer cannot be empty"
        },
        // Add a setter to handle arrays
        set: function(v) {
          if (Array.isArray(v)) {
            return v.join(', ');
          }
          return v;
        }
      },
      accuracy: {
        type: [String],
      },
      count: {
        type: Number,
        default: 0,
      },
      repetitions: {
        type: Number,
        default: 0,
      },
      interval: {
        type: Number,
        default: 1,
      },
      easiness: {
        type: Number,
        default: 2.5,
      },
      nextPracticeDate: {
        type: Date,
        default: getCurrentDateOnly, // Use the custom function to set only the date (without time)
      },
    },
  ],
  timestamp: {
    type: Date,
    default: Date.now,
  },
});

const Flashcard = mongoose.model("Flashcard", flashcardSchema);
module.exports = Flashcard;
