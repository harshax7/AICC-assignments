from textblob import TextBlob

# Step 1: Sample Movie Reviews
reviews = [
    "The movie was amazing and full of suspense",
    "I hated the film, it was too boring",
    "The acting was okay but the story was dull",
    "What a fantastic movie, I loved it",
    "Terrible experience, waste of time"
]

# Step 2: Analyze Sentiment
print("Movie Review Sentiment Analysis:\n")

for i, review in enumerate(reviews):
    blob = TextBlob(review)
    
    polarity = blob.sentiment.polarity  # range: -1 to +1
    
    # Step 3: Classify sentiment
    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😡"
    else:
        sentiment = "Neutral 😐"
    
    print(f"Review {i+1}: {review}")
    print(f"Sentiment: {sentiment}\n")