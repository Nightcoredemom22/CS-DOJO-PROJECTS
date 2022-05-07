# HEAVEN BARNES
# Hangman Game
# Player makes a guess one letter 
# at a time

import random
word_list = ["simple","football", "kitten","soccer"]
tries = 5
def display_hangman(tries):
    print("you have "+ tries +" left to guess")
def get_word():
        word= word_list[random.randint(1, 4)]
        return word.upper() 

def play():
    word= word_list[random.randint(1, 4)]
    get_word= int(input("Guess the word. "))
    word_length = "-" + len(word)
    guessed_word = False
    guessed_letters = set () # what the user has guessed
    print("Time for a a game of Hangman!")    
    print(display_hangman(tries))
    print("There are " + word_length + " characters in guess")
    print("\n")
    while guessed_word is False and tries > 0:
        guess = int(input("Guess a letter in word:")).upper()
        if len(guess)== 1 and guess.isalpha():
                for guess in guessed_letters:
                    if guess in guessed_letters:
                        print("You alrady enetered that letter", guess)               
        elif guess not in word:
            print(guess, "is not included in the word.")
            tries -= 1
        guessed_letters.append(guess)
    else:
        print("Great job", guess, "is in the word.")
    guessed_letters.append(guess)
    word_as_list =list(word_length)
    indices = [i for i, letter in enumerate(word) if letter == guess]
    for index in indices:
        word_as_list[index] = guess
    word_completed = "".join(word_as_list)
    if "_" not in word_list:
        guessed_word = True
    elif len(guess)== len(guess_letters ) and guess.isalpha():
        if guessed_word:
            print("Congrats, you guessed correctly! You win! ")

    print("Sorry, you ran out of tries. The word was " + word + ". Better luck next time!")
play()