def get_multiplied_digits(number): # объявление функции с параметром number
    str_number = str(number) # преобразование числа в строку и сохранение в переменной str_number
    if len(str_number) > 1: # проверка, что длина строки больше 1
        first = int(str_number[0]) # получение первой цифры и преобразование её в число
        return first * get_multiplied_digits(int(str_number[1:])) # рекурсивный вызов функции без первой цифры
    else:
        return int(str_number) # возврат единственной оставшейся цифры, преобразованной в число

# Пример использования функции
result = get_multiplied_digits(40203) # вызов функции с числом 40203
print(result) # вывод результата на консоль, ожидается 24
