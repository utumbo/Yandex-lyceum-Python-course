import re
from collections import Counter

def count_words(text:str):
    lower_text = re.sub(r'[^\w\s]', '', text.lower())
    words = lower_text.split()
    res = Counter(words)
    return res

print(count_words("Hello, hello world! World is great."))