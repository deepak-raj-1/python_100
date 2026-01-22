import random
def compare(user, comp, attempts):
    if user == comp:
        return "You guessed the correct number", attempts
    elif user > comp and user != comp:
        attempts -= 1
        return "Your guess is too high", attempts
    elif user < comp and  user != comp:
        attempts -= 1
        return "Your guess is too low", attempts

def difficulty_level(difficulty):
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
lives = 0
lives_remaining = True
computer_guess = random.randint(1, 100)
print(computer_guess)
level = str(input("Select easy or hard:")).lower()
lives = difficulty_level(level)
while lives_remaining:
    print(f"You have {lives} attempts remaining.")
    user_input = int(input("guess the number: "))
    result , lives = compare(user_input, computer_guess,lives)
    print(result)
    if user_input == computer_guess:
        lives_remaining = False
    elif lives == 0:
        print("You ran out of lives")
        lives_remaining = False