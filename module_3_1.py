calls = 0 # Создаем переменную для подсчета вызовов функций

def count_calls(): # Определяем функцию для увеличения счетчика вызовов
    global calls # Указываем, что будем использовать глобальную переменную calls
    calls += 1 # Увеличиваем значение переменной calls на 1

def string_info(string): # Определяем функцию для обработки строки
    count_calls() # Увеличиваем счетчик вызовов
    return (len(string), string.upper(), string.lower()) # Возвращаем кортеж с длиной строки, строкой в верхнем и нижнем регистрах

def is_contains(string, list_to_search): # Определяем функцию для проверки наличия строки в списке
    count_calls() # Увеличиваем счетчик вызовов
    return string.lower() in [item.lower() for item in list_to_search] # Возвращаем True, если строка присутствует в списке, игнорируя регистр

print(calls) # Выводим количество вызовов функций на консоль

print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)
