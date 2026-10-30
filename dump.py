name = input("Enter your full name: ")
pn = input("phone number: ")

name = name.capitalize()
name = name.upper()
name = name.isdigit()

result = pn.count("-")
pn = pn.replace("-", " ")

print(name)
print(result)
print(pn)