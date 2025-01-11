import time  # импортируем модуль для измерения времени
from multiprocessing import Pool  # импортируем Pool для многопроцессного подхода
import os  # модуль os для работы с путями


def read_info(name):
    """Функция для построчного чтения файла."""
    try:  # блок обработки исключений
        with open(name, 'r') as file:  # открываем файл для чтения
            while True:  # запускаем бесконечный цикл
                line = file.readline()  # считываем строку из файла
                if not line:  # проверяем, если строка пустая
                    break  # выходим из цикла
    except FileNotFoundError:  # обрабатываем случай, если файл не найден
        print(f"Файл {name} не найден. Проверьте путь и название файла.")  # выводим сообщение об ошибке


if __name__ == '__main__':
    # Указываем путь к директории, где находятся файлы
    base_dir = '/Users/igorvasin/PycharmProjects/Lessons0'  # абсолютный путь к папке с файлами
    filenames = [os.path.join(base_dir, f'file_{number}.txt') for number in range(1, 5)]  # список файлов

    # Линейный вызов
    start_time = time.time()  # фиксируем начальное время
    for filename in filenames:  # проходим по каждому файлу
        read_info(filename)  # вызываем функцию для чтения файла
    end_time = time.time()  # фиксируем конечное время
    print(f'Линейное выполнение заняло: {end_time - start_time:.2f} секунд')  # выводим время выполнения

    # Многопроцессный вызов
    start_time = time.time()  # фиксируем начальное время
    with Pool() as pool:  # создаем пул процессов
        pool.map(read_info, filenames)  # вызываем функцию read_info для каждого файла в пуле
    end_time = time.time()  # фиксируем конечное время
    print(f'Многопроцессное выполнение заняло: {end_time - start_time:.2f} секунд')  # выводим время выполнения
