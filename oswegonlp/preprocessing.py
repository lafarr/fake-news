from collections import Counter

import numpy as np
import pandas as pd

from oswegonlp.re_tokenizer import RegexTokenizer


# deliverable 1.1
def bag_of_words(text, retok):
    """
    Count the number of word occurences for each document in the corpus

    :param retok: an instance of RegexTokenizer
    :param text: a document, as a single string
    :returns: a Counter for a single document
    :rtype: Counter
    """

    return Counter(retok.tokenize(text))


# deliverable 1.2
def aggregate_word_counts(bags_of_words):
    """
    Aggregate word counts for individual documents into a single bag of words representation

    :param bags_of_words: a list of bags of words as Counters from the bag_of_words method
    :returns: an aggregated bag of words for the whole corpus
    :rtype: Counter
    """

    counter = Counter()
    for bow in bags_of_words:
        counter += Counter(bow)
    return counter


# deliverable 1.3
def compute_oov(bow1, bow2):
    """
    Return a set of words that appears in bow1, but not bow2

    :param bow1: a bag of words
    :param bow2: a bag of words
    :returns: the set of words in bow1, but not in bow2
    :rtype: set
    """

    bow1_set = set(bow1.copy())
    bow2_set = set(bow2.copy())
    return bow1_set.difference(bow2_set)


# deliverable 1.4
def prune_vocabulary(counts, target_data, min_count):
    """
    prune target_data to only words that appear at least min_counts times in count

    :param counts: aggregated Counter for training data
    :param target_data: list of Counters containing dev bow's
    :param min_count: threshold
    :returns: new list of Counters, with pruned vocabulary
    :returns: list of words in pruned vocabulary
    :rtype: list of Counters, set
    """

    new_counters = []
    pruned_vocab = set()
    for bow in target_data:
        d = {}
        for k, v in bow.items():
            count = counts[k]
            if count >= min_count:
                d.update({k: counts[k]})
                pruned_vocab.add(k)
        new_counters.append(d)
    return new_counters, pruned_vocab


# deliverable 5.1
def make_numpy(bags_of_words, vocab):
    """
    Convert the bags of words into a 2D numpy array

    :param bags_of_words: list of Counters
    :param vocab: pruned vocabulary
    :returns: the bags of words as a matrix
    :rtype: numpy array
    """
    vocab = sorted(vocab)

    raise NotImplementedError


### Helper Code ###

def read_data(filename, label='RealOrFake', preprocessor=bag_of_words):
    retok = RegexTokenizer("[A-Za-z']+")
    df = pd.read_csv(filename)
    return df[label].values, [preprocessor(string, retok) for string in df['Headline'].values]


def oov_rate(bow1, bow2):
    return len(compute_oov(bow1, bow2)) / len(bow1.keys())
