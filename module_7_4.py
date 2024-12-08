import os # импортируем модуль os для работы с файловой системой
import time # импортируем модуль time для работы с датой и временем

directory = "." # указываем путь к каталогу, который будем обходить (в данном случае текущая директория)

# используем os.walk для обхода каталога
for root, dirs, files in os.walk(directory): # перебираем корневую папку, подкаталоги и файлы
    for file in files: # перебираем файлы в текущем каталоге
        filepath = os.path.join(root, file) # формируем полный путь к файлу
        filetime = os.path.getmtime(filepath) # получаем время последнего изменения файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime)) # форматируем время в читаемый вид
        filesize = os.path.getsize(filepath) # получаем размер файла в байтах
        parent_dir = os.path.dirname(filepath) # получаем родительскую директорию файла
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}') # выводим информацию о файле