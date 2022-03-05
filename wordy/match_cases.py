from typing import List, Tuple


def is_match_case(candidate_word: str, labeled_word: str, case: List[str]) -> bool:
    candidate_word = list(candidate_word)
    # check green
    for i in range(len(case)):
        if case[i] == '🟩':
            if labeled_word[i] != candidate_word[i]:
                return False
            else:
                candidate_word[i] = None
    # check yellow
    for i in range(len(case)):
        if case[i] == '🟨':
            if labeled_word[i] in candidate_word:
                idx = candidate_word.index(labeled_word[i])
                if (i != candidate_word.index(labeled_word[i])):
                    candidate_word[idx] = None
                else:
                    return False
            else:
                return False
    for i in range(len(case)):
        if case[i] == '⬜':
            if labeled_word[i] in candidate_word:
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
    assert is_match_case('abccd', 'ccccc', ['⬜', '⬜', '🟩', '🟩', '⬜']) == True
    assert is_match_case('rupee', 'tepee', ['⬜', '⬜', '🟩', '🟩', '🟩']) == True
    assert is_match_case('rupee', 'reeve', ['🟩', '🟨', '⬜', '⬜', '🟩']) == True
    assert is_match_case('there', 'nasty', ['🟨', '⬜', '⬜', '⬜', '⬜']) == False


def test_generate_feedback():
    assert generate_feedback('tales', 'rupee') == ['⬜', '⬜', '⬜', '🟩', '⬜']
    assert generate_feedback('count', 'rupee') == ['⬜', '⬜', '🟨', '⬜', '⬜']
    assert generate_feedback('tepee', 'rupee') == ['⬜', '⬜', '🟩', '🟩', '🟩']
    assert generate_feedback('prune', 'rupee') == ['🟨', '🟨', '🟨', '⬜', '🟩']
    assert generate_feedback('reeve', 'rupee') == ['🟩', '🟨', '⬜', '⬜', '🟩']
