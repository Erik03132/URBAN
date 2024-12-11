class IncorrectVinNumber(Exception):  # Создаем класс исключения для некорректного VIN номера
    def __init__(self, message):
        self.message = message  # Устанавливаем сообщение исключения


class IncorrectCarNumbers(Exception):  # Создаем класс исключения для некорректных номеров автомобиля
    def __init__(self, message):
        self.message = message  # Устанавливаем сообщение исключения


class Car:  # Создаем основной класс Car
    def __init__(self, model, vin, numbers):
        self.model = model  # Устанавливаем атрибут model
        if self.__is_valid_vin(vin):  # Проверяем VIN через метод __is_valid_vin
            self.__vin = vin  # Устанавливаем приватный атрибут __vin
        if self.__is_valid_numbers(numbers):  # Проверяем номера через метод __is_valid_numbers
            self.__numbers = numbers  # Устанавливаем приватный атрибут __numbers

    def __is_valid_vin(self, vin_number):  # Приватный метод проверки корректности VIN
        if not isinstance(vin_number, int):  # Проверяем, является ли VIN числом
            raise IncorrectVinNumber('Некорректный тип vin номер')  # Выбрасываем исключение, если тип неверный
        if not (1000000 <= vin_number <= 9999999):  # Проверяем диапазон VIN
            raise IncorrectVinNumber('Неверный диапазон для vin номера')  # Выбрасываем исключение, если диапазон неверный
        return True  # Возвращаем True, если VIN корректный

    def __is_valid_numbers(self, numbers):  # Приватный метод проверки корректности номеров
        if not isinstance(numbers, str):  # Проверяем, является ли номер строкой
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')  # Выбрасываем исключение, если тип неверный
        if len(numbers) != 6:  # Проверяем длину номера
            raise IncorrectCarNumbers('Неверная длина номера')  # Выбрасываем исключение, если длина неверная
        return True  # Возвращаем True, если номер корректный


# Пример выполнения программы
try:
    first = Car('Model1', 1000000, 'f123dj')  # Создаем объект с корректными данными
except IncorrectVinNumber as exc:
    print(exc.message)  # Выводим сообщение об ошибке VIN
except IncorrectCarNumbers as exc:
    print(exc.message)  # Выводим сообщение об ошибке номеров
else:
    print(f'{first.model} успешно создан')  # Сообщаем об успешном создании объекта

try:
    second = Car('Model2', 300, 'т001тр')  # Создаем объект с некорректным VIN
except IncorrectVinNumber as exc:
    print(exc.message)  # Выводим сообщение об ошибке VIN
except IncorrectCarNumbers as exc:
    print(exc.message)  # Выводим сообщение об ошибке номеров
else:
    print(f'{second.model} успешно создан')  # Сообщаем об успешном создании объекта

try:
    third = Car('Model3', 2020202, 'нет номера')  # Создаем объект с некорректным номером
except IncorrectVinNumber as exc:
    print(exc.message)  # Выводим сообщение об ошибке VIN
except IncorrectCarNumbers as exc:
    print(exc.message)  # Выводим сообщение об ошибке номеров
else:
    print(f'{third.model} успешно создан')  # Сообщаем об успешном создании объекта
