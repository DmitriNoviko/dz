import random

my_list = []

for _ in range(10):
my_list.append(random.randint(1, 100))

print("Список случайных чисел:", my_list)

max_element = max(my_list)

print("Наибольший элемент списка:", max_element)
