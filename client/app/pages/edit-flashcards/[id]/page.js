"use client";

import React, { useState, useEffect } from "react";
import { useParams } from "next/navigation";
import axios from "axios";
import "../../../../styles/EditFlashcards.scss";
import { Card } from "@/components/ui/card";
import { Button } from "@nextui-org/button";
import { Input, Textarea } from "@nextui-org/input";

const EditFlashCards = () => {
  const [flashcards, setFlashcards] = useState([]);
  const [isEditing, setIsEditing] = useState(null);
  const [editData, setEditData] = useState({});
  const [newQuestion, setNewQuestion] = useState("");
  const [newAnswer, setNewAnswer] = useState("");
  const [showAddFlashCard, setShowAddFlashCard] = useState(false);
  const [showAIInput, setShowAIInput] = useState(false);
  const [aiInputText, setAIInputText] = useState("");
  const params = useParams();
  const id = params?.id; // The dynamic 'id' from URL

  useEffect(() => {
    if (!id) return;

    // Fetch flashcards for the given ID
    const fetchFlashcards = async () => {
      try {
        const response = await axios.get(
          `${process.env.NEXT_PUBLIC_API_URL}/api/flashcards/read/${id}`
        );
        setFlashcards(response.data.cards);
      } catch (error) {
        console.error("Error fetching flashcards:", error);
      }
    };

    fetchFlashcards();
  }, [id]);

  const handleEdit = (cardId) => {
    setIsEditing(cardId);
    const card = flashcards.find((card) => card._id === cardId);
    setEditData(card);
  };

  const handleDelete = (cardId) => {
    setFlashcards(flashcards.filter((card) => card._id !== cardId));
  };

  const handleInputChange = (e) => {
    setEditData({ ...editData, [e.target.name]: e.target.value });
  };

  const handleSave = () => {
    setFlashcards(
      flashcards.map((card) => (card._id === editData._id ? editData : card))
    );
    setIsEditing(null);
  };

  const handleCancel = () => {
    setIsEditing(null);
  };

  // Submit the changes to the server
  const handleSubmit = async () => {
    try {
      const updatedFlashcards = [...flashcards]; // Get all the flashcards, including new and edited ones

      console.log("Submitting updated flashcards:", updatedFlashcards); // Log the data being sent

      // Make the API request to update the flashcards on the backend
      const response = await axios.post(
        `${process.env.NEXT_PUBLIC_API_URL}/api/flashcards/old-update/${id}`,
        {
          cards: updatedFlashcards, // Send the updated cards array to the backend
        }
      );

      if (response.status === 200) {
        alert("Flashcards updated successfully!");
        console.log("Response from server:", response.data);
      } else {
        alert("Failed to update flashcards.");
        console.error("Unexpected response:", response);
      }
    } catch (error) {
      console.error("Error updating flashcards:", error);
      alert("Error updating flashcards. Please try again.");
    }
  };

  const handleAddCard = () => {
    if (newQuestion.trim() === "" || newAnswer.trim() === "") {
      alert("Both fields are required to add a new card.");
      return;
    }

    const newCard = {
      question: newQuestion,
      answer: newAnswer,
      accuracy: [],
      count: 0,
      repetitions: 1,
      interval: 1,
      easiness: 2.5,
      nextPracticeDate: new Date().toISOString(),
    };

    setFlashcards([...flashcards, newCard]);
    setNewQuestion("");
    setNewAnswer("");
  };

  const handleAISubmit = async () => {
    if (!aiInputText.trim()) {
      console.error("Empty input text");
      alert("Please enter some information to generate flashcards.");
      return;
    }

    try {
      // First, send to AI service to generate new flashcards
      console.log("Sending request to AI service:", `${process.env.NEXT_PUBLIC_AI_URL}/api/ai-flashcards/edit`);
      console.log("Request payload:", { id, information: aiInputText });

      const response = await axios.post(
        `${process.env.NEXT_PUBLIC_AI_URL}/api/ai-flashcards/edit`,
        {
          id: id,
          information: aiInputText
        }
      );
      
      console.log("Full AI service response:", response);
      console.log("AI service response data:", response.data);

      if (response.data && response.data.data) {
        console.log("Updated flashcards data:", response.data.data);
        setFlashcards(response.data.data.cards);
        setShowAIInput(false);
        setAIInputText("");
        console.log("Successfully updated flashcards state");
      } else {
        console.error("Invalid response format from AI service:", response.data);
        throw new Error("Invalid response format from AI service");
      }
    } catch (error) {
      console.error("Full error object:", error);
      console.error("Error name:", error.name);
      console.error("Error message:", error.message);
      if (error.response) {
        console.error("Error response data:", error.response.data);
        console.error("Error response status:", error.response.status);
        console.error("Error response headers:", error.response.headers);
      }
      alert("Error generating flashcards. Check console for details.");
    }
  };

  return (
    <div className="EditFlashCards page">
      <h1 className="page-header">Edit Flashcards</h1>

      {/* Add AI Input Form */}
      {showAIInput && (
        <Card className="ai-input-section p-6">
          <h2>Add More AI-Generated Flashcards</h2>
          <Textarea
            label="Additional Information"
            placeholder="Enter additional information to generate more flashcards"
            value={aiInputText}
            onChange={(e) => setAIInputText(e.target.value)}
            className="mb-3"
            minRows={5}
            required
          />

          <div className="flex gap-2">
            <Button
              className="primary-btn"
              color="primary"
              variant="solid"
              onClick={handleAISubmit}
            >
              Generate More Flashcards
            </Button>
            <Button
              className="primary-btn"
              color="danger"
              variant="solid"
              onClick={() => {
                setShowAIInput(false);
                setAIInputText("");
              }}
            >
              Cancel
            </Button>
          </div>
        </Card>
      )}

      {showAddFlashCard && (
          <Card className="new-card-section p-6">
            <h2>Add New Flashcard</h2>
            <Input
              type="text"
              label="New Question"
              placeholder="Enter new question"
              value={newQuestion}
              onChange={(e) => setNewQuestion(e.target.value)}
              className="mb-3"
              required
            />

            <Textarea
              label="New Answer"
              placeholder="Enter new answer"
              value={newAnswer}
              onChange={(e) => setNewAnswer(e.target.value)}
              className="mb-3"
              minRows={3}
              required
            />

            <div className="flex gap-2">
              <Button
                className="primary-btn"
                color="primary"
                variant="solid"
                onClick={handleAddCard}
              >
                Add Card
              </Button>
              <Button
                className="primary-btn"
                color="danger"
                variant="solid"
                onClick={() => {
                  setShowAddFlashCard(!showAddFlashCard);
                }}
              >
                Cancel
              </Button>
            </div>
          </Card>
        )}

      <div className="container">
        <Button
          className="primary-btn"
          color="success"
          variant="solid"
          onClick={() => {
            setShowAddFlashCard(!showAddFlashCard);
          }}
        >
          Add a Flashcard
        </Button>
        <Button
          className="primary-btn"
          color="secondary"
          variant="solid"
          onClick={() => setShowAIInput(!showAIInput)}
        >
          Add More AI Flashcards
        </Button>
        <Button
          className="primary-btn"
          color="primary"
          variant="solid"
          onClick={handleSubmit}
        >
          Submit Updates
        </Button>

        {/* Flashcards list */}
        {flashcards.map((card) => (
          <Card key={card._id || Math.random()} className="flashcard-card p-6">
            <div>
              {isEditing === card._id ? (
                <>
                  <div>
                    <Input
                      type="text"
                      label="Question"
                      name="question"
                      placeholder="Edit Question"
                      value={editData.question}
                      onChange={handleInputChange}
                      className="mb-3"
                      required
                    />

                    <Textarea
                      label="Answer"
                      name="answer"
                      placeholder="Edit Answer"
                      value={editData.answer}
                      onChange={handleInputChange}
                      className="mb-3"
                      minRows={3}
                      required
                    />

                    <div className="buttons">
                      <Button
                        className="primary-btn"
                        color="primary"
                        variant="solid"
                        onClick={handleSave}
                      >
                        Save
                      </Button>
                      <Button
                        className="primary-btn"
                        color="danger"
                        variant="solid"
                        onClick={handleCancel}
                      >
                        Cancel
                      </Button>
                    </div>
                  </div>
                </>
              ) : (
                <>
                  <div className="flashcard-header question">
                    <h3>{card.question}</h3>
                  </div>
                  <div className="answer">
                    <p>{card.answer}</p>
                  </div>
                  <div className="buttons">
                    <Button
                      className="primary-btn"
                      color="primary"
                      variant="solid"
                      onClick={() => handleEdit(card._id)}
                    >
                      Edit
                    </Button>
                    <Button
                      className="primary-btn"
                      color="danger"
                      variant="solid"
                      onClick={() => handleDelete(card._id)}
                    >
                      Delete
                    </Button>
                  </div>
                </>
              )}
            </div>
          </Card>
        ))}
        {showAddFlashCard && (
          <Card className="new-card-section p-6">
            <h2>Add New Flashcard</h2>
            <Input
              type="text"
              label="New Question"
              placeholder="Enter new question"
              value={newQuestion}
              onChange={(e) => setNewQuestion(e.target.value)}
              className="mb-3"
              required
            />

            <Textarea
              label="New Answer"
              placeholder="Enter new answer"
              value={newAnswer}
              onChange={(e) => setNewAnswer(e.target.value)}
              className="mb-3"
              minRows={3}
              required
            />

            <div className="flex gap-2">
              <Button
                className="primary-btn"
                color="primary"
                variant="solid"
                onClick={handleAddCard}
              >
                Add Card
              </Button>
              <Button
                className="primary-btn"
                color="danger"
                variant="solid"
                onClick={() => {
                  setShowAddFlashCard(!showAddFlashCard);
                }}
              >
                Cancel
              </Button>
            </div>
          </Card>
        )}

        <Button
          className="primary-btn"
          color="success"
          variant="solid"
          onClick={() => {
            setShowAddFlashCard(!showAddFlashCard);
          }}
        >
          Add a Flashcard
        </Button>
        <Button
          className="primary-btn"
          color="primary"
          variant="solid"
          onClick={handleSubmit}
        >
          Submit Updates
        </Button>
      </div>
    </div>
  );
};

export default EditFlashCards;
