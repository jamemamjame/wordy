# -*- coding: utf-8 -*-
from initial_resource import ALL_WORDS
import pickle

from words_probs_calculation import calculate_words_prob

words_prob = calculate_words_prob(ALL_WORDS, ALL_WORDS)
with open('words_prob.pickle', 'wb') as f:
    pickle.dump(words_prob, f)
