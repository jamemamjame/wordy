from typing import List, Tuple

from constant import GameStatus
from match_cases import generate_feedback


class WordleSimulator:
    MAX_GUESS_COUNT = 6

    def __init__(self, answer_word: str):
        self.answer_word = answer_word
        self.guess_count = 0

    def get_game_state(self, played_word: str) -> (GameStatus, List[str]):
        feedback = self.__generate_feedback(played_word)
        self.guess_count += 1
        game_status = self.__generate_game_status(feedback)
        return game_status, feedback

    def __generate_game_status(self, feedback):
        if self.__is_correct(feedback):
            game_status = GameStatus.WIN
        else:
            if self.guess_count >= self.MAX_GUESS_COUNT:
                game_status = GameStatus.GAME_OVER
            else:
                game_status = GameStatus.ON_GOING
        return game_status

    def __is_correct(self, feedback: List[str]):
        return feedback == ['🟩', '🟩', '🟩', '🟩', '🟩']

    def __generate_feedback(self, played_word: str):
        return generate_feedback(played_word, self.answer_word)
