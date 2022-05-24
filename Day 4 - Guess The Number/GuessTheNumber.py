from random import randint

guessed = False
tries = 8
info = ""

# Ask name
name = input("Tell me your name: ")

# Inform player: Guess the number between 0 and 100 having 8 tries
print(f"Hello {name}, I'm going to choose a number between 0 and 100 (included) and you have 8 tries to guess it. "
      f"Let's start.")

# Choose number
rand_num = randint(0, 11)

while not guessed and tries > 0:
    # Ask number
    user_num = int(input(f"Tries remaining: {tries} Choose a number: "))
    tries -= 1
    # Analyze number
    # Number is out of range
    if user_num < 0 or user_num > 100:
        info = "Wrong number. Must be between 0 and 100 (included)."
    # Number is smaller
    elif user_num < rand_num:
        info = "The number is greater."
    # Number is greater
    elif user_num > rand_num:
        info = "The number is smaller."
    # User has guessed the num. Inform him/her and tell the tries taken
    elif user_num == rand_num:
        info = f"YOU DID IT! {user_num} is the correct number! Congratulations!!"
        guessed = True
    else:
        info = "Unexpected value."

    print(info)

print(f"Thank you for playing, {name}, have a nice day.")