# tokenizer.py

import re
import string
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

def tokenize(text):
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text.lower())
    tokens = text.split()
    tokens = [token for token in tokens if token.isalpha()]
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens
