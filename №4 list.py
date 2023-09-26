import random

my_list = []

for _ in range(10):
my_list.append(random.randint(1, 100))

print("Список случайных чисел:", my_list)

sum_of_elements = sum(my_list)
product_of_elements = 1

for num in my_list:
product_of_elements *= num

print("Сумма элементов списка:", sum_of_elements)
print("Произведение элементов списка:", product_of_elements)
