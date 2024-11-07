def calculate_structure_sum(data):
    total_sum = 0 # инициализация переменной для хранения суммы

    if isinstance(data, (int, float)): # если элемент - число
        return data # возвращаем его

    if isinstance(data, str): # если элемент - строка
        return len(data) # возвращаем длину строки

    if isinstance(data, (list, tuple, set)): # если элемент - список, кортеж или множество
        for item in data: # перебираем каждый элемент
            total_sum += calculate_structure_sum(item) # рекурсивно вызываем функцию и добавляем результат к общей сумме

    if isinstance(data, dict): # если элемент - словарь
        for key, value in data.items(): # перебираем ключи и значения
            total_sum += calculate_structure_sum(key) # добавляем длину ключа или значение, если это число
            total_sum += calculate_structure_sum(value) # добавляем длину значения или само значение, если это число

    return total_sum # возвращаем общую сумму

# Пример использования функции
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure) # вызов функции с заданной структурой данных
print(result) # вывод результата на консоль, ожидается 99
