num = int(input("Введи число:"))
while num > 0:
    digit = num % 10
    print(digit, end=' ')
    num //= 10