import math

x = 9

print(math.pi)
print(math.e)

result = math.sqrt(x)
result = math.ceil(x)

print(result)

import math

rad = float(input("enter radius: "))

circ = 2*math.pi*rad
print(circ)

print(f"the circ is {round(circ)}")


area = math.pi*pow(rad, 2)
print(f"area is {round(area)}")

a = float(input("enter side a: "))
b = float(input("enter side b: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C = {c}")
            