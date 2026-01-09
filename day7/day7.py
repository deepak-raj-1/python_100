import random

word_list = ["apple", "banana", "grape"]
chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)
dam = "_" * word_length
print(dam)
game_over = False
correct_letters = []
lives = 6
while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    if guess in correct_letters:
        print("You already guessed that!")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        lives -= 1
        print(f"You lose a life. Lives left: {lives}")
        if lives == 0:
            game_over = True
            print("You lose")

    print(display)
    if "_" not in display:
        game_over = True
        print("🎉 You win!")