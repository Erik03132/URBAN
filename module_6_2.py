class Vehicle: # создание класса Vehicle
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white'] # атрибут класса - список допустимых цветов

    def __init__(self, owner, model, color, engine_power): # инициализация объекта Vehicle
        self.owner = owner # владелец транспорта
        self.__model = model # скрытый атрибут модели транспорта
        self.__color = color # скрытый атрибут цвета транспорта
        self.__engine_power = engine_power # скрытый атрибут мощности двигателя

    def get_model(self): # метод для получения модели транспорта
        return f"Модель: {self.__model}" # возвращает строку с названием модели

    def get_horsepower(self): # метод для получения мощности двигателя
        return f"Мощность двигателя: {self.__engine_power}" # возвращает строку с мощностью двигателя

    def get_color(self): # метод для получения цвета транспорта
        return f"Цвет: {self.__color}" # возвращает строку с цветом транспорта

    def print_info(self): # метод для вывода информации о транспорте на консоль
        print(self.get_model()) # вывод модели
        print(self.get_horsepower()) # вывод мощности двигателя
        print(self.get_color()) # вывод цвета
        print(f"Владелец: {self.owner}") # вывод владельца

    def set_color(self, new_color): # метод для изменения цвета транспорта
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]: # проверка, есть ли новый цвет в списке допустимых
            self.__color = new_color # установка нового цвета
        else:
            print(f"Нельзя сменить цвет на {new_color}") # вывод сообщения о невозможности сменить цвет


class Sedan(Vehicle): # создание класса Sedan, наследующего Vehicle
    __PASSENGERS_LIMIT = 5 # атрибут класса - ограничение на количество пассажиров

    def __init__(self, owner, model, color, engine_power): # инициализация объекта Sedan
        super().__init__(owner, model, color, engine_power) # вызов конструктора родительского класса


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500) # создание объекта класса Sedan

# Изначальные свойства
vehicle1.print_info() # вывод информации об объекте

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink') # попытка сменить цвет на недопустимый
vehicle1.set_color('BLACK') # смена цвета на допустимый
vehicle1.owner = 'Vasyok' # смена владельца объекта

# Проверяем что поменялось
vehicle1.print_info() # вывод обновленной информации об объекте
