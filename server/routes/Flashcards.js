const express = require("express");
const router = express.Router();
const {
  createFlashcards,
  readFlashcards,
  readFlashcardsFromID,
  updateFlashcards,
  oldUpdateFlashcards,
  deleteFlashcards,
  editFlashcardsWithAI,
} = require("../controllers/Flashcards");
router.route("/create").post(createFlashcards);
router.route("/read").get(readFlashcards);
router.route("/read/:id").get(readFlashcardsFromID);
router.route("/old-update/:id").post(oldUpdateFlashcards);
router.route("/update/:id").post(updateFlashcards);
router.route("/delete/:id").delete(deleteFlashcards);
router.route("/edit").post(editFlashcardsWithAI);
module.exports = router;
