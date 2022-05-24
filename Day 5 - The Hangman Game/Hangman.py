from random import choice, shuffle
import string

LIFES = 8
INITIAL_WORDS = ["BACON", "OCTOPUS", "THREE", "SUN", "TRIPOFOBIA", "SPOON", "PIECE"]


def start_game(words, lifes):
    letters = ""
    shuffle_words(words)
    word = select_word(words)
    print(is_finished("copa", "paco"))

    while not is_finished(letters, word) and not is_dead(lifes):
        show_lifes(lifes)
        print()
        show_word(word, letters)

        letter = ask_letter()
        print()
        if not check_letter(letter, word) or letter in letters:
            lifes = substract_life(lifes)
            print(f"Ups, the letter is not in the word or is already said.")
        else:
            print(f"The letter {letter} is correct.")
        letters = add_letter(letter, letters)

    print("The word was: " + word)

    if not is_dead(lifes) and is_finished(letters, word):
        print("YOU WON!")
    else:
        print("You are dead.")

    print("Thank you for playing.")


def shuffle_words(words):
    shuffle(words)


def select_word(words):
    return choice(words)


def show_word(word, letters):
    current_state = ""
    for letter in word:
        if letter in letters:
            current_state += letter
        else:
            current_state += "_"
    print(current_state)


def ask_letter():
    while True:
        letter = input("Please, introduce a letter --> ")
        if letter.upper() in string.ascii_uppercase:
            break

    return letter


def check_letter(letter, word):
    return letter.upper() in word.upper()


def is_finished(letters, word):
    finished = True
    for word_letter in word:
        if word_letter not in letters:
            finished = False
            break
    return finished


def add_letter(letter, letters):
    if letter not in letters:
        letters += letter.upper()
    return letters


def substract_life(life):
    life -= 1
    return life


def show_lifes(life):
    print(f"Lifes remaining: {life}")


def is_dead(life):
    return life <= 0


### START ###
start_game(INITIAL_WORDS, LIFES)
