# 🃏 French Flashcards

A flashcard application built using Python Tkinter to help practice French vocabulary. Users have a limited time to recall a word before the correct translation is revealed.

## ✨ Technologies

- `Python`
- `Tkinter`
- `Pandas`
- `CSV`

## 🚀 Features

- Timed flashcards with automatic word reveal
- French-to-English vocabulary practice
- Track known and unknown words
- Saves unlearned words to a CSV file
- Clean, distraction-free UI

## 📍 The Process

This project was built as **Day 31 of the 100 Days of Python Code** course and focused on combining Tkinter with data handling using Pandas.

Each flashcard displays a French word and gives the user a few seconds to recall its meaning. If the timer runs out, the card automatically flips to reveal the English translation.

If the user remembers the word, they can mark it as known using the ✔ button. If they don’t know the word, they can press ✖ to skip it and move on without revealing the answer. Words that are not marked as known are saved to a separate file (`words_to_learn.csv`) so they can be reviewed and practiced later.

This project reinforced working with timers in Tkinter, managing application state, and using Pandas DataFrames and dictionary-based data structures to track learning progress.

## 🚦 Running the Project

1. Clone the repository  
2. Ensure the `data/` and `images/` folders are present  
3. Run the script: `python main.py`  
4. Recall the French word before the timer ends  
5. Use ✔ or ✖ to mark whether you knew the word

## 🎞️ Preview

https://github.com/user-attachments/assets/09edc78b-946a-4285-bb16-3fe76bc9e77b
