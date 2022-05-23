text = input("Please, write a text: ")
letters = input("Write 3 letters: ")

# letters to tuple
letters.strip()
letters = list(letters.upper())

# How many times each letter appears in text
print(f'The letters "{letters[0]}" appears {text.upper().count(letters[0])} times,'
      f' "{letters[1]}" appears {text.upper().count(letters[1])} times and'
      f' "{letters[2]}" appears {text.upper().count(letters[2])} times.')

# Count all letters in text
print(f'The text has {len(text.strip())} letters and a length of {len(text)} characters.')

# First and last letter
print(f'The first letter is "{text[0].upper()}" and the last is "{text[-1].upper()}"')

# Reverse text
print("This is the reversed text:")
print(text[::-1])

# "Python" appears in text?
print(('"Python" doesn\'t appears in the text', '"Python" appears in the text.')["python" in text.lower()])
