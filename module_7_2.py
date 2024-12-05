import string # Импортируем модуль string для работы с пунктуацией

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names # Сохраняем имена файлов в атрибут file_names

    def get_all_words(self):
        all_words = {} # Создаем пустой словарь для хранения слов
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file: # Открываем файл с помощью оператора with
                    content = file.read().lower() # Читаем содержимое файла и приводим его к нижнему регистру
                    for punct in string.punctuation:
                        content = content.replace(punct, '') # Удаляем пунктуацию из текста
                    words = content.split() # Разбиваем текст на слова
                    all_words[file_name] = words # Записываем слова в словарь
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.") # Обработка ошибки, если файл не найден
        return all_words # Возвращаем словарь всех слов

    def find(self, word):
        word = word.lower() # Приводим искомое слово к нижнему регистру
        positions = {} # Создаем словарь для хранения позиций
        all_words = self.get_all_words() # Получаем все слова из файлов
        for file_name, words in all_words.items():
            try:
                position = words.index(word) + 1 # Находим позицию слова в списке
            except ValueError:
                position = None # Если слово не найдено, устанавливаем позицию в None
            positions[file_name] = position # Записываем позицию в словарь
        return positions # Возвращаем словарь позиций

    def count(self, word):
        word = word.lower() # Приводим искомое слово к нижнему регистру
        counts = {} # Создаем словарь для хранения количества вхождений
        all_words = self.get_all_words() # Получаем все слова из файлов
        for file_name, words in all_words.items():
            count = words.count(word) # Считаем количество вхождений слова
            counts[file_name] = count # Записываем количество в словарь
        return counts # Возвращаем словарь количества вхождений

# Пример использования класса
finder2 = WordsFinder('test_file.txt') # Создаем объект класса WordsFinder
print(finder2.get_all_words()) # Выводим все слова из файла
print(finder2.find('TEXT')) # Ищем слово 'TEXT' и выводим его позицию
print(finder2.count('teXT')) # Считаем количество вхождений слова 'teXT'

