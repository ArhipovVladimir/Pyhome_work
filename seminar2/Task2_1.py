# Домашнее задание
# 1 Подсчитать сумму цифр в вещественном числе.
 
def sum_digit (dig):
    dig_r= dig.replace(".","")
    result= 0
    for i in dig_r:
        result+=int(i)
    return result

num=input("введите вещ. число:")
print (f'Сумма числе числа {sum_digit(num)}') 

