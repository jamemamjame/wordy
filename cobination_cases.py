from typing import List


def recur(li, position: int):
    global all_possible_cases
    if position >= len(li):
        all_possible_cases.append(li.copy())
        return

    li[position] = '⬜'
    recur(li, position + 1)

    li[position] = '🟨'
    recur(li, position + 1)

    li[position] = '🟩'
    recur(li, position + 1)


all_possible_cases: List[List[str]] = []
recur(['W', 'W', 'W', 'W', 'W'], 0)
