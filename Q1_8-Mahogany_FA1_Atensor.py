import math

#
x1 = float(input("What is x1: "))
y1 = float(input("What is y1: "))
x2 = float(input("What is x2: "))
y2 = float(input("What is y2: "))

x3 = x2 - x1
y3 = y2 - y1

d1 = pow(x3,2)
d2 = pow(y3,2)

x = (d1 + d2)

y = math.sqrt(x)

print("The distance between the two points is:", y)

"""
Reflection:
I learned that then Math Library helps with coding by making it a lot easier and simplerby providing shortcuts and explaining each function.
And without functions like "sqrt()" and "pow()", the coding process would become longer and complex, making it take longer.
"""