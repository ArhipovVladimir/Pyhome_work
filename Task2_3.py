
# 3 Задать список из n чисел последовательности (1+ 1 ) и вывести на экран их сумму.n

def sum_digit (dig):
    result_list= []
    sum=0
    for i in range(1,dig+1):
       result=round(((1+1/i)**i),5)
       result_list.append(result)
       sum+=result
    return (sum,result_list)

num=int(input(" введите число:"))
print (f' сумма числел последовательности {sum_digit(num)[1]} равна {sum_digit(num)[0]}') 





# 4 Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов
# на указанных позициях. Позиции хранятся в списке positions - создайте этот список (например:
# positions = [1, 3, 6]).
# 5 Реализовать алгоритм перемешивания списка.