first = ['Strings', 'Student', 'Computers'] # первый список строк
second = ['Строка', 'Урбан', 'Компьютер'] # второй список строк

# Генераторная сборка для вычисления разницы длин строк, если их длины не равны (с использованием zip)
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s)) # генераторная сборка с zip и условием

# Генераторная сборка для сравнения длин строк в одинаковых позициях (с использованием range и len)
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second)))) # генераторная сборка без zip

print(list(first_result)) # вывод списка из генераторной сборки first_result
print(list(second_result)) # вывод списка из генераторной сборки second_result
