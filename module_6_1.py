class Animal: # Создаем класс Animal
    def __init__(self, name): # Инициализируем объект класса Animal
        self.alive = True # Устанавливаем атрибут объекта alive в True
        self.fed = False # Устанавливаем атрибут объекта fed в False
        self.name = name # Устанавливаем атрибут объекта name

class Plant: # Создаем класс Plant
    def __init__(self, name): # Инициализируем объект класса Plant
        self.edible = False # Устанавливаем атрибут объекта edible в False
        self.name = name # Устанавливаем атрибут объекта name

class Mammal(Animal): # Создаем класс Mammal, наследующий от Animal
    def eat(self, food): # Определяем метод eat
        if food.edible: # Проверяем атрибут edible объекта food
            print(f"{self.name} съел {food.name}") # Выводим сообщение о съедении
            self.fed = True # Меняем атрибут объекта fed на True
        else:
            print(f"{self.name} не стал есть {food.name}") # Выводим сообщение о несъеденном растении
            self.alive = False # Меняем атрибут объекта alive на False

class Predator(Animal): # Создаем класс Predator, наследующий от Animal
    def eat(self, food): # Определяем метод eat
        if food.edible: # Проверяем атрибут edible объекта food
            print(f"{self.name} съел {food.name}") # Выводим сообщение о съедении
            self.fed = True # Меняем атрибут объекта fed на True
        else:
            print(f"{self.name} не стал есть {food.name}") # Выводим сообщение о несъеденном растении
            self.alive = False # Меняем атрибут объекта alive на False

class Flower(Plant): # Создаем класс Flower, наследующий от Plant
    pass # Ничего не меняем, просто наследуем

class Fruit(Plant): # Создаем класс Fruit, наследующий от Plant
    def __init__(self, name): # Переопределяем инициализацию
        super().__init__(name) # Вызываем инициализацию родительского класса
        self.edible = True # Устанавливаем атрибут объекта edible в True

# Создаем объекты классов
a1 = Predator('Волк с Уолл-Стрит') # Создаем объект класса Predator
a2 = Mammal('Хатико') # Создаем объект класса Mammal
p1 = Flower('Цветик семицветик') # Создаем объект класса Flower
p2 = Fruit('Заводной апельсин') # Создаем объект класса Fruit

print(a1.name) # Выводим атрибут name объекта a1
print(p1.name) # Выводим атрибут name объекта p1

print(a1.alive) # Выводим атрибут alive объекта a1
print(a2.fed) # Выводим атрибут fed объекта a2
a1.eat(p1) # Объект a1 вызывает метод eat с объектом p1
a2.eat(p2) # Объект a2 вызывает метод eat с объектом p2
print(a1.alive) # Выводим атрибут alive объекта a1 после еды
print(a2.fed) # Выводим атрибут fed объекта a2 после еды
