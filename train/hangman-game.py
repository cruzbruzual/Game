
---

## **3. Python Code: `hangman.py`**  
This code implements the **Hangman** game, where the player tries to guess a word by entering letters.

```python
import random

# List of words for the game
word_list = ["python", "developer", "computer", "hangman", "github", "programming"]

# Function to get a random word
def get_random_word():
    return random.choice(word_list).lower()

# Function to display the current state of the word
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Main game function
def play_hangman():
    word = get_random_word()
    guessed_letters = set()
    attempts = 6  # Maximum wrong attempts allowed

    print("Welcome to Hangman!")
    print("Try to guess the word letter by letter.")

    while attempts > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Remaining attempts: {attempts}")
        
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        
        guessed_letters.add(guess)

        if guess in word:
            print("✅ Correct!")
            if all(letter in guessed_letters for letter in word):
                print(f"\n🎉 Congratulations! You guessed the word: {word}")
                break
        else:
            attempts -= 1
            print("Incorrect! Try again.")

    if attempts == 0:
        print(f"\n Game Over! The correct word was: {word}")

if __name__ == "__main__":
    play_hangman()
