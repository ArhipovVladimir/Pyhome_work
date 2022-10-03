#  5 Реализовать алгоритм перемешивания списка.

from random import randint


def get_digit (dig):
    result_list= []
    for i in range(-dig,dig+1):
       result_list.append(i)
    return (result_list)

def no_sort_list (list):
    n_list=[]
    for i in range(0,len(list)-1):
        n_list[i] = list[randint(0,len(list)-1)]
    return n_list



num=int(input(" введите число:"))
list= get_digit(num)
new_list= no_sort_list(list)
print (f' исходный список {list}') 
print (f' перемешанный список {new_list}') 