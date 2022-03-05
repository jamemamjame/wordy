import pickle

from typing import List

from wordy.match_cases import filter_words_by_case
from wordy.score_calculator import calculate_gini_by_word
from wordy.utils import PATH_WORDS_PROB
from wordy.words_probs_calculator import calculate_words_prob


class WordySimulator:
    def __init__(self, possible_words_answer: List[str]):
        self.possible_words_answer: List[str] = possible_words_answer.copy()
        self.possible_words_to_play: List[str] = possible_words_answer.copy()

    def guess(self, round: int, played_words: List[str] = None, feedback_cases: List[str] = None):
        if round == 1:
            sorted_word_score = self.__guess_first_round()
        else:
            played_word = played_words[-1]
            feedback_case = feedback_cases[-1]
            sorted_word_score = self.__guess_during_game(played_word, feedback_case)
        word_should_be_played = self.get_final_word_should_be_played(sorted_word_score, played_words)
        return word_should_be_played

    def get_final_word_should_be_played(self, sorted_word_score, played_words: List[str]):
        if len(self.possible_words_answer) <= 2:
            return self.possible_words_answer[0]
        for word, score in sorted_word_score.items():
            if word not in played_words and score != 1.0:
                return word

    def __guess_first_round(self):
        with open(PATH_WORDS_PROB, 'rb') as f:
            words_prob = pickle.load(f)
        sorted_word_score = self.calculate_words_should_be_played_score(words_prob)
        return sorted_word_score

    def __guess_during_game(self, last_played_word: str, last_feedback_case: str):
        self.update_possible_words_answer(last_played_word, last_feedback_case)
        sorted_word_score = self.calculate_words_should_be_played_score()
        return sorted_word_score

    def update_possible_words_answer(self, played_word, feedback_case):
        self.possible_words_answer = filter_words_by_case(possible_words_answer=self.possible_words_answer,
                                                          played_word=played_word,
                                                          case=feedback_case)

    def calculate_words_should_be_played_score(self, words_prob=None):
        if not words_prob:
            words_prob = calculate_words_prob(self.possible_words_to_play, self.possible_words_answer, use_thread=False)
        sorted_word_score = calculate_gini_by_word(words_prob)
        return sorted_word_score
