# Flashy
Flashy is a simple and interactive flashcard application built with Python and Tkinter. It helps users learn French words by presenting them as flashcards with their English translations.

## Features

- Displays French words on the front of a virtual flashcard
- Shows the English translation when the card is flipped
- Tracks words the user knows and removes them from the learning deck
- Saves progress by creating a custom word list for future learning sessions

## Requirements

- Python 3.x
- Tkinter 
- Pandas

The application window will open, showing you French words. After 3 seconds, the card will flip to show the English translation. You can then mark whether you knew the word or not:

- Click the ✓ button if you knew the word. This will remove the word from your learning list.
- Click the ✗ button if you didn't know the word. This will keep the word in rotation.

## File Structure

- `main.py`: The main Python script
- `data/french_words.csv`: The original list of French-English word pairs
- `data/words_to_learn.csv`: The dynamically updated list of words the user is still learning
- `images/`: Directory containing the UI images (card front, card back, right and wrong buttons)

## Customization

You can customize the following aspects of the app:

- `BACKGROUND_COLOR`: Change the background color of the application
- Card flip time: Modify the `3000` milliseconds in the `window.after()` calls
- Fonts and text sizes in the `canvas.create_text()` calls

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the issues page if you want to contribute.

