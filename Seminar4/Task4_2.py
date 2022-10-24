# 2 Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.

def find_mult (dig1):
    num = dig1
    spisok = []
    while num != 1: 
        for i in (2, 3, 5, 7, 11, 13, 17):
            if num % i == 0:spisok.append(i); num = num / i
    return spisok

dig = int(input("введите число: "))
print (find_mult (dig))