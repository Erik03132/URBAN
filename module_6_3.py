import random  # импортируем модуль random для генерации случайных чисел

class Animal:  # создаем класс Animal
    live = True  # атрибут, указывающий, что животное живое
    sound = None  # атрибут звука, изначально None
    _DEGREE_OF_DANGER = 0  # степень опасности, по умолчанию 0

    def __init__(self, speed):  # инициализация объекта с параметром скорости
        self._cords = [0, 0, 0]  # начальные координаты
        self.speed = speed  # скорость передвижения

    def move(self, dx, dy, dz):  # метод для перемещения
        if self._cords[2] + dz * self.speed < 0:  # проверяем, не уходим ли ниже допустимого уровня
            print("It's too deep, i can't dive :(")  # выводим сообщение при попытке уйти ниже 0
            return  # выходим из метода без изменений координат
        self._cords[0] += dx * self.speed  # изменяем координату x
        self._cords[1] += dy * self.speed  # изменяем координату y
        self._cords[2] += dz * self.speed  # изменяем координату z

    def get_cords(self):  # метод для получения текущих координат
        print(f"X: {int(self._cords[0])} Y: {int(self._cords[1])} Z: {int(self._cords[2])}")  # вывод координат

    def attack(self):  # метод атаки
        if self._DEGREE_OF_DANGER < 5:  # если степень опасности меньше 5
            print("Sorry, i'm peaceful :)")  # выводим, что животное мирное
        else:  # иначе
            print("Be careful, i'm attacking you 0_0")  # выводим предупреждение об атаке

    def speak(self):  # метод для издания звука
        if self.sound:  # если звук определен
            print(self.sound)  # выводим звук
        else:  # иначе
            print("...")  # выводим многоточие, если звук отсутствует


class Bird(Animal):  # создаем класс Bird, наследуемый от Animal
    beak = True  # наличие клюва

    def lay_eggs(self):  # метод для откладывания яиц
        print(f"Here are(is) {random.randint(1, 4)} eggs for you")  # выводим случайное количество яиц


class AquaticAnimal(Animal):  # создаем класс AquaticAnimal, наследуемый от Animal
    _DEGREE_OF_DANGER = 3  # степень опасности равна 3

    def dive_in(self, dz):  # метод для ныряния
        dz = abs(dz)  # берем модуль dz
        self._cords[2] -= dz * (self.speed / 2)  # уменьшаем координату z с учетом уменьшенной скорости
        if self._cords[2] < 0:  # проверяем, чтобы координата z не была меньше 0
            self._cords[2] = 0  # если меньше, устанавливаем в 0


class PoisonousAnimal(Animal):  # создаем класс PoisonousAnimal, наследуемый от Animal
    _DEGREE_OF_DANGER = 8  # степень опасности равна 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):  # создаем класс Duckbill, наследуемый от Bird, AquaticAnimal и PoisonousAnimal
    sound = "Click-click-click"  # звук, издаваемый утконосом


# Пример использования
db = Duckbill(10)  # создаем объект Duckbill со скоростью 10

print(db.live)  # выводим атрибут live
print(db.beak)  # выводим атрибут beak

db.speak()  # вызываем метод speak
db.attack()  # вызываем метод attack

db.move(1, 2, 3)  # перемещаем объект
db.get_cords()  # выводим текущие координаты
db.dive_in(6)  # вызываем метод dive_in для ныряния
db.get_cords()  # выводим текущие координаты

db.lay_eggs()  # вызываем метод lay_eggs


