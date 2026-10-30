import random

cash = random.randint(1, 100)

size = input("Size: ")
colour = input("Colour: ")
quantity = input("Quantity: ")

print(f"Available balance: {cash}")
confirmation = input("Proceed to checkout?: ")
if confirmation == 'Yes':
    print("Checking if your cash is enough...")
    if cash > 20:
        print("Order confirmed.")
    elif cash < 20:
        print("Order not completed.")
else:
    print("Confirmation terminated.")

