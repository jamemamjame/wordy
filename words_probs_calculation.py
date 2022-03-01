import concurrent.futures
from typing import List

from initial_resource import ALL_POSSIBLE_CASES
import match_cases as mc


def __update_words_prob(words_prob: dict, case: List[str], hash_case: str,
                        able_to_play_word: str, possible_words_answer: List[str]):
    for k, possible_answer_word in enumerate(possible_words_answer):
        words_prob[able_to_play_word, hash_case] += mc.is_match_case(
            candidate_word=possible_answer_word,
            labeled_word=able_to_play_word,
            case=case
        )
    words_prob[able_to_play_word, hash_case] /= len(possible_words_answer)
    print(f'done for case={hash_case} able_to_play_word={able_to_play_word}')


def calculate_words_prob(possible_words_to_play: List[str], possible_words_answer: List[str]):
    words_prob = dict()
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        for i, case in enumerate(ALL_POSSIBLE_CASES):
            hash_case = ''.join(case)
            print(f'{i + 1}/{len(ALL_POSSIBLE_CASES)}) {hash_case}')
            for j, able_to_play_word in enumerate(possible_words_to_play):
                words_prob[able_to_play_word, hash_case] = 0
                executor.submit(__update_words_prob, words_prob, case, hash_case,
                                able_to_play_word, possible_words_answer)
    return words_prob
