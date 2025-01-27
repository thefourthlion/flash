"use client";
import React, { useState } from "react";
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert";
import { Card } from "@/components/ui/card";
import { Input } from "@nextui-org/input";
import { Textarea } from "@nextui-org/input";
import {
  ExclamationTriangleIcon,
  CheckCircledIcon,
} from "@radix-ui/react-icons";
import axios from "axios";
import { Button } from "@nextui-org/button";

import { useUserAuth } from "@/context/UserAuthContext";
import "../../../styles/AddCard.scss";

const AddFlashCard = () => {
  const { user } = useUserAuth() || {};
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [information, setInformation] = useState("");
  const [tags, setTags] = useState([]);
  const [inputTag, setInputTag] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  console.log(user.username);

  // Function to handle form submission and API call
  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");

    // Prepare the flashcard data including the author (user information)
    const flashcardData = {
      title,
      description,
      information,
      tags, // Send the tags array to the API
      author: user?.email || "Unknown Author", // Add the user's email as the author
    };

    console.log(flashcardData);

    try {
      const response = await axios.post(
        `${process.env.NEXT_PUBLIC_AI_URL}/api/ai-flashcards/create`,
        flashcardData,
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      setSuccess("Flashcards generated successfully!");
      console.log("Flashcards:", response.data);
    } catch (error) {
      setError("Failed to generate flashcards. Please try again.");
      console.error(
        "Error:",
        error.response ? error.response.data : error.message
      );
    }
  };

  // Function to handle tag input
  const handleTagInput = (e) => {
    const value = e.target.value;
    if (value.includes(",")) {
      const newTags = value
        .split(",")
        .map((tag) => tag.trim())
        .filter((tag) => tag !== "");
      setTags([...tags, ...newTags]);
      setInputTag(""); // Reset the input field
    } else {
      setInputTag(value); // Update input field value for a tag
    }
  };

  // Function to remove a tag
  const removeTag = (indexToRemove) => {
    setTags(tags.filter((_, index) => index !== indexToRemove));
  };

  if (!user) {
    return (
      <div className="AddFlashCard page">
        <h1 className="page-header">Create Flashcards</h1>
        <div className="container">
          <Alert variant="destructive">
            <ExclamationTriangleIcon className="h-4 w-4" />
            <AlertTitle>Authentication Required</AlertTitle>
            <AlertDescription>
              Please log in to create flashcards
            </AlertDescription>
          </Alert>
        </div>
      </div>
    );
  }

  return (
    <div className="AddFlashCard page">
      <h1 className="page-header">Create Flashcards</h1>
      <div className="container">
        {error && (
          <Alert variant="destructive">
            <ExclamationTriangleIcon className="h-4 w-4" />
            <AlertTitle>Error</AlertTitle>
            <AlertDescription>{error}</AlertDescription>
          </Alert>
        )}
        {success && (
          <Alert>
            <CheckCircledIcon className="h-4 w-4" />
            <AlertTitle>Success</AlertTitle>
            <AlertDescription>{success}</AlertDescription>
          </Alert>
        )}

        <Card className="p-6">
          <div>
            <h4 className="flashcard-header">
              What are you creating flashcards for?
            </h4>
            <Input
              type="text"
              label="Title"
              placeholder="Enter title"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              className="mb-3"
              required
            />
          </div>

          <div>
            <h4 className="flashcard-header">
              What's a good description for the flashcards?
            </h4>
            <Input
              type="text"
              label="Description"
              placeholder="Enter description"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              className="mb-3"
              required
            />
          </div>

          <div>
            <h4 className="flashcard-header">Information on the topic</h4>
            <Textarea
              label="Information"
              placeholder="Enter information"
              value={information}
              onChange={(e) => setInformation(e.target.value)}
              className="mb-3"
              minRows={3}
              required
            />
          </div>

          <div>
            <h4 className="flashcard-header">
              Tags <span>(separate with commas)</span>
            </h4>
            <Input
              type="text"
              label="Tags"
              placeholder="Add tags and press comma"
              value={inputTag}
              onChange={handleTagInput}
              className="mb-3"
            />

            <div className="tag-input-container">
              {tags.map((tag, index) => (
                <div className="tag" key={index}>
                  {tag}
                  <span className="tag-close" onClick={() => removeTag(index)}>
                    &times;
                  </span>
                </div>
              ))}
            </div>
          </div>

          <p>Character Count: {information.length}</p>
          <Button
            color="primary"
            variant="solid"
            className="primary-btn"
            onClick={handleSubmit}
          >
            Generate Flashcard Stack
          </Button>
        </Card>
      </div>
    </div>
  );
};

export default AddFlashCard;
