class House:
    houses_history = [] # атрибут класса для хранения истории зданий

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls) # создание нового экземпляра класса
        cls.houses_history.append(args[0]) # добавление названия здания в историю
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name # инициализация имени здания
        self.number_of_floors = number_of_floors # инициализация количества этажей

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}" # возвращает строковое представление объекта

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории") # вывод сообщения при удалении объекта

# Создание объектов класса House
h1 = House('ЖК Эльбрус', 10) # создание объекта h1 с именем "ЖК Эльбрус" и 10 этажами
print(House.houses_history) # вывод на консоль истории зданий

h2 = House('ЖК Акация', 20) # создание объекта h2 с именем "ЖК Акация" и 20 этажами
print(House.houses_history) # вывод на консоль истории зданий

h3 = House('ЖК Матрёшки', 20) # создание объекта h3 с именем "ЖК Матрёшки" и 20 этажами
print(House.houses_history) # вывод на консоль истории зданий

# Удаление объектов
del h2 # удаление объекта h2
del h3 # удаление объекта h3

print(House.houses_history) # вывод на консоль истории зданий
