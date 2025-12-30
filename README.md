# 🎓 Quizificate

### Video Demo: https://youtu.be/aPzX14sKnLQ

Quizificate is a Python-based quiz application that tests users on programming language knowledge and rewards successful participants with a personalized PDF certificate.

This project was developed as a final project and demonstrates file handling, testing, modular design, and PDF generation in Python.

# 🚀 Features

* 📚 Loads quiz questions from a JSON file

* 🔀 Randomizes questions on each run

* 🎨 Colorful terminal interface using colorama

* ⏱ Simulated quiz timing for better user experience

* 🧮 Automatic scoring system

* 🏆 Generates a professional PDF certificate for users who score 70% or higher

* 🧪 Fully tested using pytest and monkeypatch

# 🗂 Project Structure
.
├── project.py
├── test_project.py
├── data/
│   └── questions.json
├── assets/
│   └── background.jpg
├── certificates/
│   └── (generated PDF certificates)
└── README.md

# 🧠 How It Works

* The user enters their name

* Quiz questions are loaded from data/questions.json

* Questions are displayed one by one with multiple-choice answers

* Each correct answer gives 10 points

* If the user scores at least 70%, a PDF certificate is generated

* The certificate is saved inside the certificates/ directory

# ▶️ How to Run
## 1️⃣ Install dependencies
pip install fpdf colorama pytest

## 2️⃣ Run the application
python project.py

## 3️⃣ Run tests
pytest

# 🧪 Testing

## This project includes unit tests for all major functions:

* load_questions

* run_quiz

* generate_certificate

* main

**The monkeypatch fixture is used to mock user input and isolate external dependencies such as file access and certificate generation.**

# 📄 Certificate Generation

## Certificates are generated using the FPDF library

Output format: A4 (Landscape)

Includes:

* Date

* User name

* Score

* Background image

**Saved as:**

**certificates/<name>_certificate.pdf**

# 💡 Notes

Quiz questions can be easily extended by editing data/questions.json

Certificate background image can be customized in assets/background.jpg

The project follows modular design and clean coding practices

# 👨‍💻 Author

**Mahdyar Talebi**