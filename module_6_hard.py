class Figure:
    sides_count = 0  # количество сторон, по умолчанию 0

    def __init__(self, color, *sides):  # конструктор класса
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]  # проверка цвета
        self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count  # проверка сторон
        self.filled = False  # публичный атрибут, закрашена ли фигура

    def __is_valid_color(self, r, g, b):  # проверка корректности цвета
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))  # проверка диапазона

    def set_color(self, r, g, b):  # установка нового цвета
        if self.__is_valid_color(r, g, b):  # проверка корректности цвета
            self.__color = [r, g, b]  # обновление цвета

    def get_color(self):  # получение текущего цвета
        return self.__color  # возвращаем цвет

    def __is_valid_sides(self, *sides):  # проверка сторон
        return len(sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in sides)  # валидация

    def set_sides(self, *new_sides):  # установка новых сторон
        if self.__is_valid_sides(*new_sides):  # проверка корректности сторон
            self.__sides = list(new_sides)  # обновление сторон

    def get_sides(self):  # получение текущих сторон
        return self.__sides  # возвращаем стороны

    def __len__(self):  # вычисление периметра
        return sum(self.__sides)  # возвращаем сумму всех сторон


class Circle(Figure):
    sides_count = 1  # у круга одна сторона (длина окружности)

    def __init__(self, color, *sides):  # конструктор класса
        super().__init__(color, *sides)  # вызов конструктора родительского класса
        self.__radius = self.get_sides()[0] / (2 * 3.14159)  # вычисляем радиус

    def get_square(self):  # вычисление площади круга
        return 3.14159 * (self.__radius ** 2)  # площадь круга через радиус


class Triangle(Figure):
    sides_count = 3  # у треугольника три стороны

    def get_square(self):  # вычисление площади треугольника
        a, b, c = self.get_sides()  # получаем стороны
        s = (a + b + c) / 2  # полупериметр
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5  # формула Герона


class Cube(Figure):
    sides_count = 12  # у куба 12 рёбер

    def __init__(self, color, *sides):  # конструктор класса
        super().__init__(color, *([sides[0]] * self.sides_count if len(sides) == 1 else sides))  # проверка сторон

    def get_volume(self):  # вычисление объёма куба
        edge = self.get_sides()[0]  # длина одной стороны
        return edge ** 3  # объём куба


# Проверка работы классов:
circle1 = Circle((200, 200, 100), 10)  # создаём круг
cube1 = Cube((222, 35, 130), 6)  # создаём куб

# Проверка изменения цветов
circle1.set_color(55, 66, 77)  # изменяем цвет круга
print(circle1.get_color())  # выводим новый цвет круга
cube1.set_color(300, 70, 15)  # пытаемся установить некорректный цвет куба
print(cube1.get_color())  # цвет куба не изменится

# Проверка изменения сторон
cube1.set_sides(5, 3, 12, 4, 5)  # пытаемся изменить стороны куба
print(cube1.get_sides())  # стороны куба не изменятся
circle1.set_sides(15)  # изменяем сторону круга
print(circle1.get_sides())  # выводим новую длину окружности

# Проверка периметра (длины окружности)
print(len(circle1))  # выводим периметр круга

# Проверка объёма куба
print(cube1.get_volume())  # выводим объём куба
