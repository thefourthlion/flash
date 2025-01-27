"use client";
import React, { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import axios from "axios";
import "../../../../styles/Flashcards.scss";
import Link from "next/link";
import { Button } from "@nextui-org/button";
import { Card } from "@/components/ui/card";


// Utility function to shuffle an array
const shuffleArray = (array) => {
  return array.sort(() => Math.random() - 0.5);
};

// SM-2 algorithm to update flashcard metadata
const updateFlashcardWithSM2 = (flashcard, quality) => {
  if (quality < 0 || quality > 5) {
    throw new Error("Quality must be between 0 and 5");
  }

  let repetitions = flashcard.repetitions || 0;
  let interval = flashcard.interval || 1;
  let easiness = flashcard.easiness || 2.5;

  // Update easiness factor
  easiness = Math.max(
    1.3,
    easiness + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
  );

  // Update repetitions and interval
  if (quality < 3) {
    repetitions = 0;
    interval = 1;
  } else {
    repetitions += 1;
    if (repetitions === 1) {
      interval = 1;
    } else if (repetitions === 2) {
      interval = 6;
    } else {
      interval = Math.round(interval * easiness);
    }
  }

  const millisecondsInDay = 24 * 60 * 60 * 1000;
  const nextPracticeDate = new Date(Date.now() + interval * millisecondsInDay).toISOString().split("T")[0];

  return { ...flashcard, repetitions, interval, easiness, nextPracticeDate };
};

const Flashcards = () => {
  const [flashcards, setFlashcards] = useState([]);
  const [currentCardIndex, setCurrentCardIndex] = useState(0);
  const [showAnswer, setShowAnswer] = useState(false);
  const [isFinished, setIsFinished] = useState(false);
  const [title, setTitle] = useState("");
  const [correctAnswers, setCorrectAnswers] = useState(0);

  const params = useParams();
  const id = params?.id;
  useEffect(() => {
    if (!id) return;
  
    const fetchFlashcards = async () => {
      try {
        console.log(`Fetching flashcards for ID: ${id}`);
        const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/api/flashcards/read/${id}`);
        console.log("Response from flashcard fetch:", response.data);
  
        // Get today's date in UTC without the time part
        const today = new Date();
        const todayUTC = new Date(Date.UTC(today.getUTCFullYear(), today.getUTCMonth(), today.getUTCDate()));
  
        // Filter flashcards due for review today or earlier
        const dueFlashcards = response.data.cards.filter((card) => {
          const cardDate = new Date(card.nextPracticeDate);
          const cardDateUTC = new Date(Date.UTC(cardDate.getUTCFullYear(), cardDate.getUTCMonth(), cardDate.getUTCDate()));
  
          console.log(`Comparing card date ${cardDateUTC.toISOString()} with today ${todayUTC.toISOString()}`);
  
          // Compare the UTC dates
          return cardDateUTC <= todayUTC;
        });
  
        if (dueFlashcards.length === 0) {
          console.log("No flashcards due for review.");
        } else {
          console.log(`Found ${dueFlashcards.length} flashcards due for review.`);
        }
  
        const shuffledFlashcards = shuffleArray(dueFlashcards).slice(0, 20);
        setFlashcards(shuffledFlashcards);
        setTitle(response.data.title);
      } catch (error) {
        console.error("Error fetching flashcards:", error);
      }
    };
  
    fetchFlashcards();
  }, [id]);
  
  

  const handleAnswer = async (quality) => {
    const updatedFlashcards = [...flashcards];
    const currentCard = updatedFlashcards[currentCardIndex];

    const updatedCard = updateFlashcardWithSM2(currentCard, quality);

    updatedFlashcards[currentCardIndex] = updatedCard;

    if (quality >= 3) {
      setCorrectAnswers((prev) => prev + 1);
    }

    try {
      await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/api/flashcards/update/${id}`, {
        cardId: updatedCard._id,
        updatedCard,
      });
    } catch (error) {
      console.error("Error updating flashcards:", error);
    }

    if (currentCardIndex < flashcards.length - 1) {
      setCurrentCardIndex(currentCardIndex + 1);
      setShowAnswer(false);
    } else {
      setIsFinished(true);
    }
  };

  const handleShowAnswer = () => {
    setShowAnswer(true);
  };

  const calculatePercentage = () => {
    return ((correctAnswers / flashcards.length) * 100).toFixed(2);
  };

  return (
    <div className="Flashcards page">
      <div className="container">
        <h1 className="page-header">{title} Flashcards</h1>
        <Card className="p-6" >
        {!isFinished && flashcards.length > 0 && (
          <div className="flashcard-card">
            <div className="flashcard-header question">
              <h3>{flashcards[currentCardIndex].question}</h3>
              <p className="card-count">
                {currentCardIndex + 1}/{flashcards.length}
              </p>
              {!showAnswer && (
                <Button color="primary" variant="solid" className="primary-btn" onClick={handleShowAnswer}>
                  Show Answer
                </Button >
              )}
            </div>

            {showAnswer && (
              <div className="answer">
                <p>{flashcards[currentCardIndex].answer}</p>
                <div className="buttons">
                  <p>Rate your recall:</p>
                  <div className="quality-buttons">
                    {[0, 1, 2, 3, 4, 5].map((quality) => (
                      <button 
                        key={quality}
                        className={`quality-circle quality-${quality}`}
                        onClick={() => handleAnswer(quality)}
                      />
                    ))}
                  </div>
                </div>
              </div>
            )}
          </div>
        )}

        {isFinished && (
          <div className="done">
            <p>You have completed the flashcards!</p>
            <p>Your score: {calculatePercentage()}%</p>
            <Link href="/pages/view-stacks">
              <Button color="primary" variant="solid" className="primary-btn">Finish</Button >
            </Link>
          </div>
        )}
      </Card></div>
    </div>
  );
};

export default Flashcards;
