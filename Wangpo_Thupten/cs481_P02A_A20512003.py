import nltk
from nltk.corpus import brown, reuters, stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

nltk.download('brown')
nltk.download('reuters')
nltk.download('stopwords')

#   1. obtain the word frequency distribution (after removing all stop words; use the stopwords corpora for that purpose) for BOTH corpora,
brown_words = brown.words()
reuters_words = reuters.words()
stopWordsCorpus = set(nltk.corpus.stopwords.words('english'))
# stopWordsCorpus = stopWordsCorpus.union(set(string.punctuation))
reutersFrequenciesAndWords = dict()
brownFrequenciesAndWords = dict()


reuters_words = [w for w in reuters_words if w.lower() not in stopWordsCorpus]
brown_words = [w for w in brown_words if w.lower() not in stopWordsCorpus]

frequencyDistributionReuters = nltk.FreqDist(word.lower() for word in reuters_words) #
frequencyDistributionBrown = nltk.FreqDist(word.lower() for word in brown_words) 

for word in reuters_words:
    reutersFrequenciesAndWords[word] = frequencyDistributionReuters[word]
for word in brown_words:
    brownFrequenciesAndWords[word] = frequencyDistributionBrown[word]

## display a top ten (ranks 1 through 10) words for BOTH corpora on screen (also place them in the table below)

brownFrequenciesAndWords = list(brownFrequenciesAndWords.items())
brownFrequenciesAndWords.sort(key = lambda a: a[1])
brownFrequenciesAndWords.reverse()
labelsBrown, frequenciesBrown = map(list, zip(*brownFrequenciesAndWords))
for index in range(10):
    print(labelsBrown[index] , ' ', frequenciesBrown[index])

reutersFrequenciesAndWords = list(reutersFrequenciesAndWords.items())
reutersFrequenciesAndWords.sort(key = lambda a: a[1])
reutersFrequenciesAndWords.reverse()
labelsReuters, frequenciesReuters = map(list, zip(*reutersFrequenciesAndWords))
for index in range(10):
    print(labelsReuters[index] , ' ', frequenciesReuters[index])


## generate log(rank) vs log(frequency) plots for the first 1000 (ranks 1 through 1000) words for BOTH corpora (you can use the matplotlib package or some other plotting package / tool). Place BOTH plots in the table below.

labelsBrown2 = labelsBrown[:200]
frequenciesBrown2 = frequenciesBrown[:200]
fig, ax = plt.subplots()
xs = range(len(labelsBrown2))
def format_fn(tick_val, tick_pos):
    if int(tick_val) in xs:
        return labelsBrown2[int(tick_val)]
    else:
        return ''
ax.xaxis.set_major_formatter(format_fn)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_yscale('log')
ax.plot(xs, frequenciesBrown2)
ax.set_title('Token frequency counts in Brown corpus [first 200 tokens]')
plt.xlabel('Word')
plt.ylabel('Frequency count')
plt.xticks(rotation=90)
plt.show()

labelsReuters2 = labelsReuters[:200]
frequenciesReuters2 = frequenciesReuters[:200]
fig, ax = plt.subplots()
xs = range(len(labelsReuters2))
def format_fn(tick_val, tick_pos):
    if int(tick_val) in xs:
        return labelsReuters2[int(tick_val)]
    else:
        return ''
ax.xaxis.set_major_formatter(format_fn)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_yscale('log')
ax.plot(xs, frequenciesReuters2)
ax.set_title('Token frequency counts in Reuters corpus [first 200 tokens]')
plt.xlabel('Word')
plt.ylabel('Frequency count')
plt.xticks(rotation=90)
plt.show()

#use frequency counts obtained earlier to calculate the unigram occurrence probability for the TWO (“technical” and not technical) words. Use lowercasing first! Display all relevant counts and probability on screen for BOTH corpora (also: enter final values in the table below). It can be zero for some words.


unigrams = ['adiabatic', 'dinner']
unigrams_brown = sum(frequencyDistributionBrown.values())
unigrams_reuters = sum(frequencyDistributionReuters.values())
def calculateProbability(count, total):
    return count / total if total > 0 else 0
for unigram in unigrams:
    count = frequencyDistributionBrown.get(unigram, 0)
    probability = calculateProbability(count, unigrams_brown)  
    print(f"Corpus: Brown, Unigram '{unigram}', Probability = {probability}")
for unigram in unigrams:
    count = frequencyDistributionReuters.get(unigram, 0)
    probability = calculateProbability(count, unigrams_reuters)  
    print(f"Corpus: Reuters, Unigram '{unigram}', Probability = {probability}")
