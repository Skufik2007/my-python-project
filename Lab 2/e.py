def sum_recursive(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_recursive(numbers[1:])

print("Рекурсивная сумма чисел")
n = int(input("Введите количество чисел: "))
numbers = []
for i in range(n):
    num = float(input("Введите число " + str(i+1) + ": "))
    numbers.append(num)
result = sum_recursive(numbers)
print("Сумма чисел " + str(numbers) + " = " + str(result))
