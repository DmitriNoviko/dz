num = int(input("Введи число:"))
eng = 0
while num > 0:
    b = num % 10
    if b % 2 == 0:
        eng += b
    num //= 10
print(eng)