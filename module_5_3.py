class House:
    def __init__(self, name, number_of_floors):
        self.name = name # инициализация имени здания
        self.number_of_floors = number_of_floors # инициализация количества этажей

    def __len__(self):
        return self.number_of_floors # возвращает количество этажей

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}" # возвращает строковое представление объекта

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors # сравнение количества этажей
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors # сравнение количества этажей
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors # сравнение количества этажей
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors # сравнение количества этажей
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors # сравнение количества этажей
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors # сравнение количества этажей
        return False

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value # увеличение количества этажей
        return self

    def __radd__(self, value):
        return self.__add__(value) # вызов __add__

    def __iadd__(self, value):
        return self.__add__(value) # вызов __add__

# Создание объектов класса House
h1 = House('ЖК Эльбрус', 10) # создание объекта h1 с именем "ЖК Эльбрус" и 10 этажами
h2 = House('ЖК Акация', 20) # создание объекта h2 с именем "ЖК Акация" и 20 этажами

print(h1) # вывод на консоль строкового представления объекта h1
print(h2) # вывод на консоль строкового представления объекта h2

print(h1 == h2) # сравнение объектов h1 и h2

h1 = h1 + 10 # увеличение количества этажей объекта h1 на 10
print(h1) # вывод на консоль строкового представления объекта h1
print(h1 == h2) # сравнение объектов h1 и h2

h1 += 10 # увеличение количества этажей объекта h1 на 10
print(h1) # вывод на консоль строкового представления объекта h1

h2 = 10 + h2 # увеличение количества этажей объекта h2 на 10
print(h2) # вывод на консоль строкового представления объекта h2

print(h1 > h2) # сравнение объектов h1 и h2
print(h1 >= h2) # сравнение объектов h1 и h2
print(h1 < h2) # сравнение объектов h1 и h2
print(h1 <= h2) # сравнение объектов h1 и h2
print(h1 != h2) # сравнение объектов h1 и h2
