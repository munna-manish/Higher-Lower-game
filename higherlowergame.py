from data import data
import random

def ans_value(item):
    name = item['name']
    description = item["type"]
    nation = item["nation"]
    return f"{name}, a {description}, {nation}"

def searches_only(item):
    #Only deals with the searches of the item
    searches = item['searches']
    return searches

game_should_continue = True
score = 0

def user_guess():
    #checks for the user guess with the answer
    guess = input("Compare 'A' and 'B', guess which got more no.of searches this month: (Type A or B): ").lower()
    if searches_1>searches_2:
        if guess == 'a':
            return True
    elif searches_2>searches_1:
        if guess == 'b':
            return True
    else:
        return False

item_2 = random.choice(data)

while game_should_continue:
    item_1 = item_2
    item_2 = random.choice(data)

    if item_1 == item_2:
        item_2 = random.choice(data)

    print("A = ",ans_value(item_1))
    print("B = ",ans_value(item_2))
    searches_1 = searches_only(item_1)
    searches_2 = searches_only(item_2)
    correct_answer = user_guess()
    if correct_answer:
        score += 1
        print("Yup! That's correct\n")
        print(f"Your current score: {score}")
        print("\n"*2)
    else:
        print("Oops! That's incorrect!")
        print(f"\nYour Final score: {score}")
        game_should_continue = False
        print("\n" * 2)








