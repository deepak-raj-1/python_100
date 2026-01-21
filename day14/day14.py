from game_data import data
import art
import random
def check_answer(account_a, account_b):
    if account_a["follower_count"] > account_b["follower_count"]:
        return "a"
    else:
        return "b"
def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"

score = 0
print(art.logo)
account_a = random.choice(data)
account_b = random.choice(data)
game_should_continue = True
while game_should_continue:
    while account_a == account_b:
        account_b = random.choice(data)
    print(format_data(account_a))
    print(art.vs)
    print(format_data(account_b))
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess == check_answer(account_a, account_b):
        score += 1
        account_a = account_b
        account_b = random.choice(data)
        print(f"score: {score}")
    else:
        print(f"Your final score is {score}")
        game_should_continue = False