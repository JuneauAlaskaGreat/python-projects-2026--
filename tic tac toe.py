import random

# beginning scores of user and computer
user_score = 0
pc_score = 0

# 'rock', 'paper',
#range of availible options for computer to choose from
options = ['rock', 'paper', 'scissors']

#conditional expression for a 3 game round
while user_score < 3 or pc_score < 3:
    user_choice = input("rock, paper, scissors: ")
#computer makes a random choice
    computer_choice = random.choice(options)
    if user_choice == computer_choice:
        print("Tie. User Score, Printer Score: ", user_score, pc_score)
#options for if the user makes a differing choice to  the computer
    elif user_choice == 'rock':
    # rock < paper
        if computer_choice == options[1]:
            pc_score = pc_score + 1
            print("Computer wins. User Score, Printer Score: ", user_score, pc_score)
    # rock > scissors
        elif computer_choice == options[2]:
            user_score = user_score + 1
            print("User wins. User Score, Printer Score: ", user_score, pc_score)
#options for paper choice, pc takes random and matches it up with the user input
    elif user_choice == 'paper':
    # paper > rock
        if computer_choice == options[0]:
            user_score = user_score + 1
            print("Computer wins. User Score, Printer Score: ", user_score, pc_score)
    # paper < scissors
        elif computer_choice == options[2]:
            pc_score = pc_score + 1
            print("User wins. User Score, Printer Score: ", user_score, pc_score)


