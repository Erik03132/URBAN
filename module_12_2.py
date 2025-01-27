def introspection_info(obj):  # Создаем функцию для интроспекции объекта
    info = {}  # Инициализируем словарь для хранения информации об объекте

    info['type'] = type(obj).__name__  # Определяем тип объекта
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith(
        "__")]  # Получаем список атрибутов объекта
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith(
        "__")]  # Получаем список методов объекта
    info['module'] = getattr(obj, '__module__', 'built-in')  # Определяем модуль, к которому принадлежит объект

    return info  # Возвращаем словарь с информацией об объекте


# Пример работы функции
number_info = introspection_info(42)  # Вызываем функцию для числа 42
print(number_info)  # Выводим результат на консоль


# Создаем свой класс для тестирования
class MyClass:
    def __init__(self, value):
        self.value = value  # Устанавливаем атрибут value

    def my_method(self):
        return f"My value is {self.value}"  # Пример метода


# Создаем объект своего класса
my_object = MyClass(10)  # Создаем объект с атрибутом value=10

# Пример работы функции с объектом пользовательского класса
object_info = introspection_info(my_object)  # Вызываем функцию для объекта
print(object_info)  # Выводим результат на консоль
