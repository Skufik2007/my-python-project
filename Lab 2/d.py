import random
num = random.randint(1, 5)
kolichestvo_popitok = 0
print("Я загадал число от 1 до 5")
while True:
    guess = int(input("Введи число: "))
    kolichestvo_popitok = kolichestvo_popitok + 1
    
    if guess < num:
        print("Слишком мало")
    elif guess > num:
        print("Слишком много")
    else:
        print("Поздравляю! Ты угадал!")
        print("Количество попыток:", kolichestvo_popitok)
        break
