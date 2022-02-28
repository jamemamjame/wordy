import concurrent.futures
from typing import List

from initial_resource import ALL_POSSIBLE_CASES
import match_cases as mc


def __update_words_prob(words_prob: dict, case: List[str], hash_case: str, possible_words_to_play: List[str],
                        possible_words_answer: List[str]):
    for j, able_to_play_word in enumerate(possible_words_to_play):
        words_prob[able_to_play_word, hash_case] = 0
        for k, possible_answer_word in enumerate(possible_words_answer):
            words_prob[able_to_play_word, hash_case] += mc.is_match_case(
                candidate_word=possible_answer_word,
                labeled_word=able_to_play_word,
                case=case
            )
        words_prob[able_to_play_word, hash_case] /= len(possible_words_answer)


def calculate_words_prob(possible_words_to_play: List[str], possible_words_answer: List[str]):
    words_prob = dict()
    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        for i, case in enumerate(ALL_POSSIBLE_CASES):
            hash_case = ''.join(case)
            print(f'{i + 1}/{len(ALL_POSSIBLE_CASES)}) {hash_case}')
            executor.submit(__update_words_prob, words_prob, case, hash_case, possible_words_to_play,
                            possible_words_answer)
    return words_prob
