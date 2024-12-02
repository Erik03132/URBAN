class Product:
    def __init__(self, name, weight, category):  # Инициализация атрибутов класса Product
        self.name = name  # Название продукта
        self.weight = weight  # Вес продукта
        self.category = category  # Категория продукта

    def __str__(self):  # Метод для возвращения строки в формате "<название>, <вес>, <категория>"
        return f"{self.name}, {self.weight}, {self.category}"  # Форматирование строки


class Shop:
    def __init__(self):  # Инициализация атрибутов класса Shop
        self.__file_name = 'products.txt'  # Инкапсулированный атрибут с названием файла

    def get_products(self):  # Метод для чтения продуктов из файла
        try:
            with open(self.__file_name, 'r') as file:  # Открытие файла в режиме чтения
                return file.read()  # Чтение содержимого файла и возврат строки
        except FileNotFoundError:  # Если файл не найден
            return ''  # Возвращаем пустую строку

    def add(self, *products):  # Метод для добавления продуктов
        existing_products = self.get_products().splitlines()  # Получаем текущие продукты из файла в виде списка строк
        existing_names = [line.split(', ')[0] for line in existing_products]  # Извлекаем названия существующих продуктов

        with open(self.__file_name, 'a') as file:  # Открываем файл в режиме добавления
            for product in products:  # Перебираем переданные продукты
                if product.name not in existing_names:  # Если продукта с таким названием нет
                    file.write(str(product) + '\n')  # Записываем продукт в файл
                else:
                    print(f'Продукт {product.name} уже есть в магазине')  # Выводим сообщение, если продукт существует


# Пример работы программы
s1 = Shop()  # Создаем объект магазина

p1 = Product('Potato', 50.5, 'Vegetables')  # Создаем продукт "Potato"
p2 = Product('Spaghetti', 3.4, 'Groceries')  # Создаем продукт "Spaghetti"
p3 = Product('Potato', 5.5, 'Vegetables')  # Создаем еще один продукт "Potato" с другим весом

print(p2)  # Выводим информацию о продукте p2

s1.add(p1, p2, p3)  # Добавляем продукты в магазин

print(s1.get_products())  # Выводим все продукты из магазина

