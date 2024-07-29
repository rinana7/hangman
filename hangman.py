import random
import string

from words import words


def get_valid_word(words):
    word = random.choice(words)

    # randomly chooses something from the list
    while True:
        if "-" in word or " " in word:
            word = random.choice(words)
            continue
        break

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 10

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ''.join(['a', 'b', 'cd']) --> 'a b cd'

        print(
            "Yor have",
            lives,
            "lives left and you have used these letters:",
            "".join(used_letters),
        )
        # what currend word is (ie W - R D)

        word_list = []
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append("-")

        # word_list = [letter if letter in used_letters else '-' for letter in word]

        print("Current word: ", "".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1  # takes away a life if wrong
                print("Letter is not in word.")

        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
        else:
            print("Invalid character. Please try again")

    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print("You guessed the word", word, "!!")


hangman()
