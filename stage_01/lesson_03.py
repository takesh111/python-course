import math
from decimal import Decimal
# Задание 1
print(7/2, type(7/2))
#3.5 float
print(10 / 5, type(10 / 5))
#2 float
print(7 // 2, type(7 // 2))
#3 int
print(-7 // 2, type(-7 // 2 ))
#-4 int
print(7 % 3, type(7 % 3))
#1 int
print(-7 % 3, type (-7 % 3 ))
#-1 int
print(2**10, type(2**10))
#1024 int

# Задание 2
print(0.1 + 0.2,type(0.1+0.2))
#0.30000000000000004, float
print(0.1 + 0.2 == 0.3, type(0.1 + 0.2 == 0.3))
#False
print(math.isclose(0.1 + 0.2, 0.3))
#True , float
print(f"{0.1 + 0.2:.20f}")
#0.30000000000000004441 , float

# Задание 3
print(round(0.5),round(1.5), round(2.5),round(3.5))
#0 , 2, 2 , 4
print(round(2.675, 2))
#2.67
print(True + True,isinstance(True, int))
#2,true
print(int(3.9), int(-3.9))
print("-----------------")
#3 , -3 int берет только целую часть числа 

# Задача 4 

print(float(0.1+ 0.1+ 0.1))
print(float(0.1+ 0.1+ 0.1 == 0.3)) and print(f"{0.1 + 0.1 + 0.1:.20f}")
print(Decimal(0.1 + 0.1 + 0.1 )== Decimal(0.3))
#Выбрал бы этот способ так как Decimal позволяет вычислить точную десятичную арифметику
print(int((0.1 + 0.1 + 0.1)/100))