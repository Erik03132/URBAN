from threading import Thread # импортируем класс Thread из библиотеки threading
import time # импортируем библиотеку time для использования задержек

class Knight(Thread): # создаем класс Knight, наследованный от Thread
    def __init__(self, name, power): # определяем инициализатор класса
        super().__init__() # вызываем инициализатор родительского класса Thread
        self.name = name # устанавливаем имя рыцаря
        self.power = power # устанавливаем силу рыцаря

    def run(self): # определяем метод run, который будет выполняться в потоке
        global enemies # объявляем глобальную переменную enemies для доступа к общему количеству врагов
        days = 0 # переменная для подсчета дней сражения
        print(f"{self.name}, на нас напали!") # вывод сообщения о начале сражения
        while enemies > 0: # пока есть враги
            time.sleep(1) # задержка в 1 секунду
            enemies -= self.power # уменьшаем количество врагов на силу рыцаря
            days += 1 # увеличиваем количество дней сражения
            enemies = max(enemies, 0) # чтобы количество врагов не стало отрицательным
            print(f"{self.name} сражается {days}..., осталось {enemies} воинов.") # вывод текущего состояния сражения
        print(f"{self.name} одержал победу спустя {days} дней(дня)!") # вывод сообщения о победе

# Инициализация общего количества врагов
enemies = 100 # общее количество врагов

# Создание объектов рыцарей
first_knight = Knight('Sir Lancelot', 10) # создаем первого рыцаря с именем Sir Lancelot и силой 10
second_knight = Knight("Sir Galahad", 20) # создаем второго рыцаря с именем Sir Galahad и силой 20

# Запуск потоков
first_knight.start() # запускаем поток для первого рыцаря
second_knight.start() # запускаем поток для второго рыцаря

# Ожидание завершения потоков
first_knight.join() # ожидаем завершения потока первого рыцаря
second_knight.join() # ожидаем завершения потока второго рыцаря

# Вывод строки об окончании сражения
print("Битва окончена!") # вывод сообщения об окончании битвы