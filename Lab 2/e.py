print("Сумма чисел")
n = int(input("Введите количество чисел: "))
numbers = []
for i in range(n):
    num = float(input("Введите число " + str(i+1) + ": "))
    numbers.append(num)
total = 0
for num in numbers:
    total += num
print("Сумма чисел " + str(numbers) + " = " + str(total))
