# 1 Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141 10-1 <= d <= 10-10
import math


def res_round(r):
    r1 = len(r.split('.')[1])
    resalt = round (math.pi,r1)
    return resalt


razm = input('Веедите точность числа Например 0.0001')
print(res_round (razm))