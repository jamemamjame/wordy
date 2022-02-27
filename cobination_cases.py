from typing import List


def recur(li, position: int):
    global all_possible_cases
    if position >= len(li):
        all_possible_cases.append(li.copy())
        return

    li[position] = 'W'
    recur(li, position + 1)

    li[position] = 'Y'
    recur(li, position + 1)

    li[position] = 'G'
    recur(li, position + 1)


all_possible_cases: List[List[str]] = []
recur(['W️', 'W️', 'W️', 'W️', 'W️'], 0)
