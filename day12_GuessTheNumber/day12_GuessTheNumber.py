import random, art
print(art.logo)
attempts = 0
def GuessNumber(attempts):
    """Checks if the number guessed by the user matches what the computer chose."""
    attempt = attempts
    num = random.randint(1, 100)
    while attempt > 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess < num:
            print("Too low. \nGuess again.")
            attempt -= 1
        elif guess > num:
            print("Too high. \nGuess again")
            attempt -= 1
        else:
            print(f"You got it! The answer is {num}")
            break
    print("You've run out of guesses. You lose.")


print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty=="easy":
    attempts = 10
else:
    attempts = 5
GuessNumber(attempts)
