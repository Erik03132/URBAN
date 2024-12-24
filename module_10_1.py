import threading # импортируем модуль для работы с потоками
from time import sleep, time # импортируем sleep для паузы и time для измерения времени

def write_words(word_count, file_name): # объявляем функцию write_words с двумя параметрами
    with open(file_name, 'w', encoding='utf-8') as file: # открываем файл для записи с указанием кодировки
        for i in range(1, word_count + 1): # цикл для записи слов
            file.write(f"Какое-то слово № {i}\n") # записываем строку в файл
            sleep(0.1) # делаем паузу на 0.1 секунду
    print(f"Завершилась запись в файл {file_name}") # выводим сообщение о завершении записи

# Взятие текущего времени перед выполнением функций
start_time = time() # фиксируем начальное время

# Запуск функций с аргументами из задачи
write_words(10, "example1.txt") # вызов функции с 10 словами
write_words(30, "example2.txt") # вызов функции с 30 словами
write_words(200, "example3.txt") # вызов функции с 200 словами
write_words(100, "example4.txt") # вызов функции с 100 словами

# Взятие текущего времени после выполнения функций
end_time = time() # фиксируем конечное время
print(f"Время выполнения функций: {end_time - start_time} секунд") # выводим разницу времени

# Взятие текущего времени перед выполнением потоков
start_time_threads = time() # фиксируем начальное время для потоков

# Создание потоков
thread1 = threading.Thread(target=write_words, args=(10, "example5.txt")) # создаем поток с 10 словами
thread2 = threading.Thread(target=write_words, args=(30, "example6.txt")) # создаем поток с 30 словами
thread3 = threading.Thread(target=write_words, args=(200, "example7.txt")) # создаем поток с 200 словами
thread4 = threading.Thread(target=write_words, args=(100, "example8.txt")) # создаем поток с 100 словами

# Запуск потоков
thread1.start() # запускаем первый поток
thread2.start() # запускаем второй поток
thread3.start() # запускаем третий поток
thread4.start() # запускаем четвертый поток

# Ожидание завершения потоков
thread1.join() # ждем завершения первого потока
thread2.join() # ждем завершения второго потока
thread3.join() # ждем завершения третьего потока
thread4.join() # ждем завершения четвертого потока

# Взятие текущего времени после выполнения потоков
end_time_threads = time() # фиксируем конечное время для потоков
print(f"Время выполнения потоков: {end_time_threads - start_time_threads} секунд") # выводим разницу времени для потоков
