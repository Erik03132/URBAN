class StepValueError(ValueError): # создаем пользовательский класс исключения StepValueError, наследуемый от ValueError
    pass # оставляем класс пустым

class Iterator: # создаем класс Iterator
    def __init__(self, start, stop, step=1): # метод инициализации объекта
        if step == 0: # проверяем, равен ли шаг 0
            raise StepValueError('шаг не может быть равен 0') # выбрасываем исключение StepValueError
        self.start = start # устанавливаем начальное значение итерации
        self.stop = stop # устанавливаем конечное значение итерации
        self.step = step # устанавливаем шаг итерации
        self.pointer = start # устанавливаем указатель на начальное значение

    def __iter__(self): # метод для возврата итератора
        self.pointer = self.start # сбрасываем указатель на начальное значение
        return self # возвращаем сам объект

    def __next__(self): # метод для получения следующего значения
        if (self.step > 0 and self.pointer >= self.stop) or (self.step < 0 and self.pointer <= self.stop): # проверяем завершение итерации
            raise StopIteration # выбрасываем исключение StopIteration
        current = self.pointer # сохраняем текущее значение указателя
        self.pointer += self.step # увеличиваем указатель на шаг
        return current # возвращаем текущее значение

try: # блок обработки исключений
    iter1 = Iterator(100, 200, 0) # создаем объект итератора с шагом 0
    for i in iter1: # пытаемся пройтись по итератору
        print(i, end=' ') # выводим элементы итератора
except StepValueError: # ловим исключение StepValueError
    print('Шаг указан неверно') # выводим сообщение об ошибке

iter2 = Iterator(-5, 1) # создаем объект итератора с отрицательным стартом и положительным стопом
iter3 = Iterator(6, 15, 2) # создаем объект итератора с шагом 2
iter4 = Iterator(5, 1, -1) # создаем объект итератора с отрицательным шагом
iter5 = Iterator(10, 1) # создаем объект итератора с положительным стартом и отрицательным стопом

for i in iter2: # проходимся по итератору iter2
    print(i, end=' ') # выводим элементы итератора
print() # переход на новую строку

for i in iter3: # проходимся по итератору iter3
    print(i, end=' ') # выводим элементы итератора
print() # переход на новую строку

for i in iter4: # проходимся по итератору iter4
    print(i, end=' ') # выводим элементы итератора
print() # переход на новую строку

for i in iter5: # проходимся по итератору iter5
    print(i, end=' ') # выводим элементы итератора
print() # переход на новую строку
