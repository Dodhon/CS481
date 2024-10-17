import nltk
from nltk.corpus import brown, reuters, stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


# Use Python’s NLTK package along with the Brown corpus (after removing all stop words; use the stopwords corpora for that purpose) for the following tasks:
nltk.download('brown')
nltk.download('stopwords')
print("_________________________________")
brown_words = brown.words()
stopWordsCorpus = set(nltk.corpus.stopwords.words('english'))
brown_words = [w for w in brown_words if w.lower() not in stopWordsCorpus] # stopwords removed
uniqueWordsBrown = set(brown_words)
print(uniqueWordsBrown)

w1 = input("Please enter 1 word: ")
while w1 not in uniqueWordsBrown:
    w1 = input("That is not a word in the Brown corpus. Please try again: ")
    
