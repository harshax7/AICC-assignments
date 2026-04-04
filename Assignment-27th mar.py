import spacy

nlp = spacy.load("en_core_web_md")

# Step 1: Word pairs
word_pairs = [
    ("car", "automobile"),
    ("happy", "joyful"),
    ("teacher", "student"),
    ("dog", "animal"),
    ("hot", "cold")
]

print("Semantic Similarity Between Word Pairs:\n")

for w1, w2 in word_pairs:
    token1 = nlp(w1)
    token2 = nlp(w2)
    
    similarity = token1.similarity(token2)
    
    print(f"{w1} - {w2} : {round(similarity, 3)}")