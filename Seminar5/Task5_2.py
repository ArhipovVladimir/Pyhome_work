
# 1.Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;

# 2 Дана строка:
# 'дом, окно, дверь, стена, кухня, стол, стул, дверь, дом, стул, стол, окно, стул'
# Необходимо получить словарь, в котором ключи – слова, значения – количество слов в
# строке:
# {'дом': 2, 'окно': 2, 'дверь': 2, 'стена': 1, 'кухня': 1, 'стол': 2, 'стул': 3}

stroka = 'дом, окно, дверь, стена, кухня, стол, стул, дверь, дом, стул, стол, окно, стул'
print(stroka)

list_stroka = stroka.split(", ")
print(list_stroka)

set_stroka = set(list_stroka)
print(set_stroka)

list_srtoka_no_dubl = list(set_stroka)
list_count=[]

# list_count = map(lambda element: list_count.append(list_stroka.count(element), list_stroka)) 
for element in list_srtoka_no_dubl:
    list_count.append(list_stroka.count(element))

result_dict = dict(zip(list_srtoka_no_dubl, list_count))
print (result_dict)

