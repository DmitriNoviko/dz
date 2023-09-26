import random

my_list = []

for _ in range(10):
my_list.append(random.randint(1, 100))

print("Список случайных чисел:", my_list)

duplicates = []

for num in my_list:
if my_list.count(num) > 1 and num not in duplicates:
duplicates.append(num)

if duplicates:
print("Повторяющиеся элементы:", duplicates)
else:
print("Нет повторяющихся элементов в списке.")