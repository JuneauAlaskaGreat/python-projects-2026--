import random

def check_guess(secret_number, guess):
    while guess != secret_number:
        guess = int(input("number: "))
        if guess == secret_number:
            print("you won")
    
secret_number = random.randint(1, 10)
guess = int(input("number: "))
check_guess(secret_number, guess)   
