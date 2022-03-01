from typing import List, Tuple


def is_match_case(candidate_word: str, labeled_word: str, case: List[str]) -> bool:
    result = True
    for i, c in enumerate(case):
        target_char = labeled_word[i]
        if c == '🟩':
            result = result and (target_char == candidate_word[i])

        elif c == '⬜':
            sub_result = True
            for j in range(len(candidate_word)):
                if candidate_word[j] == target_char:
                    if case[j] != '🟩':
                        sub_result = False
                        break
            result = result and sub_result
        elif c == '🟨':
            result = result and (
                    target_char in labeled_word and target_char != candidate_word[i])
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


def generate_feedback(played_word: str, answer_word: str):
    feedback: List[Tuple[int, str]] = []
    checked_indices = []
    answer_word = list(answer_word)
    # give Green feedback
    for i in range(len(played_word)):
        target_char = played_word[i]
        if target_char == answer_word[i]:
            feedback.append((i, '🟩'))
            checked_indices.append(i)
            answer_word[i] = None

    for i in range(len(played_word)):
        if i in checked_indices:
            continue
        target_char = played_word[i]
        label = '⬜'
        for j in range(len(answer_word)):
            if target_char == answer_word[j]:
                label = '🟨'
                answer_word[j] = None
                break
        feedback.append((i, label))
    return [x[1] for x in sorted(feedback, key=lambda x: x[0])]


def test_is_match_case():
    assert is_match_case('again', 'async', ['🟩', '⬜', '⬜', '🟨', '⬜']) == True
    assert is_match_case('again', 'async', ['🟩', '⬜', '🟨', '🟨', '⬜']) == True
    assert is_match_case('abccd', 'ccccc', ['🟨', '🟨', '🟩', '🟩', '🟨']) == True
    assert is_match_case('rupee', 'tepee', ['⬜', '⬜', '🟩', '🟩', '🟩']) == True


def test_generate_feedback():
    assert generate_feedback('tales', 'rupee') == ['⬜', '⬜', '⬜', '🟩', '⬜']
    assert generate_feedback('count', 'rupee') == ['⬜', '⬜', '🟨', '⬜', '⬜']
    assert generate_feedback('tepee', 'rupee') == ['⬜', '⬜', '🟩', '🟩', '🟩']
    assert generate_feedback('prune', 'rupee') == ['🟨', '🟨', '🟨', '⬜', '🟩']
