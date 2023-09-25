Num = int(input("Введи число:"))
a, b = 0, 1
for _ in range(Num):
    print(a, end=' ')
    c = a + b
    a = b
    b = c