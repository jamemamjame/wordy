import os

from typing import List

PATH_WORDS = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources/sgb-words.txt')
PATH_WORDS_PROB = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources/words_prob.pickle')


def recur(li, position: int):
    global ALL_POSSIBLE_CASES
    if position >= len(li):
        ALL_POSSIBLE_CASES.append(li.copy())
        return

    li[position] = '⬜'
    recur(li, position + 1)

    li[position] = '🟨'
    recur(li, position + 1)

    li[position] = '🟩'
    recur(li, position + 1)


def get_all_words():
    global PATH_WORDS
    with open(PATH_WORDS, 'r') as f:
        all_words = [l.strip() for l in f.readlines()]
    return all_words


ALL_POSSIBLE_CASES: List[List[str]] = []
recur(['W', 'W', 'W', 'W', 'W'], 0)

ALL_WORDS: List[str] = get_all_words()

COLOR = {
    'g': '🟩', 'y': '🟨', 'w': '⬜'
}
