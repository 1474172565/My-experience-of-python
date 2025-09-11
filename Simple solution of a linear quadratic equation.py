import math
a = float(input("please board the coefficiant of quadratic term \t"))
b = float(input("please board the coefficiant of Linear term \t"))
c = float(input("please board the constant \t"))
delta = (b ** 2) - 4*a*c
print(f"root1 \t{((-b)+math.sqrt(delta))/2*a}") 
print(f"root2 \t{((-b)-math.sqrt(delta))/2*a}") 