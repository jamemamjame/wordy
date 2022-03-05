"""
This script is using for pre-calculate probability of WORDS x 243 possible FEEDBACK CASE
"""
from wordy.utils import ALL_WORDS
import pickle

from wordy.words_probs_calculator import calculate_words_prob

words_prob = calculate_words_prob(ALL_WORDS, ALL_WORDS)
with open('../wordy/resources/words_prob.pickle', 'wb') as f:
    pickle.dump(words_prob, f)
