# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь
from math import sqrt

k1 = 12
k2 = 5

hypatenuse = sqrt(k1 ** 2 + k2 ** 2)
square = (k1 * k2) / 2

print(f"Гипотенуза равна: {hypatenuse}")
print(f"Площадь равна: {square}")
