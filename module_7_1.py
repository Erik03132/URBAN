def custom_write(file_name, strings): # определяем функцию custom_write с параметрами file_name и strings
    strings_positions = {} # создаем словарь для хранения позиций строк
    with open(file_name, 'w', encoding='utf-8') as file: # открываем файл для записи в режиме 'w' с кодировкой utf-8
        for line_number, string in enumerate(strings, start=1): # перебираем строки с их номерами, начиная с 1
            byte_position = file.tell() # получаем текущую позицию в байтах перед записью строки
            file.write(string + '\n') # записываем строку в файл, добавляя символ новой строки
            strings_positions[(line_number, byte_position)] = string # добавляем данные в словарь: ключ - кортеж (номер строки, позиция), значение - строка
    return strings_positions # возвращаем словарь с позициями строк

# Пример использования функции
info = [ # создаем список строк для записи
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info) # вызываем функцию custom_write и передаем имя файла и список строк

for elem in result.items(): # перебираем элементы словаря
    print(elem) # выводим ключ и значение на консоль
