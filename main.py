import os

# Here's the body 
deadguy = [
    """
  +---+
      |
      |
      |
     ===   
""",


"""
  +---+
  O   |
      |
      |
     ===
""",


"""
  +---+
  O   |
  |   |
      |
     ===
""",


"""
  +---+
  O   |  
 /|   | 
      |
     ===
""",


"""
  +---+
  O   |
 /|\\  |
      |
     ===  
""",


"""
  +---+
  O   |
 /|\\  |
 /    |
     ===
""",


"""
  +---+
  O   |
 /|\\  |
 / \\  |
     ===
"""
]

''' Main things are here intro, logics, and the loop'''
# Are you still reading the code?
def playhangman():
    print("Welcome!")
    word = input("Enter the word: ").upper().strip()

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 50)

    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6




    print("Start Guessing, don't cheat!")


    while incorrect_guesses < max_incorrect:
        print(deadguy[incorrect_guesses])

        displayword = []
        for letter in word:
            if letter in guessed_letters:
                displayword.append(letter)
            else:
                displayword.append("_")






        print(f"Word: {' '.join(displayword)}")
        print(f"Letters guessed: {' '.join(sorted(guessed_letters)) if guessed_letters else 'None' }\n")

        if "_" not in displayword:
            print(f"Good job! You guessed the word: {word}")
            break





        guess = input("Guess letters: ").strip().upper()





        if len(guess) != 1 or not guess.isalpha():
            print("Enter a single letter, fool!")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}', fool!")
            continue



        guessed_letters.add(guess)

        if guess in word:
            print(f"Appreciate it!, '{guess}' is present")
        else:
            print(f"You can't be always right, '{guess}' is absent")
            incorrect_guesses += 1 
        
        
    else:
        print(deadguy[incorrect_guesses])
        print(f"Your guy is hung")
        print("Game over! you loser, the word was:" + f" {word}")

if __name__ == "__main__":
    playhangman() #That's it

                         