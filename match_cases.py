from typing import List


def is_match_case(next_guess_word: str, possible_answer_word: str, case: List[str]) -> bool:
    result = True
    for i, c in enumerate(case):
        if c == 'G':
            result = result and (next_guess_word[i] == possible_answer_word[i])
        elif c == 'W️':
            result = result and (next_guess_word[i] not in possible_answer_word)
        elif c == 'Y':
            result = result and (
                    next_guess_word[i] in next_guess_word and next_guess_word[i] != possible_answer_word[i])
        else:
            raise ValueError(f'Unknown charactor {c} len={len(c)}')
        if not result:
            return False
    return True


def test_is_match_case():
    assert is_match_case('async', 'again', ['G', 'W', 'W', 'Y', 'W']) == True
    assert is_match_case('async', 'again', ['G', 'W', 'Y', 'Y', 'W']) == True
    assert is_match_case('abccd', 'ccccc', ['Y', 'Y', 'G', 'G', 'Y']) == True
