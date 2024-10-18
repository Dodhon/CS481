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
brownWordsFreq = dict()
for word in brown_words:
    if word in brownWordsFreq:
        brownWordsFreq[word] += 1
    else:
        brownWordsFreq[word] = 1
# print(uniqueWordsBrown)

w1 = input("Please enter 1 word: ")
while w1 not in uniqueWordsBrown:
    w1 = input("That is not a word in the Brown corpus. Please try again: ")
    
# Assuming a 2-gram language model, a menu with TOP 3 “most likely to follow W1” words (according to the W1, NEXT WORD probability estimate). For example, if the user started with W1 = “good”, the following could be displayed 

N = 2
bigramsInBrown = nltk.ngrams(brown_words, N)
brownBigramList = [bigram for bigram in bigramsInBrown]
brownBigramFreq = dict()
for bigram in brownBigramList:
    if bigram in brownBigramFreq:
        brownBigramFreq[bigram] += 1
    else:
        brownBigramFreq[bigram] = 1
        

goodInputs = set()
for i in range(3):
    goodInputs.add(i+1)
go = True
while go:
    max = [0,0]
    possibleBigrams = list()
    for bigram in brownBigramList:
        if bigram[0] == w1:
            possibleBigrams.append(bigram)
    for bigram in possibleBigrams:
        if brownBigramFreq[bigram] > max[1]:
            max[0] = bigram
            max[1] = brownBigramFreq[bigram]
        
        
               
    
    response = 0
    while response not in goodInputs:
        response = input(f"Which word should follow?\n 1\n 2\n 3\n 4\n Please pick a number 1-4")
        if response == f"1":
            pass
        if response == f"2":
            pass
        if response == f"3":
            pass
        if response == f"4":
            go = False
        else:
            response = 1 # place logic of response == 1 here
    
    