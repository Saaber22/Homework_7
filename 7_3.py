"""Создать файл с функциями (на своё усмотрение). Во втором файле 
подключить его как библиотеку и запустить функции."""

"""Подключаем функции, которые нам нужны из файла"""
from modul7_3 import modern_string as mstr
from modul7_3 import reverse_string as rstr

"""Выполняем данные функции"""
print(mstr('Linux'))
print(rstr(mstr('Linux')))

