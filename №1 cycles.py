G = int(input("Введи число, которое определит max значение:"))
for i in range(1, G + 1):
    c = i * i
    if c <= G:
        print(c, end=' ')