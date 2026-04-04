from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

documents = [
    "AI is transforming the world",
    "Machine learning is a part of AI",
    "Deep learning advances AI applications",
    "AI is used in healthcare and finance",
    "Machine learning improves predictions"
]

# TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)

feature_names = vectorizer.get_feature_names_out()

# Convert to DataFrame
df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)

# 🔹 Step: Sum TF-IDF scores across all documents
word_scores = df.sum(axis=0)

# 🔹 Sort words by importance
top_words = word_scores.sort_values(ascending=False)

# 🔹 Display top 5 keywords
print("Top Keywords Across All Documents:\n")

for word, score in top_words.head(5).items():
    print(f"{word} ")