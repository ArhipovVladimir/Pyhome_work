# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
# 5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def dex_bin (num):
    result = str('z')
    while num >0:
        resalt = str(num % 2) + resalt
        num = num // 2
    return result



dig=int(input("введите число: "))
print (dex_bin(dig))


