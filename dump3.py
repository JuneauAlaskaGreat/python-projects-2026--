num = 5
a = 6
b = 7 
age = 56
temperature = 30
user_role = "guest"

max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age > 18 else "Child"
weather = "Hot" if temperature > 20 else "COLD"
access_level = "Full access" if user_role == "admin" else "Limited Acess"

print(access_level)