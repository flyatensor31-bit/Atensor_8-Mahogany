import math

#Asks you to input the coordinates.
x1 = float(input("What is x1: "))
y1 = float(input("What is y1: "))
x2 = float(input("What is x2: "))
y2 = float(input("What is y2: "))

#Subtracts the coordinates to create the two points.
Point_1 = x2 - x1
Point_2 = y2 - y1

#Squares the two points and adds them together.
d1 = pow(Point_1,2)
d2 = pow(Point_2,2)

x = (d1 + d2)

#Square roots the sum and finds the distance between the two points.
Distance = math.sqrt(x)

#Prints the distance between the two points.
print("The distance between the two points is:", Distance)

"""
Reflection:
I learned that then Math Library helps with coding by making it a lot easier and simplerby providing shortcuts and explaining each function.
And without functions like "sqrt()" and "pow()", the coding process would become longer and complex, making it take longer.
"""