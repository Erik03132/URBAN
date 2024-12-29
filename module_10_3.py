import threading # импорт модуля для работы с потоками
from random import randint # импорт функции для генерации случайных чисел
from time import sleep # импорт функции для ожидания

class Bank:
    def __init__(self): # инициализация объекта класса
        self.balance = 0 # начальный баланс банка
        self.lock = threading.Lock() # объект блокировки для потоков

    def deposit(self): # метод для пополнения баланса
        for _ in range(100): # цикл для выполнения 100 транзакций
            amount = randint(50, 500) # случайное число для пополнения
            self.balance += amount # увеличение баланса
            if self.balance >= 500 and self.lock.locked(): # проверка на разблокировку
                self.lock.release() # разблокировка замка
            print(f"Пополнение: {amount}. Баланс: {self.balance}") # вывод информации о пополнении
            sleep(0.001) # ожидание для имитации скорости выполнения операций

    def take(self): # метод для снятия средств
        for _ in range(100): # цикл для выполнения 100 транзакций
            amount = randint(50, 500) # случайное число для снятия
            print(f"Запрос на {amount}") # вывод информации о запросе
            if amount <= self.balance: # проверка достаточности средств
                self.balance -= amount # уменьшение баланса
                print(f"Снятие: {amount}. Баланс: {self.balance}") # вывод информации о снятии
            else:
                print("Запрос отклонён, недостаточно средств") # вывод сообщения об отклонении запроса
                self.lock.acquire() # блокировка потока

# Создание объекта класса Bank
bk = Bank()

# Создание потоков для методов deposit и take
th1 = threading.Thread(target=Bank.deposit, args=(bk,)) # поток для пополнения
th2 = threading.Thread(target=Bank.take, args=(bk,)) # поток для снятия

# Запуск потоков
th1.start() # старт первого потока
th2.start() # старт второго потока

# Ожидание завершения потоков
th1.join() # ожидание завершения первого потока
th2.join() # ожидание завершения второго потока

# Вывод итогового баланса
print(f'Итоговый баланс: {bk.balance}') # вывод итогового баланса
