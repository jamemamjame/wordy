from typing import List


def is_match_case(next_guess_word: str, possible_answer_word: str, case: List[str]) -> bool:
    result = True
    for i, c in enumerate(case):
        if c == '🟩':
            result = result and (next_guess_word[i] == possible_answer_word[i])

        elif c == '⬜':
            result = result and (next_guess_word[i] not in possible_answer_word)

        elif c == '🟨':
            result = result and (
                    next_guess_word[i] in next_guess_word and next_guess_word[i] != possible_answer_word[i])
        else:
            raise ValueError(f'Unknown charactor {c} len={len(c)}')
        if not result:
            return False
    return True


def filter_words_by_case(remaining_words, played_word, case: List[str]) -> List[str]:
    filtered_words = []
    for word in remaining_words:
        if is_match_case(word, played_word, case):
            filtered_words.append(word)
    return filtered_words


def test_is_match_case():
    assert is_match_case('async', 'again', ['🟩', '⬜', '⬜', '🟨', '⬜']) == True
    assert is_match_case('async', 'again', ['🟩', '⬜', '🟨', '🟨', '⬜']) == True
    assert is_match_case('abccd', 'ccccc', ['🟨', '🟨', '🟩', '🟩', '🟨']) == True
