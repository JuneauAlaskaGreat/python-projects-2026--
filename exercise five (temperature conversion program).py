unit = input("is this temperature in celsius or fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32)
    print(f"The temperature in fahreinheit is: {temp}")
elif unit == "F":
    temp = round((temp - 32) * 5/9)
    print(f"The temperature in celsius is: {temp}")
else:
    print(f"{unit} is an invalid unit of measurement")