def single_root_words(root_word, *other_words): # объявление функции с параметрами root_word и *other_words
    same_words = [] # создание пустого списка для хранения подходящих слов
    for word in other_words: # перебор каждого слова в other_words
        if root_word.lower() in word.lower() or word.lower() in root_word.lower(): # проверка условия на наличие root_word в слове или наоборот
            same_words.append(word) # добавление слова в список same_words, если условие выполнено
    return same_words # возврат списка same_words в качестве результата

# Вызов функции и вывод результата на консоль
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies') # вызов функции с первым набором аргументов
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel') # вызов функции со вторым набором аргументов

print(result1) # вывод результата первого вызова на консоль, ожидается ['richiest', 'richies']
print(result2) # вывод результата второго вызова на консоль, ожидается ['Disable']









