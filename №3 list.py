import random

my_list = []

for _ in range(10):
my_list.append(random.randint(1, 100))

x = int(input("Введите число: "))

if x in my_list:
index = my_list.index(x)
print("Номер числа в списке:", index)
else:
print("-1")