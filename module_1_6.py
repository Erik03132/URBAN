my_dict = {"Имя": "Год рождения"} # создание словаря с ключом "Имя" и значением "Год рождения"
print(my_dict) # вывод словаря на консоль
print(my_dict["Имя"]) # вывод значения по существующему ключу "Имя" из словаря my_dict
my_dict["Александр"] = 1990 # добавление пары "Александр": 1990 в словарь my_dict
my_dict["Мария"] = 1985 # добавление пары "Мария": 1985 в словарь my_dict
print(my_dict) # вывод обновленного словаря на консоль
removed_value = my_dict.pop("Александр") # удаление пары с ключом "Александр" из словаря my_dict и сохранение значения
print(removed_value) # вывод удаленного значения на консоль
print(my_dict) # вывод текущего состояния словаря my_dict на консоль

my_set = {1, 2.0, "текст", (1, 2), 1, "текст"} # создание множества my_set с элементами разных типов данных, включая повторяющиеся значения
print(my_set) # вывод множества my_set на консоль
print(my_set) # вывод множества my_set на консоль, отображаются только уникальные значения
my_set.add(3) # добавление элемента 3 в множество my_set
my_set.add("новый элемент") # добавление элемента "новый элемент" в множество my_set
print(my_set) # вывод обновленного множества my_set на консоль
my_set.remove(1) # удаление элемента 1 из множества my_set
print(my_set) # вывод обновленного множества my_set на консоль
print(my_set) # вывод текущего состояния множества my_set на консоль
