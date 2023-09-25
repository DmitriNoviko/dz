import math

a = float(input("Введите a = "))
z1 = (math.cos(a) + math.sin(a)) / (math.cos(a) - math.sin(a))
z2 = math.tan(2*a) + (1/math.cos(2*a))
print('z1 =', z1)
print('z2 =', z2)
