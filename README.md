A simple and interactive **flashcard learning app** built using Python and Tkinter to help users learn English-Hindi vocabulary.

## 📚 Features

- 💬 Displays Hindi words and flips to show English translation after 3 seconds
- ✅ Mark words as known to remove them from the learning set
- 💾 Saves progress automatically in `words_to_learn.csv`
- 🔁 Randomized word display for effective repetition
- 🖼️ Clean, image-based flashcard UI

## 🛠️ Tech Stack

- Python 3
- Tkinter (for GUI)
- Pandas (for CSV handling)

## 📁 Project Structure

flash-card-project-start/
│
├── data/
│   ├── English\_Hindi\_Vocabulary.csv     # Original vocabulary list
│   └── words\_to\_learn.csv               # Auto-generated progress file
│
├── images/
│   ├── card\_front.png
│   ├── card\_back.png
│   ├── right.png
│   └── wrong.png
│
├── main.py                              # Main Python script
└── README.md                            # Project documentation

## ▶️ How to Run

1. **Clone or download** this repository.
2. Make sure you have Python 3 installed.
3. Install the required libraries (if not already installed):

   ```bash
   pip install pandas
````

4. Run the app:

   ```bash
   python main.py
   ```
## 🔄 Usage Instructions

* When the app launches, you'll see a **Hindi word**.
* After **3 seconds**, the flashcard will **flip** to reveal the **English translation**.
* Click ✅ if you know the word (it will be removed from the study list).
* Click ❌ to skip and try another word.
* Your progress is saved automatically!

## 📌 Notes

* If `words_to_learn.csv` exists, the app continues from where you left off.
* If not, it loads the full word list from `English_Hindi_Vocabulary.csv`.

## 📦 Future Ideas

* Add pronunciation (Text-to-Speech)
* Add difficulty levels or categories (verbs, nouns, etc.)
* Turn into a mobile or web app

## 🙌 Credits

* Vocabulary data curated manually
* GUI inspired by [Angela Yu's 100 Days of Code Bootcamp](https://www.udemy.com/course/100-days-of-code/)

## 📄 License

This project is open-source and available under the MIT License.
