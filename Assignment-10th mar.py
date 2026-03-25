import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
data = {
    'message': [
        "Win a free iPhone now",
        "Hello, how are you?",
        "Congratulations, you won a lottery",
        "Let's meet tomorrow",
        "Claim your free prize now",
        "Are you coming to class?",
        "Get cash rewards instantly",
        "See you in college"
    ],
    'label': ['spam', 'ham', 'spam', 'ham', 'spam', 'ham', 'spam', 'ham']
}

df = pd.DataFrame(data)

X_train, X_test, y_train, y_test = train_test_split(
    df['message'], df['label'], test_size=0.25, random_state=42
)

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

y_pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nReport:\n", classification_report(y_test, y_pred))
new_msg = input("\nEnter a message: ")
new_vec = vectorizer.transform([new_msg])
prediction = model.predict(new_vec)

print("Prediction:", prediction[0])


'''This program builds a spam detection system using machine learning. The text messages are first converted into numerical form using TF-IDF vectorization, which measures the importance of words.

A Naive Bayes classifier is trained on labeled data (spam or ham). After training, the model predicts whether a new message is spam or not.

The system is evaluated using accuracy and classification metrics, making it a basic but effective spam filtering models'''