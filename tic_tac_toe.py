import random

computer_score = 0 
human_score = 0

def choice_to_number(choice):
    return {'Rock': 1, 'Paper': 2, 'Scissors': 3}[choice]
def number_to_choice(number):
    return {1: 'Rock', 2: 'Paper', 3: 'Scissors'}[number]
def random_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])
    

def choice_result(human_choice, computer_choice):
    global computer_score
    global human_score
    human_number = choice_to_number(human_choice)
    computer_number = choice_to_number(computer_choice)
    if (human_number - computer_number) % 3 == 1:
        computer_score += 1
    elif human_number == computer_number:
        print('Tie')
    else:
        human_score += 1
    if human_score > computer_score:
        print("Human Wins")
    else:
        print("Computer Wins")

user_human_choice = str(input("Enter your choice \n 1. Rock \n 2. Paper \n 3. Scissors \n"))

choice_result(user_human_choice, random_computer_choice())