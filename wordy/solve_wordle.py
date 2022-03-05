from wordy.utils import ALL_WORDS, COLOR
from wordy.simulator.wordy_simulator import WordySimulator


def validate_feedback(feedback: str) -> bool:
    if len(feedback) != 5:
        return False
    for char in feedback:
        if char not in set(COLOR.keys()):
            return False
    return True


def console_interaction_solve_wordle():
    wordy = WordySimulator(possible_words_answer=ALL_WORDS)

    # init game
    round = 1
    played_words = []
    feedback_cases = []

    print('Hi, I\'m Wordy. 🤖🙏🏻')
    print(
        'I will suggest you the word for guessing in Wordle game base on feedback in each round.')
    print('Feedback consist of:\n'
          '\t"g" (Green) that represent to correctness\n'
          '\t"y" (Yellow) that represent to presenting\n'
          '\t"w" (White) that represent to absent')
    print('Once you\'ve guessed the word in each round, please provide me the feedback as a sequence of color like an example below.')
    print('feedback: ywwgg << 🟨⬜⬜🟩🟩')
    print('----------------------------')
    while round <= 6:
        print('Calculating the most suitable word... (This process takes long time)')
        word_to_play = wordy.guess(round=round, played_words=played_words, feedback_cases=feedback_cases)
        played_words.append(word_to_play)
        print(f'[Round {round}] Please guess "{word_to_play}"')
        while True:
            feedback = input(f'Feedback: ')
            is_valid = validate_feedback(feedback)
            if is_valid:
                break
            else:
                print('Feedback is incorrect, please provide again such as "wwwyg".')
        if feedback == 'ggggg':
            break
        else:
            transformed_feedback = list(map(lambda c: COLOR[c], feedback))
            feedback_cases.append(transformed_feedback)
            print(''.join(transformed_feedback))
            print()
            round += 1
    if round <= 6:
        print(f'Hoolay!! We won with in round {round} 🎉')
    else:
        print('😵‍💫 Sorry, I can\'t solve it within time')
