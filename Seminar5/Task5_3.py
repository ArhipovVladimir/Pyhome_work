
# 3 Дан файл jack.txt (https://disk.yandex.ru/d/orFlUSXkcA600w)
# по аналогии с предыдущим заданием составить аналогичный словарь.

stroka=[]

with open ("jack.txt","r") as data:
    for stroka in data:
         print (stroka)

list_stroka = stroka.split(" ")
print(list_stroka)

set_stroka = set(list_stroka)
print(set_stroka)

list_srtoka_no_dubl = list(set_stroka)
list_count=[]

for element in list_srtoka_no_dubl:
    list_count.append(list_stroka.count(element))

result_dict = dict(zip(list_srtoka_no_dubl, list_count))
print (result_dict)

# 3 Дан файл jack.txt (https://disk.yandex.ru/d/orFlUSXkcA600w)
# по аналогии с предыдущим заданием составить аналогичный словарь.