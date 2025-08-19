import re

# Very basic text cleaning
def clean_text(text):
    text = text.lower()                  # lowercase everything
    text = re.sub(r'\s+', ' ', text)     # remove extra spaces
    text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
    return text.strip()
