import pickle
import math
from src.utils import ALL_POSSIBLE_CASES, ALL_WORDS


def calculate_gini_by_word(words_prob):
    result = dict()
    for word in ALL_WORDS:
        sum_square = 0
        for case in ALL_POSSIBLE_CASES:
            hash_case = ''.join(case)
            prob = words_prob.get((word, hash_case), 0)
            sum_square += prob ** 2
        gini_index = sum_square
        result[word] = gini_index
    result = dict(sorted(result.items(), key=lambda item: item[1]))
    return result


def calculate_entropy_by_word(words_prob):
    result = dict()
    for word in ALL_WORDS:
        sum_square = 0
        for case in ALL_POSSIBLE_CASES:
            hash_case = ''.join(case)
            prob = words_prob[word, hash_case]
            sum_square += prob * math.log(1 / prob, 2) if prob != 0 else 0
        total_entropy = sum_square
        result[word] = total_entropy
    result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
    return result


def calculate_avg_entropy_by_word(words_prob):
    result = dict()
    for word in ALL_WORDS:
        sum_square = 0
        for case in ALL_POSSIBLE_CASES:
            hash_case = ''.join(case)
            prob = words_prob[word, hash_case]
            sum_square += prob * math.log(1 / prob, 2) if prob != 0 else 0
        avg_entropy = sum_square / len(ALL_POSSIBLE_CASES)
        result[word] = avg_entropy
    result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
    return result


with open('src/resources/words_prob.pickle', 'rb') as f:
    words_prob = pickle.load(f)

# words_gini = calculate_gini_by_word(words_prob)
# words_entropy = calculate_entropy_by_word(words_prob)
