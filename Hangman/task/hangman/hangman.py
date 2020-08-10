import random


def output_word(word, guessed_letters):
    output_word = '\n'
    for letter in word:
        if letter in guessed_letters:
            output_word += letter
        else:
            output_word += '-'
    return output_word


def hangman():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    random_word = random.choice(word_list)

    random_word_letters = set(random_word)
    input_letters = set()

    print('-' * len(random_word))
    lives = 8
    output = ''

    while lives:
        input_letter = input('Input a letter:')

        if len(input_letter) == 1:
            if input_letter.isascii() and input_letter.islower():
                if input_letter not in input_letters:
                    if input_letter not in random_word_letters:
                        print('No such letter in the word')
                        lives -= 1
                        if not lives:
                            break
                    input_letters.add(input_letter)
                else:
                    print('You already typed this letter')
            else:
                print('It is not an ASCII lowercase letter')
        else:
            print('You should input a single letter')

        output = output_word(random_word, input_letters)
        print(output)

    if output == random_word:
        print('''You guessed the word!
        You survived!''')
    else:
        print('You are hanged!')


print('H A N G M A N\n')
while True:
    player_choice = input('Type "play" to play a game, "exit" to quit:')
    if player_choice == 'play':
        hangman()
        break
    else:
        break
