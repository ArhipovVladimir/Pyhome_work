# 4 Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов
# на указанных позициях. Позиции хранятся в списке positions - создайте этот список (например:
# positions = [1, 3, 6]).

def get_digit (dig):
    result_list= []
    for i in range(-dig,dig+1):
       result_list.append(i)
    return (result_list)

def pow_poz (l,l_poz):
    resalt=1
    for i in l:
        if i in l_poz: resalt *=l[i]
    return resalt



num=int(input(" введите число:"))
list= get_digit(num)
list_poz=[2,4]
pow=pow_poz(list, list_poz)
print (f' произведение числел последовательности {get_digit(num)} равна {pow}') 

