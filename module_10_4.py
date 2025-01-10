from threading import Thread
from queue import Queue
import time
import random

# Класс Table
class Table:
    def __init__(self, number): # инициализация стола с номером
        self.number = number # номер стола
        self.guest = None # гость за столом (по умолчанию None)

# Класс Guest
class Guest(Thread): # наследуется от Thread
    def __init__(self, name): # инициализация гостя с именем
        super().__init__() # вызов конструктора родительского класса
        self.name = name # имя гостя

    def run(self): # метод потока
        time.sleep(random.randint(3, 10)) # ожидание от 3 до 10 секунд

# Класс Cafe
class Cafe:
    def __init__(self, *tables): # инициализация кафе со столами
        self.tables = list(tables) # список столов
        self.queue = Queue() # очередь гостей

    def guest_arrival(self, *guests): # прибытие гостей
        for guest in guests: # для каждого гостя
            for table in self.tables: # проверяем столы
                if table.guest is None: # если стол свободен
                    table.guest = guest # садим гостя за стол
                    guest.start() # запускаем поток гостя
                    print(f"{guest.name} сел(-а) за стол номер {table.number}") # сообщение
                    break # выходим из цикла
            else: # если свободных столов нет
                self.queue.put(guest) # добавляем гостя в очередь
                print(f"{guest.name} в очереди") # сообщение

    def discuss_guests(self): # обслуживание гостей
        while not self.queue.empty() or any(table.guest is not None for table in self.tables): # пока очередь не пуста или есть занятые столы
            for table in self.tables: # проверяем каждый стол
                if table.guest and not table.guest.is_alive(): # если за столом есть гость и он закончил приём пищи
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)") # сообщение
                    print(f"Стол номер {table.number} свободен") # сообщение
                    table.guest = None # освобождаем стол

                if not self.queue.empty() and table.guest is None: # если очередь не пуста и стол свободен
                    next_guest = self.queue.get() # берём гостя из очереди
                    table.guest = next_guest # садим гостя за стол
                    next_guest.start() # запускаем поток гостя
                    print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}") # сообщение

# Создание столов
tables = [Table(number) for number in range(1, 6)] # создаём 5 столов

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
] # список имён гостей

# Создание гостей
guests = [Guest(name) for name in guests_names] # создаём гостей

# Заполнение кафе столами
cafe = Cafe(*tables) # создаём кафе с 5 столами

# Приём гостей
cafe.guest_arrival(*guests) # принимаем гостей

# Обслуживание гостей
cafe.discuss_guests() # обслуживаем гостей
