"use client";
import React, { useEffect, useState } from "react";
import axios from "axios";
import Link from "next/link";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faBrain,
  faPen,
  faTrash,
  faSyncAlt,
} from "@fortawesome/free-solid-svg-icons";
import "../../../styles/ViewStacks.scss";
import { Card } from "@/components/ui/card";


const ViewStacks = () => {
  const [stacks, setStacks] = useState([]);
  const [expanded, setExpanded] = useState({});

  useEffect(() => {
    // Fetch the flashcard stacks from the API
    const fetchStacks = async () => {
      try {
        const response = await axios.get(
          `${process.env.NEXT_PUBLIC_API_URL}/api/flashcards/read`
        );
        setStacks(response.data);
      } catch (error) {
        console.error("Error fetching stacks:", error);
      }
    };

    fetchStacks();
  }, []);

  const refreshPage = () => {
    window.location.reload();
  };

  const deleteStack = async (stackId) => {
    try {
      await axios.delete(
        `${process.env.NEXT_PUBLIC_API_URL}/api/flashcards/delete/${stackId}`
      );
      refreshPage();
    } catch (error) {
      console.error("Error deleting the stack:", error);
    }
  };

  const refreshCards = async (stack) => {
    try {
      const today = new Date();
      const todayUTC = new Date(
        Date.UTC(
          today.getUTCFullYear(),
          today.getUTCMonth(),
          today.getUTCDate()
        )
      ).toISOString();

      // Loop over each card and update it individually
      for (const card of stack.cards) {
        const updatedCard = {
          ...card,
          nextPracticeDate: todayUTC,
        };

        // Send a POST request to update the card
        await axios.post(
          `${process.env.NEXT_PUBLIC_API_URL}/api/flashcards/update/${stack._id}`,
          {
            cardId: card._id,
            updatedCard,
          }
        );
      }

      alert("All cards in this stack have been refreshed.");
      refreshPage(); // Refresh the page to reflect the changes
    } catch (error) {
      console.error("Error refreshing the cards:", error);
    }
  };

  const toggleExpand = (id) => {
    setExpanded((prevState) => ({
      ...prevState,
      [id]: !prevState[id],
    }));
  };

  const getShortDescription = (desc, id) => {
    const charLimit = 100;
    if (desc.length > charLimit) {
      return expanded[id] ? desc : `${desc.substring(0, charLimit)}...`;
    }
    return desc;
  };

  // Helper function to check if a card is due for review
  const isCardDueForReview = (nextPracticeDate) => {
    // Get today's date in UTC without the time part
    const today = new Date();
    const todayUTC = new Date(
      Date.UTC(today.getUTCFullYear(), today.getUTCMonth(), today.getUTCDate())
    );

    // Convert the card's nextPracticeDate to a Date object in UTC
    const cardDate = new Date(nextPracticeDate);
    const cardDateUTC = new Date(
      Date.UTC(
        cardDate.getUTCFullYear(),
        cardDate.getUTCMonth(),
        cardDate.getUTCDate()
      )
    );

    // Return true if the card is due today or earlier
    return cardDateUTC <= todayUTC;
  };

  return (
    <div className="ViewStacks page">
      <div className="container">
        <h1 className="page-header">Your Stacks of Flashcards</h1>
        <div className="stacks-list">
          {stacks.map((stack) => {
            const dueFlashcardsCount = stack.cards.filter((card) =>
              isCardDueForReview(card.nextPracticeDate)
            ).length;

            return (
              <Card key={stack._id} className="p-6 stack-card">
                <div className="stack-info">
                  <h3 className="stack-header">{stack.title}</h3>

                  {/* Shortened description with toggle */}
                  <p className="stack-description">
                    {getShortDescription(stack.description, stack._id)}
                    {stack.description.length > 100 && (
                      <span
                        className="toggle-expand"
                        onClick={() => toggleExpand(stack._id)}
                      >
                        {expanded[stack._id] ? "Show Less" : "Show More"}
                      </span>
                    )}
                  </p>

                  <hr/>

                  <h4 className="stack-count">
                    <span className="stack-count-num">
                      {/* Display flashcards to review out of the total */}
                      {dueFlashcardsCount}/{stack.cards.length}
                    </span>{" "}
                    Flashcards to Review
                  </h4>
                </div>

                {/* Icons for actions: Review, Edit, Delete, Refresh */}
                <div className="stack-actions">
                  {dueFlashcardsCount > 0 ? (
                    // If there are flashcards due, make the icon clickable
                    <Link href={`/pages/flashcards/${stack._id}`} passHref>
                      <FontAwesomeIcon
                        icon={faBrain}
                        size="2x"
                        title="Review Stack"
                        className="fa-icon fa-brain"
                      />
                    </Link>
                  ) : (
                    // If no flashcards are due, grey out the icon and make it non-clickable
                    <FontAwesomeIcon
                      icon={faBrain}
                      size="2x"
                      title="No Flashcards to Review"
                      className="fa-icon fa-brain disabled-icon grey-icon"
                    />
                  )}

                  {/* Edit Stack Icon */}
                  <Link href={`/pages/edit-flashcards/${stack._id}`} passHref>
                    <FontAwesomeIcon
                      icon={faPen}
                      size="2x"
                      title="Edit Stack"
                      className="fa-icon fa-pen"
                    />
                  </Link>

                  {/* Delete Stack Icon */}
                  <FontAwesomeIcon
                    icon={faTrash}
                    size="2x"
                    title="Delete Stack"
                    className="fa-icon fa-trash"
                    onClick={() => {
                      if (
                        window.confirm(
                          "Are you sure you want to delete this stack?"
                        )
                      ) {
                        deleteStack(stack._id);
                      }
                    }}
                  />

                  {/* Refresh Stack Icon */}
                  <FontAwesomeIcon
                    icon={faSyncAlt}
                    size="2x"
                    title="Refresh Cards"
                    className="fa-icon fa-sync"
                    onClick={() => {
                      if (
                        window.confirm(
                          "Are you sure you want to refresh all cards in this stack? This will reset their next practice date to today."
                        )
                      ) {
                        refreshCards(stack);
                      }
                    }}
                  />
                </div>
              </Card>
            );
          })}
        </div>
      </div>
    </div>
  );
};

export default ViewStacks;

