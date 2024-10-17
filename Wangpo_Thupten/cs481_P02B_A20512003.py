import nltk
from nltk.corpus import brown, reuters, stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


    
    
# Ask the user to enter a sentence S from a keyboard.
S = input("Please enter a sentence S from a keyboard: ")

# Apply lowercasing to S.
S = S.lower()

#[45 pts] Calculate P(S) assuming a 2-gram language model (assume that probability of any bigram starting or ending a sentence is 0.25)


nltk.download('brown')

def calculateProbability(count, total):
    return count / total if total > 0 else 0

brown_words = brown.words()
brown_words = [word.lower() for word in brown_words]
brownFrequenciesAndWords = dict()
frequencyDistributionBrown = nltk.FreqDist(word for word in brown_words) 
for word in brown_words:
    brownFrequenciesAndWords[word] = frequencyDistributionBrown[word]
tokensOfS = word_tokenize(S)
unigramFreq = dict()
unigrams_brown = sum(frequencyDistributionBrown.values())
for unigram in tokensOfS:
    count = frequencyDistributionBrown.get(unigram, 0)
    probability = calculateProbability(count, unigrams_brown) 
    unigramFreq[unigram] = probability
print(unigramFreq)