"""
Подключить библиотеку os. С её помощью вывести: имя операционной системы; 
имя пользователя, вошедшего в терминал; список файлов и директорий в папке.
"""
import os
import getpass

print('Имя ОС:',os.name)

nameos = input('Введите название вашей системы (Windows, Linux):')

if 'windows'.lower() in nameos:
    print('Имя пользователя, вошедшего в терминал',getpass.getuser())
else:
    print('Имя пользователя, вошедшего в терминал',os.getlogin)

print('Список файлов и директорий в папке',os.listdir(path="."))