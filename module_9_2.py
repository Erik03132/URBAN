first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable'] # список строк
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler'] # другой список строк

# Создание списка с длинами строк из first_strings, где длина >= 5
first_result = [len(s) for s in first_strings if len(s) >= 5] # списочная сборка с условием на длину строки

# Создание списка пар слов одинаковой длины из двух списков
second_result = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)] # двойной цикл и условие на длину

# Создание словаря строк и их длин (только для строк четной длины)
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0} # словарная сборка с объединением списков и фильтром

print(first_result) # вывод результата первого задания
print(second_result) # вывод результата второго задания
print(third_result) # вывод результата третьего задания
