#1.
import math
degree = int(input("Input degree: "))
num = degree * math.pi / 180
print("Output radian:", round(num, 6))

#2.
import math
height = int(input("Height: "))
base1 = int(input("Base, first value: "))
base2 = int(input("Base, second value: "))
area = (base1 + base2) * height / 2
print("Expected Output:", area)

#3.
import math
n = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
area = (n * length**2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:",round(area))

#4.
import math
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = base * height
print("Expected Output:", area)