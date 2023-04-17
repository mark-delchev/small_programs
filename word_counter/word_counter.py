import nltk
from collections import Counter

nltk.download('punkt')
# Load the text data
with open('edited_data.txt', 'r') as f:
    text = f.read()

# Tokenize the text data
tokens = nltk.word_tokenize(text)

# Count the frequency of each word
word_counts = Counter(tokens)

# Sort the words by frequency
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Print the top 10 most common words
for word, count in sorted_words[:10]:
    print(word, count)
