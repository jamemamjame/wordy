from typing import List


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
    with open('src/resources/sgb-words.txt', 'r') as f:
        all_words = [l.strip() for l in f.readlines()]
    return all_words


ALL_POSSIBLE_CASES: List[List[str]] = []
recur(['W', 'W', 'W', 'W', 'W'], 0)

ALL_WORDS: List[str] = get_all_words()

COLOR = {
    'g': '🟩', 'y': '🟨', 'w': '⬜'
}
