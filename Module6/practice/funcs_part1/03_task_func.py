# Даны координаты двух точек на плоскости.
# Напишите функцию нахождения расстояния между двумя точками.
def distance(x1, y1, x2, y2):
def distance(x1, y1, x2, y2):
    lx = abs(x2 - x1)
    ly = abs(y2 - y1)
    return lx, ly




# Тестируем функцию
print(distance(2, 4, 2, 9))
print(distance(12, 8, 12, -9))
print(distance(23, 0, 15, 32))
