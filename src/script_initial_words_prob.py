"""
This script is using for pre-calculate probability of WORDS x 243 possible FEEDBACK CASE
"""
from src.utils import ALL_WORDS
import pickle

from words_probs_calculation import calculate_words_prob

words_prob = calculate_words_prob(ALL_WORDS, ALL_WORDS)
with open('resources/words_prob.pickle', 'wb') as f:
    pickle.dump(words_prob, f)
