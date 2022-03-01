from typing import List

from initial_resource import ALL_WORDS
from match_cases import filter_words_by_case, is_match_case
from score_calculator import calculate_gini_by_word
from words_probs_calculation import calculate_words_prob


def calculate_words_should_be_played_score(possible_words_to_play, possible_words_answer):
    words_prob = calculate_words_prob(possible_words_to_play, possible_words_answer, use_thread=False)
    sorted_word_score = calculate_gini_by_word(words_prob)
    return sorted_word_score


possible_words_to_play = ALL_WORDS.copy()
possible_words_answer = ALL_WORDS.copy()

played_word = 'tales'
feedback_case = ['⬜', '⬜', '⬜', '🟩', '⬜']
possible_words_to_play.remove(played_word)
possible_words_answer: List[str] = filter_words_by_case(possible_words_answer=possible_words_answer,
                                                        played_word=played_word,
                                                        case=feedback_case)
word_should_be_played = calculate_words_should_be_played_score(possible_words_to_play, possible_words_answer)

# ----------
played_word = 'doper'
feedback_case = ['⬜', '⬜', '🟩', '🟩', '🟨']
possible_words_to_play.remove(played_word)
possible_words_answer: List[str] = filter_words_by_case(possible_words_answer=possible_words_answer,
                                                        played_word=played_word,
                                                        case=feedback_case)
word_should_be_played = calculate_words_should_be_played_score(possible_words_to_play, possible_words_answer)

# ----------
played_word = 'weeny'
feedback_case = ['⬜', '🟨', '🟨', '⬜', '⬜']
possible_words_to_play.remove(played_word)
possible_words_answer: List[str] = filter_words_by_case(possible_words_answer=possible_words_answer,
                                                        played_word=played_word,
                                                        case=feedback_case)
word_should_be_played = calculate_words_should_be_played_score(possible_words_to_play, possible_words_answer)

# --------
played_word = 'prune'
feedback_case = ['🟨', '🟨', '🟨', '⬜', '🟩']
possible_words_to_play.remove(played_word)
possible_words_answer: List[str] = filter_words_by_case(possible_words_answer=possible_words_answer,
                                                        played_word=played_word,
                                                        case=feedback_case)
word_should_be_played = calculate_words_should_be_played_score(possible_words_to_play, possible_words_answer)
