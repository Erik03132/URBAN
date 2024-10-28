n = int(input("Введите число от 3 до 20: ")) # вводим число от 3 до 20

result = "" # создаем пустую строку для хранения результата

# перебираем все возможные пары чисел от 1 до 19
for i in range(1, 20):
    for j in range(i+1, 20): # начинаем с i+1, чтобы избежать дублирования пар и одинаковых чисел в паре
        if n % (i + j) == 0: # проверяем, делится ли n на сумму пары без остатка
            pair = f"{i}{j}" # формируем строку пары
            result += pair # добавляем пару в результат

print(f"Пароль для числа {n}: {result}") # выводим результат
