def personal_sum(numbers):  # объявление функции, которая принимает коллекцию numbers
    result = 0  # переменная для хранения суммы чисел
    incorrect_data = 0  # счётчик некорректных данных
    for item in numbers:  # перебор каждого элемента в коллекции
        try:
            result += item  # попытка добавить элемент к сумме
        except TypeError:  # обработка исключения, если элемент не числовой
            incorrect_data += 1  # увеличиваем счётчик некорректных данных
    return result, incorrect_data  # возвращаем кортеж из суммы и количества некорректных данных

def calculate_average(numbers):  # объявление функции для вычисления среднего арифметического
    try:
        result, incorrect_data = personal_sum(numbers)  # вызов функции personal_sum
        return result / (len(numbers) - incorrect_data)  # возвращаем среднее арифметическое
    except ZeroDivisionError:  # обработка исключения деления на ноль
        return 0  # возвращаем 0, если деление на 0
    except TypeError:  # обработка исключения, если передан некорректный тип данных
        print('В numbers записан некорректный тип данных')  # вывод сообщения об ошибке
        return None  # возвращаем None

# Примеры вызовов функций
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать

