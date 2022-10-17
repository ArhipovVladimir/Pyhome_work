#  2.Напишите программу, которая найдёт произведение 
# пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def new_list (l):
    i=0
    new_list=[]
    halb_len = int(len (l)/2)
    print (halb_len)
    for i in range (0, halb_len):
        new_list.append(l[i]*l[len(l)-1-i])
      
       
    if len(l) % 2 != 0:
        new_list.append(l[halb_len]**2)

    return new_list

list = [2, 3, 5, 6]

print(new_list (list))

