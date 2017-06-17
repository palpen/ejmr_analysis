"""
how to prepapre the data needed to train a Naive Bayes Classifier

problems:
- classifier not working very well (ask StackOver Flow)
    - negative sentiment assigned for very obviously positive sentiments

"""

import nltk
import random
from nltk.corpus import movie_reviews

print "Create and shuffle documents"
# create a list of tuples containing the list of words in each document AND the category for that document (whether positive or negative)

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# shuffle it because we will use this to split between training and test data
random.shuffle(documents)

print "Create word used to train classifier"
# we only want to train on the most frequently used words, not all words because most document will contain most of its words in word_features. Saves time.
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:25000]


def document_features(word_list):
    """
    input: a list of words from a word_list
    output: a dictionary of words in word_features and a key indicating whether that word is in the word_list
    note: we are only using words in the word_features list
    """

    # check to make sure no strings are passed through and only list (BIG GOTCHA!)
    assert not isinstance(word_list, basestring)

    document_words = set(word_list)

    features = {}

    # if word in word_features is in word_list words, then
    for word in word_features:

        # this is how you add an element to a dictionary; LHS is the key, RHS is values
        features['contains({0})'.format(word)] = (word in document_words)

    return features

# print "Create feature set"
# run document_features on all the documents
# c: pos or neg; d:
featuresets = [(document_features(d), c) for (d, c) in documents]

train_set, test_set = featuresets[100:], featuresets[:100]

print "Train classifier"
classifier = nltk.NaiveBayesClassifier.train(train_set)


#### post training tests


def tokenizer(sentence):

    return [word.lower() for word in nltk.word_tokenize(sentence)]


print "Tests"
sent1 = r"gavan spiders elgar kids cooking"
sent2 = r"the actors were very good"
sent3 = r"This dish is delicious"

for k, v in document_features(tokenizer(sent1)).items():
    if v is True:
        print "%s%s" % (k, v)

for k, v in document_features(tokenizer(sent2)).items():
    if v is True:
        print "%s%s" % (k, v)

for k, v in document_features(tokenizer(sent3)).items():
    if v is True:
        print "%s%s" % (k, v)


print "{0}: {1}".format(sent1, classifier.classify(document_features(tokenizer(sent1))))
print "{0}: {1}".format(sent2, classifier.classify(document_features(tokenizer(sent2))))
print "{0}: {1}".format(sent3, classifier.classify(document_features(tokenizer(sent3))))



