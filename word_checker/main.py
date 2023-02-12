import nltk
nltk.download('words')
from nltk.corpus import words
wordlist = set(words.words())

def is_real_word(word):
    return word.lower() in wordlist

print(is_real_word("hello")) # prints True
print(is_real_word("hEllO")) # prints True
print(is_real_word("hEllOo")) # prints False
