my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]  # запись исходного списка в переменную my_list
index = 0  # инициализация индекса для доступа к элементам списка

while index < len(my_list):  # цикл продолжается, пока индекс меньше длины списка
    number = my_list[index]  # получение текущего элемента списка

    if number < 0:  # проверка, является ли число отрицательным
        break  # выход из цикла, если число отрицательное

    if number == 0:  # проверка, является ли число нулем
        index += 1  # увеличение индекса на 1, чтобы перейти к следующему элементу
        continue  # пропуск текущей итерации, если число равно нулю

    print(number)  # вывод положительного числа на консоль
    index += 1  # увеличение индекса на 1 для перехода к следующему элементу
