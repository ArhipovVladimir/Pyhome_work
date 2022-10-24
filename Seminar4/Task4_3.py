# 3 Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.



def count1 (lister):
    new_list = []
    for i in lister:
        counter = lister.count(i)
        if counter == 1: new_list.append(i) 
    return new_list

list1 = [2, 3, 1, 5 , 1]
print (list1)
print (count1(list1))