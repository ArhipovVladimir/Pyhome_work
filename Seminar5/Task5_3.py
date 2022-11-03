
# # # 3 Дан файл jack.txt (https://disk.yandex.ru/d/orFlUSXkcA600w)
# # # по аналогии с предыдущим заданием составить аналогичный словарь.
# #
# stroka=[]

# with open ("jack.txt","r", encoding='utf-8') as data:
#         reader

# list_stroka = stroka.split(" ")
# print(list_stroka)

# set_stroka = set(list_stroka)
# print(set_stroka)

# list_srtoka_no_dubl = list(set_stroka)
# list_count=[]

# for element in list_srtoka_no_dubl:
#     list_count.append(list_stroka.count(element))

# result_dict = dict(zip(list_srtoka_no_dubl, list_count))
# print (result_dict)
# #
# # 3 Дан файл jack.txt (https://disk.yandex.ru/d/orFlUSXkcA600w)
# # по аналогии с предыдущим заданием составить аналогичный словарь.
#
# # ############################################################

file = 'jack.txt'
# указываем кодировку файла encoding='utf-8'
# если windows-1251, то encoding='cp1251'
with open(file, 'r', encoding='utf-8') as fp:
    data = fp.read()
# print(data)  # весь текст
# print(type(data))  # <class 'str'> - тип "строка"


def create_dict(input_str):
    # split() - если не указан аргумент, то по-умолчанию пробел (" ")
    words = input_str.split()

    # # ____________________ вариант без map и  lambda:
    # for word in words:
    #     # strip() - очищаем от знаков слева и справа
    #     # lower() - переводим в нижний регистр
    #     word = word.strip('.,?!:;').lower()
    #     # print(word)
    # # -----------------------------------------------

    words = tuple(map(lambda x: x.strip('.,?!:;').lower(), words))
    # print(len(tuple(words)))  # 246

    unique_words = set(words)
    # print(len(unique_words))  # 56

    counts = []
    for el in unique_words:
        counts.append(words.count(el))
    # print(sum(counts))  # 246

    return dict(zip(unique_words, counts))


print(create_dict(data))
