# Напишите программу, которая принимает 
# на вход координаты двух точек и находит 
# расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt

def dist_point (x1, y1, x2, y2):
    return round((sqrt ((x2-x1)**2+(y2-y1)**2)),2)


   

point_xa = int(input("Веедите координату х точки А: "))
point_ya = int(input("Веедите координату У точки А: "))
point_xb = int(input("Веедите координату Х точки В: "))
poini_yb = int(input("Веедите координату У точки В: "))
dist = dist_point (point_xa, point_ya, point_xb, poini_yb)
print (f'A ({point_xa},{point_ya}); B ({point_xb},{poini_yb}) -> {dist}')
