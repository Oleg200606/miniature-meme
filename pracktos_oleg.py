import math

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
    choice = int(input("Введите номер операции: "))
    if choice == 0:
        break
    elif choice == 10:
        a = float(input("Введите число: "))
        if a % 180 == 90:
            print("Ошибка(Такого значения нет в таблице)")
        else:
            print(math.tan(a))
    elif choice == 9:
        a = float(input("Введите число: "))
        print(math.cos(a))
    elif choice == 8:
        a = float(input("Введите число: "))
        print(math.sin(a))

    elif choice == 7:
        a = float(input("Введите число: "))
        if a >= 0:
            print(math.factorial(a))
        else:
            print("Ошибка")

    elif choice == 6:
        a = float(input("Введите число: "))
        if a >= 0:
            print(math.sqrt(a))
        else:
            print("Ошибка")

    elif choice == 5:
        a = float(input("Введите число: "))
        b = float(input("Введите степень: "))
        print(math.pow(a, b))

    elif choice == 4:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        if b == 0:
            print("На нуль делить нельзя")
        else:
            print(a/b)

    elif choice == 3:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        print(a*b)

    elif choice == 2:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        print(a-b)

    elif choice == 1:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        print(a+b)
    else:

        break
