from random import choice
from string import ascii_lowercase


def game():
    print("H A N G M A N")
    tries = 0
    secret_word = choice(["python", "java", "kotlin", "javascript"])
    hidden_word = ['-' for i in range(len(secret_word))]
    guessed_letter = set()
    print("")
    print("".join(hidden_word))
    while True:
        letter = input("Input a letter:")
        if len(letter) == 1:
            if letter in ascii_lowercase:
                if letter not in guessed_letter:
                    if letter in secret_word:
                        for i in range(len(secret_word)):
                            if letter == secret_word[i]:
                                hidden_word[i] = letter
                    else:
                        print("No such letter in the word")
                        tries += 1
                else:
                    print("You already typed this letter")
                guessed_letter.add(letter)
            else:
                print("It is not an ASCII lowercase letter")
        else:
            print("You should print a single letter")

        if tries == 8:
            print("You are hanged!")
            break
        elif "-" not in hidden_word:
            print("You guessed the word!")
            print("You survived!")
            break
        print("")
        print("".join(hidden_word))


while True:
    state = input('Print Type "play" to play the game, "exit" to quit: ')
    if state == "play":
        game()
    elif state == "exit":
        break
