import math
div = "---------------"
while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("0. Выход")
    choice = input("Введите номер операции: ")

    if not choice.isdigit():
        print(div)
        print("Ошибка. Введите номер операции (целое число).")
        print(div)
        continue

    choice = int(choice)
    if choice == 0:
        break
    elif choice == 10:
        a = float(input("Введите число: "))
        if a % 180 == 90:
            print(div)
            print("Ошибка(Такого значения нет в таблице)")
            print(div)
        else:
            print(math.tan(a))
    elif choice == 9:
        a = float(input("Введите число: "))
        print(div)
        print(math.cos(a))
        print(div)
    elif choice == 8:
        a = float(input("Введите число: "))
        print(div)
        print(math.sin(a))
        print(div)

    elif choice == 7:
        a = float(input("Введите число: "))
        if a >= 0:
            print(div)
            print(math.factorial(a))
            print(div)
        else:
            print(div)
            print("Ошибка")
            print(div)

    elif choice == 6:
        a = float(input("Введите число: "))
        if a >= 0:
            print(div)
            print(math.sqrt(a))
            print(div)
        else:
            print(div)
            print("Ошибка")
            print(div)

    elif choice == 5:
        a = float(input("Введите число: "))
        b = float(input("Введите степень: "))
        print(div)
        print(math.pow(a, b))
        print(div)

    elif choice == 4:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        if b == 0:
            print(div)
            print("На нуль делить нельзя")
            print(div)
        else:
            print(div)
            print(a/b)
            print(div)

    elif choice == 3:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        print(div)
        print(a*b)
        print(div)

    elif choice == 2:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        print(div)
        print(a-b)
        print(div)

    elif choice == 1:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        print(div)
        print(a+b)
        print(div)
    else:
        break
