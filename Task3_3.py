# 3.Задайте список из вещественных чисел. Напишите программу, которая 
# найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def spliting (list1):
    drob=[]
    for i in list1:
        if '.' in str(i): drob.append(round(i%1,5))
    max_elem=max(drob)
    min_elem=min(drob)
    return max_elem - min_elem


spisok = [1.1, 1.3, 3.1, 5, 10.01]

spisok_drob=spliting (spisok)
print (spisok)
print (f'разница между макс и мин дробной частью {spisok_drob}')

