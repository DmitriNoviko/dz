n = int(input("Введите количество чисел: "))

numbers = []
for i in range(n):
number = int(input("Введите число: "))
numbers.append(number)

print("Исходный список:", numbers)

numbers = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]

print("Список после удаления элементов по нечетным индексам:", numbers)