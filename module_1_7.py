grades_list = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] # создание списков оценок
students = ['Аарон', 'Бильбо', 'Джонни', 'Хендрик', 'Стив'] # создание списка имен студентов в алфавитном порядке
average_grades = {} # создание пустого словаря для хранения средних баллов
average_grades[students[0]] = sum(grades_list[0]) / len(grades_list[0]) # вычисление среднего для первого студента
average_grades[students[1]] = sum(grades_list[1]) / len(grades_list[1]) # вычисление среднего для второго студента
average_grades[students[2]] = sum(grades_list[2]) / len(grades_list[2]) # вычисление среднего для третьего студента
average_grades[students[3]] = sum(grades_list[3]) / len(grades_list[3]) # вычисление среднего для четвертого студента
average_grades[students[4]] = sum(grades_list[4]) / len(grades_list[4]) # вычисление среднего для пятого студента
print(average_grades) # вывод среднего балла каждого студента

