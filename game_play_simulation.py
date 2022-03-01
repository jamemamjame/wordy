from constant import GameStatus
from initial_resource import ALL_WORDS
from simulator.wordle_simulator import WordleSimulator
from simulator.wordy_simulator import WordySimulator


def simulate_game(answer_word: str):
    wordle = WordleSimulator(answer_word=answer_word)
    wordy = WordySimulator(possible_words_answer=ALL_WORDS)

    # initial game state
    game_status = GameStatus.ON_GOING
    round = 1
    played_words = []
    feedback_cases = []
    while game_status == GameStatus.ON_GOING:
        word_to_play = wordy.guess(round=round, played_words=played_words, feedback_cases=feedback_cases)
        game_status, feedback = wordle.get_game_state(played_word=word_to_play)
        played_words.append(word_to_play)
        feedback_cases.append(feedback)
        print(f'({round}) play:\t\t{word_to_play}')
        print(f'feedback:\t{"".join(feedback)}')
        print()
        round += 1

    if game_status == GameStatus.WIN:
        print(f'🎉 I found "{word_to_play.upper()}" within round {round - 1}!')
    else:
        print("☠️ I'm unable to catch that word in time :(")


vocabs = ['those', 'moist', 'shard', 'pleat', 'aloft', 'skill', 'elder', 'frame', 'humor', 'pause', 'ulcer', 'ultra',
          'robin', 'cynic', 'aroma', 'caulk', 'shake', 'dodge', 'swill', 'tacit', 'other', 'thorn', 'trove', 'bloke',
          'vivid', 'spill', 'chant', 'choke']
for vocab in vocabs:
    print(f'======= Vocab is "{vocab.upper()}" =======')
    simulate_game(vocab)
