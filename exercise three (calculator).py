operator = input("*,/,+,-: ")
if operator == '*':
    val1 = int(float(input("Value1: ")))
    val2 = int(float(input("Value2: ")))
    operation = val1*val2
    print(operation)
elif operator == '/':
    val1 = int(float(input("Value1: ")))
    val2 = int(float(input("Value2: ")))
    operation = val1/val2
    print(round(operation, 3))
elif operator == '+':
    val1 = int(float(input("Value1: ")))
    val2 = int(float(input("Value2: ")))
    operation = val1+val2
    print(operation)
elif operator == '-':
    val1 = int(float(input("Value1: ")))
    val2 = int(float(input("Value2: ")))
    operation = val1-val2
    print(operation)
else:
    print("Syntax ERROR")