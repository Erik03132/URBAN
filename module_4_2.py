def test_function():  # Определение функции test_function
    def inner_function():  # Определение внутренней функции inner_function
        print("Я в области видимости функции test_function")  # Вывод сообщения из внутренней функции

    inner_function()  # Вызов внутренней функции внутри test_function


test_function()  # Вызов функции test_function
# При попытке вызвать inner_function вне test_function, возникнет ошибка NameError, так как inner_function не находится в области видимости.
inner_function() # Попытка вызова внутренней функции вне test_function

