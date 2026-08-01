# 🎬 Movie Review Sentiment Analysis

This project is a simple Natural Language Processing (NLP) application that predicts whether a movie review is **Positive** or **Negative** using Machine Learning.

The idea behind this project was to understand how text data can be converted into numerical features and used to train a classification model. I also built a simple web application using **Streamlit** so users can test the model by entering their own movie reviews.

---

## 📌 Features

- Predicts whether a movie review is positive or negative.
- Uses TF-IDF Vectorization for text feature extraction.
- Trained with Logistic Regression.
- Interactive web interface built using Streamlit.
- Model saved using Pickle for faster predictions.
- Evaluated using multiple performance metrics.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle
- Matplotlib

---

## 📂 Project Structure

```
Movie-Review-Sentiment-Analysis/
│
├── app.py                 # Streamlit application
├── model.pkl              # Trained Logistic Regression model
├── scaler.pkl             # Saved TF-IDF Vectorizer
├── projectmodel.ipynb     # Jupyter Notebook
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. Load the movie review dataset.
2. Explore and understand the data.
3. Convert text into numerical features using TF-IDF Vectorizer.
4. Split the dataset into training and testing sets.
5. Train a Logistic Regression classifier.
6. Evaluate the model using different metrics.
7. Save the trained model and vectorizer.
8. Use Streamlit to make real-time predictions.

---

## 📊 Model Evaluation

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

These metrics provide a better understanding of how well the model performs beyond simple accuracy.

---

## 🚀 Running the Project

Clone the repository

```bash
git clone https://https://github.com/MUDASSARsd/sentiment-analysis-streamlit
```

Move into the project folder

```bash
cd movie-review-sentiment-analysis
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 💻 Demo

Enter any movie review in the text box and click **Predict**.

Example:

```
The movie was absolutely amazing with brilliant acting.
```

Prediction:

```
Positive Review
```

Example:

```
The movie was boring and a complete waste of time.
```

Prediction:

```
Negative Review
```

---

## 📚 What I Learned

Working on this project helped me understand:

- Text preprocessing for machine learning
- Feature extraction using TF-IDF
- Binary text classification
- Logistic Regression for NLP tasks
- Model evaluation using different metrics
- Building and deploying a Streamlit application
- Saving and loading machine learning models using Pickle

---

## 🔮 Future Improvements

- Add text preprocessing (stopword removal, stemming, lemmatization)
- Compare multiple machine learning models
- Improve prediction accuracy with hyperparameter tuning
- Deploy the application online
- Extend the project to classify multiple sentiment categories

---

## 👨‍💻 Author

**Mudassar Syed**

AIML Student passionate about Machine Learning, Natural Language Processing, and building practical AI applications.

If you found this project useful, feel free to ⭐ the repository.
