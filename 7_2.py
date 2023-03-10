"""
Установить через pip библиотеку numpy. С помощью этой библиотеки cоздать массив 3x3 
со случайными значениями, вывести его. Транспонировать его и вывести.
"""

"""Подключаем установленную нашу библиотеку и даем ей сокращения, для удобства использования"""
import numpy as np

"""Создаем массив 3 на 3 со случайными значениями и выводим его"""
x = np.random.sample((3,3))
print(x)

"""Транспонируем наш массив и выводим его"""
y = np.transpose(x)
print(y)
