# 4 Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def get_urovn(k):
    resalt =""
    for i in range (k, 0 , -1):
        resalt = resalt + str(random.randint(0, 101)) + "x^" + str(i) + "+" 
    resalt = resalt + str(random.randint(0, 101))
    return resalt


pow = int(input("степень: "))
urov = get_urovn(pow)
print (urov)