age = int(input("enter your age: "))

#checks if the condition is true
if age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You haven't been born yet")
elif age >= 100:
    print("You are too old to sign up")
else:
    print("You must be 18+ to sign up")

response = input("Would you like food? (Y/N): ")
if response == 'Y':
    print("Have food")
elif response == 'N':
    print("Can't have food")

name = input("Enter your name: ")
if name == "":
    print("No name submitted")
else: 
    print(f"Hello {name}")

for_sale = True
if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")

online = True
if online:
    print("This user is online")
else:
    print("This user is offline")


