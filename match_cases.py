from typing import List


def is_match_case(candidate_word: str, labeled_word: str, case: List[str]) -> bool:
    result = True
    for i, c in enumerate(case):
        if c == '🟩':
            result = result and (labeled_word[i] == candidate_word[i])

        elif c == '⬜':
            result = result and (labeled_word[i] not in candidate_word)

        elif c == '🟨':
            result = result and (
                    labeled_word[i] in labeled_word and labeled_word[i] != candidate_word[i])
        else:
            raise ValueError(f'Unknown charactor {c} len={len(c)}')
        if not result:
            return False
    return True


def filter_words_by_case(possible_words_answer, played_word, case: List[str]) -> List[str]:
    filtered_words = []
    for word in possible_words_answer:
        if is_match_case(candidate_word=word, labeled_word=played_word, case=case):
            filtered_words.append(word)
    return filtered_words


def test_is_match_case():
    assert is_match_case('async', 'again', ['🟩', '⬜', '⬜', '🟨', '⬜']) == True
    assert is_match_case('async', 'again', ['🟩', '⬜', '🟨', '🟨', '⬜']) == True
    assert is_match_case('abccd', 'ccccc', ['🟨', '🟨', '🟩', '🟩', '🟨']) == True
