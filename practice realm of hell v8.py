num = 7
a = 6
b = 7
age = 25
temperature = 48
user_role = "admin"
# X if condition else Y
# print("Positive" if num > 0 else "Negative")
max_num = a if a > b else b
print(max_num)
min_num = a if a < b else b
print(min_num)

status = "Adult" if age >= 18 else "Minor"
print(status)

result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

weather = "Hot" if temperature > 20 else "COLD"
print(weather)

access = "Full access" if user_role == "Admin" else "Limited access"
print(access)