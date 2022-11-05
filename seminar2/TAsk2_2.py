# 2 Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

def sum_digit (dig):
    result_list= []
    result=1
    for i in range(1,dig+1):
       result*=i
       result_list.append(result)
    return result_list

num=int(input(" введите число:"))
print (f' произведение числе от 1 до N {sum_digit(num)}') 

