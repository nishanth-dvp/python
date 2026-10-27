import random
print("=====Welcome to Hangman game======")
name = input("Enter your name: ")
print("good luck ! ", name)
word = ["python", "network", "computer", "programming", "keyboard"]
word = random.choice(word)
print("the words are computer based")
print("Guess the word in less than 6 attempts")
print("The word has", len(word), "characters")
print("Guess the characters")
print("please enter only one letter")
guesses = ''
turns = 6
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    if failed == 0:
        print("\n===You won===")
        break
    guess = input("\nGuess a character: ")
    if len(guess) < 2:
        guesses += guess
        if guess not in word:
            turns -= 1
            print("You guessed Wrong")
            print("You have", turns, 'more guesses')
            if turns == 0:
                print("==You Loose==")
                print("The word was:", word)
    else:
        print("please enter only one letter")
           