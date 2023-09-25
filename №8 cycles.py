num = int(input("Введи число:"))
b = 0
d = 1
while num > 0:
    db = num % 10
    b += db
    d *= db
    num //= 10
print("Сумма:", b)
print("Произведение:", d)