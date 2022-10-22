from pattern import *
from data import *
import random
score = 0
game_running = True


def random_data():
    return random.choice(data)


def formated_data(account):
    name = account['name']
    description = account['description']
    follower_count = account['follower_count']
    country = account['country']
    return f" {name}, a {description}from {country}"


def check_answer(guess, celeA, celeB):
    if celeA > celeB and guess == 'a' or celeB > celeA and guess == 'b':
        return 1
    else:
        return 0


print(logo)
while game_running:

    compare_A = random_data()
    compare_B = random_data()
    if compare_B == compare_A:
        compare_B = random_data()

    print("Compare A : ", formated_data(compare_A))
    print("Compare B : ", formated_data(compare_B))
    print("Or Enter 'exit' for quiting")
    guess = input("Who has more follower ,Enter 'A' or 'B'!  ").lower()
    print('\n')
    if guess == 'exit':
        game_running = False
    followerA = compare_A['follower_count']
    followerB = compare_B['follower_count']

    answer = check_answer(guess,followerA,followerB)
    if answer:
        score = score + 1
        print(f"Your guess is correct : Your score {score}")
    else:
        print(f"You lose,your guess was incorrect : Your score {score}")
        game_running = False
    print('\n')
    game_continue = input("Do you want to play again ? Enter 'y' for YES and 'N' for NO ").lower()
    if game_continue == 'y':
        game_running = True
    else:
        game_running = False
