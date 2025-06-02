import random, hangman_words, hangman_art

stages = hangman_art.stages
word_list = hangman_words.word_list

print(hangman_art.logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print("Word to guess: " + placeholder)

gameover = False
correct = []
lives = 6

while not gameover:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    print(guess)
    if guess in correct:
            print(f"You've already guessed {guess}.")
    display = ""

    for letter in chosen_word:
        if letter==guess:
            display += letter
            correct.append(guess)
        elif letter in correct:
            display += letter
            
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives==0:
            gameover = True
            print(f"IT WAS {chosen_word}!")
            print("******************** YOU LOSE ********************")

    if "_" not in display:
        gameover = True
        print("******************** YOU WIN ********************")
    print(stages[lives])