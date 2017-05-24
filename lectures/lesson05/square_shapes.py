#

"""Модуль расчета площадей геометрических фигур"""

def calculate_square_area(x):
    """по длине стороне считает площадь квадрата"""
    return x**2

def calculate_rechtangle_area(a, b):
    """по длинам сторон считает  площадь прямоугольника"""
    return a*b
a = 666

__all__ = [ #перечень импортируемых функций по команде import *
        "calculate_square_area",
        "calculate_rechtangle_area"
        ]

if __name__ == "__main__":
    print("тест")
