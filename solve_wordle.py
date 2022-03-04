from initial_resource import ALL_WORDS, COLOR
from simulator.wordy_simulator import WordySimulator


def validate_feedback(feedback: str) -> bool:
    if len(feedback) != 5:
        return False
    for char in feedback:
        if char not in set(COLOR.keys()):
            return False
    return True


if __name__ == "__main__":
    wordy = WordySimulator(possible_words_answer=ALL_WORDS)

    # init game
    round = 1
    played_words = []
    feedback_cases = []

    print('Hi, I\'m Wordy. I\'m ready to solve Wordle game.')
    print('I will suggest you the word for guessing then please provide me the feedback back.')
    print('Feedback consist of:\n'
          '\t"g" stand for Green that represent to correctness\n'
          '\t"y" stand for Yellow that represent to presenting\n'
          '\t"w" stand for black that represent to absent')
    print('Please provide me the feedback like below example.')
    print('feedback: ywwgg << 🟨⬜⬜🟩🟩')
    print('----------------------------')
    while round <= 6:
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
        print('Congrats! We won 🎉')
    else:
        print('😵‍💫 Sorry, I can\'t solve it within time')
