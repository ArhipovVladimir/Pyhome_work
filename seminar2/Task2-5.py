#  5 Реализовать алгоритм перемешивания списка.
# у меня ошибка с индексом массива 
from random import randint


def get_digit (dig):
    result_list= []
    for i in range(-dig,dig+1):
       result_list.append(i)
    return (result_list)



def no_sort_list (list):
    for i in range(0,len(list)-1):
        rx = randint(0,len(list)-1)
        list[i], list[rx] = list[rx], list[i]
    return list


num=int(input(" введите число:"))
list= get_digit(num)
print (f' исходный список {list}') 
new_list= no_sort_list(list)
print (f' перемешанный список {new_list}') 