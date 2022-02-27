# -*- coding: utf-8 -*-
from cobination_cases import all_possible_cases
import match_cases as mc

with open('sgb-words.txt', 'r') as f:
    all_words = [l.strip() for l in f.readlines()]

possible_answer_words = all_words.copy()
words_prob = dict()
for i, case in enumerate(all_possible_cases):
    hash_case = ''.join(case)
    print(f'{i + 1}/{len(all_possible_cases)}) {hash_case}')
    for j, guess_word in enumerate(all_words[:1]):
        words_prob[guess_word, hash_case] = 0
        # TODO: check if never play this word yet
        # print(f'\t{j + 1}/{len(all_words)}) {guess_word}')
        for k, possible_answer_word in enumerate(possible_answer_words):
            # print(f'\t\t{k + 1}/{len(possible_answer_words)}) {possible_answer_word}')
            words_prob[guess_word, hash_case] += mc.is_match_case(
                next_guess_word=guess_word,
                possible_answer_word=possible_answer_word,
                case=case
            )
        words_prob[guess_word, hash_case] /= len(possible_answer_words)
