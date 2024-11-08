from math import inf  # Импортируем бесконечность из библиотеки math

def fake_divide(first, second):
    if second == 0:
        return 'Ошибка'  # Возвращаем 'Ошибка', если делим на 0
    return first / second  # Возвращаем результат деления

def true_divide(first, second):
    if second == 0:
        return inf  # Возвращаем бесконечность, если делим на 0
    return first / second  # Возвращаем результат деления

# Тестируем функции
result1 = fake_divide(69, 3)  # Вызываем fake_divide с аргументами 69 и 3
result2 = fake_divide(3, 0)  # Вызываем fake_divide с аргументами 3 и 0
result3 = true_divide(49, 7)  # Вызываем true_divide с аргументами 49 и 7
result4 = true_divide(15, 0)  # Вызываем true_divide с аргументами 15 и 0

# Выводим результаты на консоль
print(result1)  # Ожидаемый вывод: 23.0
print(result2)  # Ожидаемый вывод: Ошибка
print(result3)  # Ожидаемый вывод: 7.0
print(result4)  # Ожидаемый вывод: inf
