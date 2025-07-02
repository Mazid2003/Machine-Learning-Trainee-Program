# ✨ Sentiment Analysis on Text Data

**Date: 02/07/2025**

**📌 Project Overview**

This project implements a Sentiment Analysis system that predicts the sentiment (positive, negative, neutral) of input text using a deep learning model. The system leverages a pre-trained LSTM model along with a saved tokenizer to process text and classify sentiment efficiently.

**🎯 Objectives**

Build a sentiment classifier using deep learning techniques.

Preprocess text using tokenization and sequence padding.

Train and save an LSTM model for text classification.

Serve predictions through an interface for easy consumption.

Ensure modularity and extensibility for future enhancements.

## ⚙ Technology Stack

- Python

- TensorFlow / Keras

- scikit-learn

- Flask

- Pickle

- NumPy / Pandas

- Matplotlib (for visualization during development)

**📂 Project Structure**
```
📂 SentimentAnalysis
 ├── tokenizer1.pkl             # Saved tokenizer for preprocessing input text
 ├── templates
       └── index.html
 ├── sentiment_lstm1.h5         # Trained LSTM model file
 ├── app.py                     # Flask app to serve sentiment predictions
 ├── test_cases.py              # Example test inputs for validation
 ├── requirements.txt           # Python dependencies
 └── README.md                  # Project documentation
```
## 🧠 Model Summary

- Architecture: Embedding layer → LSTM layer → Dense layer with softmax activation.

- Loss function: Categorical cross-entropy.

- Optimizer: Adam.

- Metric: Accuracy.

- Training Data: Labeled text data with sentiment tags.

- Input: Raw text → Tokenized → Padded sequence.

Output: Sentiment label (positive, negative, neutral).

## 🎨 Features

Supports sentiment classification for custom input text.

Pre-trained and ready for deployment.

Lightweight, easy to integrate with other applications.

Includes a simple interface for testing and prediction.

Modular design for easy upgrades (e.g., multi-language support).

## 📝 How It Works

The input text is cleaned, tokenized, and converted to a padded sequence using the saved tokenizer.

The sequence is fed to the pre-trained LSTM model.

The model outputs a probability distribution over sentiment classes, and the class with the highest probability is selected as the prediction.

## 📈 Results

The model achieves reliable sentiment predictions on a validation dataset.

**Example outputs:**
```
“I absolutely love this product!” → positive

“This is the worst service ever.” → negative

“It was okay, nothing special.” → neutral
```
Training and validation curves (accuracy and loss) demonstrate stable learning and good generalization.

## 🚀 Future Enhancements

- Train on larger or domain-specific datasets.

- Add support for additional languages.

- Integrate attention mechanisms for interpretability.

- Deploy on cloud platforms (AWS, GCP, Heroku).

- Add visualization of important words or phrases influencing predictions.

## 📌 How to Run

Clone the repository.

Install dependencies from requirements.txt.

Run the app locally and send text for prediction via the API interface.

## 💡 Key Takeaways

This project demonstrates how to build, train, save, and deploy a deep learning-based sentiment analysis model. It highlights practical steps from data preprocessing to serving predictions, making it a solid foundation for real-world NLP applications.
