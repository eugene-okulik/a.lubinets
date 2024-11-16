# Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел
from math import sqrt

first_num = 5
second_num = 7


avg_arithmetic = (first_num + second_num) / 2
print(f"Среднее арифметическое: {avg_arithmetic}")

avg_geometric = sqrt(first_num * second_num)
print(f"Среднее геометрическое: {avg_geometric}")
