from constant import GameStatus
from initial_resource import ALL_WORDS
from simulator.wordle_simulator import WordleSimulator
from simulator.wordy_simulator import WordySimulator

wordle = WordleSimulator(answer_word='rupee')
wordy = WordySimulator(possible_words_answer=ALL_WORDS[3500:3600])

# initial game state
game_status = GameStatus.ON_GOING
round = 1
played_words = []
feedback_cases = []
while game_status == GameStatus.ON_GOING:
    word_to_play = wordy.guess(round=round, played_words=played_words, feedback_cases=feedback_cases)
    game_status, feedback = wordle.get_game_state(played_word=word_to_play)
    round += 1
    played_words.append(word_to_play)
    feedback_cases.append(feedback)
    print(f'play:\t\t{word_to_play}')
    print(f'feedback:\t{"".join(feedback)}')
    print()
