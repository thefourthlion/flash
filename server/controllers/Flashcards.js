const Flashcards = require("../models/Flashcards");
exports.createFlashcards = async (req, res) => {

  try {
    let newFlashcards = new Flashcards({
      title: req.body.title,
      description: req.body.description,
      information: req.body.information,
      cards: req.body.cards,
      timestamp: req.body.timestamp,
      author:req.body.author,  
      votes:req.body.votes,  
      subscribers:req.body.subscribers,     
      tags:req.body.tags,  
    });
    await newFlashcards.save();
    res.send(newFlashcards);
  } catch (err) {
    console.log(err);
  }
};
exports.readFlashcards = async (req, res) => {
    const page = req.query.page || 0;
    const limit = req.query.limit || 25;
  try {
    Flashcards.find({}, (err, result) => {
      if (err) {
        res.json({ app: err });
      }
      res.send(result);
    })
      .sort()
      .skip(page * limit)
      .limit(limit);
  } catch (err) {
    console.log(err);
  }
};
exports.readFlashcardsFromID = async (req, res) => {
  try {
    await Flashcards.findById({ _id: req.params.id }, {}, (err, result) => {
      if (err) {
        res.json({ app: err });
      }
      res.send(result);
    });
  } catch (err) {
    console.log(err);
  }
};

exports.oldUpdateFlashcards = async (req, res) => {
  try {
    await Flashcards.findByIdAndUpdate(
      req.params.id,
      {
        title: req.body.title,
        description: req.body.description,
        information: req.body.information,
        cards: req.body.cards,
        timestamp: req.body.timestamp,
        author:req.body.author,  
        votes:req.body.votes,  
        subscribers:req.body.subscribers,     
        tags:req.body.tags,  
      },
      (err, result) => {
        if (err) {
          res.json({ app: err });
        }
        res.send(result);
      }
    );
  } catch (err) {
    console.log(err);
  }
};

exports.updateFlashcards = async (req, res) => {
  console.log("🔄 Update flashcards endpoint hit");
  console.log("Request body:", req.body);
  console.log("Flashcard ID:", req.params.id);

  try {
    const updatedFlashcards = await Flashcards.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true }
    );
    console.log("✅ Updated flashcards:", updatedFlashcards);
    res.json(updatedFlashcards);
  } catch (error) {
    console.error("❌ Error updating flashcards:", error);
    res.status(500).json({ error: "Failed to update flashcards" });
  }
};


exports.deleteFlashcards = async (req, res) => {
  try {
    if ((await Flashcards.findById(req.params.id)) === null) {
      res.json({ app: "post not found" });
    } else {
      await Flashcards.findByIdAndRemove(req.params.id).exec();
      res.json({ app: "post deleted" });
    }
  } catch (err) {
    console.log(err);
    res.send(err);
  }
};

exports.editFlashcardsWithAI = async (req, res) => {
  const { id, information } = req.body;

  try {
    // First, find the existing flashcard set
    const existingFlashcards = await Flashcards.findById(id);
    
    if (!existingFlashcards) {
      return res.status(404).json({ error: "Flashcard set not found" });
    }

    // Update the information field and save
    existingFlashcards.information += "\n" + information;
    
    // Combine existing cards with new cards
    if (req.body.newCards && Array.isArray(req.body.newCards)) {
      existingFlashcards.cards = [...existingFlashcards.cards, ...req.body.newCards];
    }

    // Save the updated document
    await existingFlashcards.save();

    res.status(200).json({
      message: "Flashcards updated successfully",
      data: existingFlashcards
    });
  } catch (error) {
    console.error("Error updating flashcards with AI:", error);
    res.status(500).json({ error: "Failed to update flashcards" });
  }
};
