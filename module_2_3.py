numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]  # заданный список чисел
index = 0  # начальный индекс для цикла

while index < len(numbers):  # цикл продолжается, пока индекс в пределах списка
    number = numbers[index]  # текущий элемент списка

    if number < 0:  # проверка на отрицательное число
        break  # выход из цикла, если число отрицательное

    if number == 0:  # проверка на ноль
        index += 1  # увеличение индекса для перехода к следующему элементу
        continue  # пропуск текущей итерации, если число равно нулю

    print(number)  # вывод положительного числа
    index += 1  # увеличение индекса для перехода к следующему элементу
