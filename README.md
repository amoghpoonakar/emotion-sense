# EmotionSense

EmotionSense is an AI-powered emotion detection chat application that analyzes user messages and predicts emotions in real time using Natural Language Processing and Machine Learning.

The project is designed as an interactive emotional assistant capable of understanding user moods from text and responding accordingly.

This project is currently in its early stages and has a long way to go. Future updates will focus on smarter conversations, improved UI/UX, voice emotion analysis, mood tracking, and AI-powered mental wellness features.

---

# Features

- Real-time emotion detection from text
- Emotion-aware chatbot responses
- NLP-based text preprocessing
- Machine Learning emotion classification
- Interactive Streamlit interface
- Lightweight and beginner-friendly architecture
- Easy to train with custom datasets

---

# Supported Emotions

The current model can detect emotions such as:

- Joy
- Sadness
- Anger
- Fear
- Love
- Surprise
- Neutral


More emotions and contextual understanding will be added in future versions.

---

# Tech Stack

## Languages
- Python

## Libraries & Frameworks
- Streamlit
- Scikit-learn
- Pandas
- NLTK

## ML Concepts Used
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Logistic Regression
- Text Classification

---

# Project Structure

```bash
emotion-chatbot/
│
├── app.py
├── train_model.py
├── responses.py
├── emotions.csv
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/emotion-chatbot.git
```

Move into the project folder:

```bash
cd emotion-chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Train The Model

Run:

```bash
python train_model.py
```

This will:
- preprocess the dataset
- train the ML model
- save the trained model and vectorizer

---

# Run The Application

Start the Streamlit app:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

# Example Inputs

```text
"I feel really stressed today."
→ Fear / Sadness

"I just achieved my goal!"
→ Joy

"I'm extremely angry right now."
→ Anger
```

---

# Model Information

| Component | Used |
|---|---|
| Vectorizer | TF-IDF |
| Algorithm | Logistic Regression |
| Learning Type | Supervised Learning |
| Accuracy | ~90% |

---

# Future Plans

This project is only the beginning.

Planned future improvements include:

- Better conversational AI
- Voice emotion detection
- Mood analytics dashboard
- Emotion history tracking
- AI journaling
- Anonymous emotional support spaces
- Music recommendations based on mood
- Deep learning integration
- Mobile app version
- Real-time speech analysis

---

# Project Goal

The vision behind EmotionSense is to create a human-centered AI experience capable of understanding emotions instead of just processing text.

The long-term goal is to evolve this project into a smarter emotional wellness platform powered by AI.

---

# Contributions

Contributions, suggestions, and ideas are always welcome.

This project is still evolving and experimenting with new possibilities.

---

# License

This project is currently open for learning and educational purposes.

---

# Developer

Built by Amogh Poonakar.

Passionate about building experimental tech, AI systems, and unconventional ideas.

---
