# Модуль №11. Стандартные и сторонние библиотеки Python. Интроспекция. Домашнее задание
import re
import requests
from pprint import pprint

def introspection_info(obj):
    info = {}
    type_of_obj = re.split(r"['.]", str(type(obj)))
    if len(type_of_obj) == 3:
        info.update({'type:': type_of_obj[1]})
    elif len(type_of_obj) == 4:
        info.update({'type:': type_of_obj[2]})
    attributes_of_obj = get_attributes_my(obj)
    info.update({'attributes': attributes_of_obj})
    methods_of_obj = get_methods_my(obj)
    info.update({'methods': methods_of_obj})
    if isinstance(obj, (int, str, float, bool, list, tuple, set, dict)):
        info.update({'module': '__main__'})
    else:
        info.update({'module': obj.__module__})
    return info

def get_attributes_my(obj):
    attributes = []
    for attr in dir(obj):
        if attr[0:2] != '__':
            if not callable(getattr(obj, attr)):
                attributes.append(attr)
    return attributes

def get_methods_my(obj):
    methods = []
    for attr in dir(obj):
        if attr[0:2] != '__':
            if callable(getattr(obj, attr)):
                methods.append(attr)
    return methods

def function1():
    pass

class MyClass:
    attribute_1 = 48
    attribute_2 = 'Это строка'
    attribute_3 = True

    def my_method(self):
        pass

    def my_method_2(self):
        pass

a = 42
b = 'Строка'
c = True
list_1 = [1, 2, 3]
tuple_1 = (1, 2, 3)
set_1 = {1, 2, 3}
dict_1 = {'1': 1, '2': 2, '3': 3}
d = MyClass()

print(introspection_info(a))
print(introspection_info(b))
print(introspection_info(c))
print(introspection_info(list_1))
print(introspection_info(tuple_1))
print(introspection_info(set_1))
print(introspection_info(dict_1))
print(introspection_info(MyClass))
print(introspection_info(d))
print(introspection_info(d.my_method))
print(introspection_info(pprint))

