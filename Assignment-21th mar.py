import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def clean_text(text):

    text = text.upper()
    
    text = re.sub(r'[^\w\s]', '', text)
    
    words = text.split()
    words = [word for word in words if word not in stop_words]
    
    return " ".join(words)

sample = "omg!! i love this product soo much😍😍"
print(clean_text(sample))