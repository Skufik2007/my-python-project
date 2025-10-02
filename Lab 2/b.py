
print("Доступные операции:")
print("+ - сложение")
print("- - вычитание")
print("* - умножение")
print("/ - деление")
print("e - выход")

while True:
    
        op = input("\nВведите операцию (+, -, *, /, e): ")
        
        if op == 'e':
            print("До свидания!")
            break
        
        if op not in ['+', '-', '*', '/']:
            print("Ошибка: неверная операция!")
            continue
        
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        
        if op == '+':
            result = a + b
            print("Результат:", a, "+", b, "=", result)
        
        elif op == '-':
            result = a - b
            print("Результат:", a, "-", b, "=", result)
        
        elif op == '*':
            result = a * b
            print("Результат:", a, "*", b, "=", result)
        
        elif op == '/':
            if b == 0:
                print("Ошибка: деление на ноль!")
            else:
                result = a / b
                print("Результат:", a, "/", b, "=", result)
    

