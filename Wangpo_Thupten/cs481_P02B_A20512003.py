import nltk
from nltk.corpus import brown, reuters, stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


    
    
# Ask the user to enter a sentence S from a keyboard.
S = input("Please enter a sentence S from a keyboard: ")

# Apply lowercasing to S.
S = S.lower()

#Calculate P(S) assuming a 2-gram language model (assume that probability of any bigram starting or ending a sentence is 0.25)


nltk.download('brown')


brown_words = brown.words()
brown_words = [word.lower() for word in brown_words]
brownFrequenciesAndWords = dict()
frequencyDistributionBrown = nltk.FreqDist(word for word in brown_words) 
for word in brown_words:
    brownFrequenciesAndWords[word] = frequencyDistributionBrown[word]
tokensOfS = word_tokenize(S)
unigramFreq = dict()
unigrams_brown = sum(frequencyDistributionBrown.values())
#print(f"brownFrequenciesAndWords is {brownFrequenciesAndWords}")

N = 2
bigramsInS = nltk.ngrams(S.split(), N)
bigramListS = [bigram for bigram in bigramsInS]
bigramsInBrown = nltk.ngrams(brown_words, N)
brownBigramList = [bigram for bigram in bigramsInBrown]
# print(f"In the brown corpus, there are {len(brownBigramList)} bigrams.")
bigramFreq = dict()
for bigram in brownBigramList: ## stopwords are not to be removed
    if bigram in bigramFreq:
        bigramFreq[bigram] += 1
    else:
        bigramFreq[bigram] = 1
first = tokensOfS[0]
last = tokensOfS.pop()
bigramProb = dict()
bigramProb[f"Probability of ('<s>' ,'{first}) is'"] = .25
for unigram, bigram in zip(tokensOfS, bigramListS):
    if bigram not in bigramFreq or unigram not in brownFrequenciesAndWords:
        bigramProb[f"Probability of {bigram}"] = 0
    else:
        bigramProb[f"Probability of {bigram} is"] = bigramFreq[bigram]/brownFrequenciesAndWords[unigram]
bigramProb[f"Probability of ('{last}','</s>') is"] = .25


# Display the sentence S, list all the individual bigrams and their probabilities, and the final probability P(S) on screen. It is fine if it is zero.
print("___________________________")
print(f"The sentence S is: '{S}'")
for i,v in zip(bigramProb.keys(),bigramProb.values()):
    print(f"{i} : {v}")
finalProb = 1
for prob in bigramProb.values():
    finalProb = finalProb*prob
print(f"The final probability P(S) is {finalProb}")

    
    
    