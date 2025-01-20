# библиотека numpy
import numpy as np # импортируем библиотеку numpy

array = np.array([1, 2, 3, 4, 5]) # создаем массив чисел
print(array) # выводим массив на консоль

squared_array = array ** 2 # возводим каждый элемент массива в квадрат
print(squared_array) # выводим массив квадратов

mean_value = np.mean(array) # вычисляем среднее значение массива
print(mean_value) # выводим среднее значение

# Библиотека requests
import requests # импортируем библиотеку requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1') # отправляем GET-запрос на сайт
print(response.status_code) # выводим статус ответа
print(response.headers['Content-Type']) # выводим тип содержимого ответа
print(response.json()) # выводим содержимое ответа в формате JSON

# Библиотека matplotlib
import matplotlib.pyplot as plt # импортируем модуль pyplot из matplotlib

x = [1, 2, 3, 4, 5] # создаем список значений для оси X
y = [1, 4, 9, 16, 25] # создаем список значений для оси Y

plt.plot(x, y, label='Квадраты чисел') # строим линейный график
plt.title('График квадратов чисел') # задаем заголовок графика
plt.xlabel('X') # подписываем ось X
plt.ylabel('Y') # подписываем ось Y
plt.legend() # добавляем легенду
plt.show() # отображаем график
