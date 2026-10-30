import random

# beginning scores of user and computer
user_score = 0
pc_score = 0

# 'rock', 'paper', SPARE OPTIONS OMEGALUL
#range of availible options for computer to choose from
options = ['rock', 'paper', 'scissors']

#conditional expression for a 3 game round
while user_score < 3 and pc_score < 3:
    user_choice = input("rock, paper, scissors: ")
#computer makes a random choice
    computer_choice = random.choice(options)
    if user_choice == computer_choice:
        print("Tie. User Score, Bot Score: ", user_score, pc_score)
#options for if the user makes a differing choice to  the computer, this case is for rock
    elif user_choice == 'rock':
    # rock < paper
        if computer_choice == options[1]:
            pc_score = pc_score + 1
            print("Computer wins. User Score, Bot Score: ", user_score, pc_score)
    # rock > scissors
        elif computer_choice == options[2]:
            user_score = user_score + 1
            print("User wins. User Score, Bot Score: ", user_score, pc_score)
#options for paper choice, pc takes random and matches it up with the user input
    elif user_choice == 'paper':
    # paper > rock
        if computer_choice == options[0]:
            user_score = user_score + 1
            print("User wins. User Score, Bot Score: ", user_score, pc_score)
    # paper < scissors (it's already 20 minutes past 3 what do i do help me)
        elif computer_choice == options[2]:
            pc_score = pc_score + 1
            print("Computer wins. User Score, Bot Score: ", user_score, pc_score)
#options for scissors choice, user inputs scissor and then pc matches it
    elif user_choice == 'scissors':
        # scissors < rock
        if computer_choice == options[0]:
            pc_score = pc_score + 1
            print("Computer wins. User Score, Bot Score: ", user_score, pc_score)
        # scissors > paper (it's already 20 minutes past 3 what do i do help me)
        elif computer_choice == options[1]:
            user_score = user_score + 1
            print("User wins. User Score, Bot Score: ", user_score, pc_score)
#win conditions
#13 minutes until 4 if im spotted on my pc well past my study start time im cooked
if pc_score == 3:
    print("Computer wins.")
elif user_score == 3:
    print("User wins.")
    


