immutable_var = (42, "Hello", 3.14, True) # создание переменной и присвоение ей кортежа
print(immutable_var) # вывод кортежа immutable_var на экран
#immutable_var[0] = 100 # попытка изменить первый элемент кортежа (Кортежи в Python являются неизменяемыми (immutable) структурами данных, что означает, что их элементы нельзя изменять после создания)
mutable_list = [10, "World", 2.71, False] # создание переменной mutable_list и присвоение ей списка с элементами разных типов данных
mutable_list[0] = 20 # изменение первого элемента списка mutable_list
mutable_list[1] = "Hello, World" # изменение второго элемента списка mutable_list
mutable_list[2] = 3.14 # изменение третьего элемента списка mutable_list
mutable_list[3] = True # изменение четвертого элемента списка mutable_list
print(mutable_list) # вывод измененного списка mutable_list на экран

