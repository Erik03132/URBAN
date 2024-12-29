def all_variants(text): # определяем функцию-генератор all_variants
    length = len(text) # вычисляем длину строки
    for start in range(length): # перебираем начальные индексы подпоследовательностей
        for end in range(start + 1, length + 1): # перебираем конечные индексы подпоследовательностей
            yield text[start:end] # возвращаем подпоследовательность от start до end

# Вызов функции-генератора и выполнение итераций
a = all_variants("abc") # создаем объект-генератор для строки "abc"

for i in a: # проходимся по объекту-генератору
    print(i) # выводим каждую подпоследовательность