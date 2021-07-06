from pympler import asizeof


class DataItem1(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


d1 = DataItem1("Alex", 42)
print(d1.__dict__)
print(f"Общир размер объекта d1: {asizeof.asizeof(d1)}")


class DataItem2(object):
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age


d2 = DataItem2("Ben", 33)
print(d2.__slots__)
print(f"Общий размер объекта d2: {asizeof.asizeof(d2)}")
"""
{'name': 'Alex', 'age': 42}
Общир размер объекта d1: 368
['name', 'age']
Общий размер объекта d2: 144
Использование слотов позволяет сохранить атрибуты в менее затратном по памяти списке
"""

