
# 3 Задать список из n чисел последовательности (1+ 1 ) и вывести на экран их сумму.n

# def sum_digit(dig):
#     result_list1 = []
#     sum1 = 0
#     for i in range(1, dig+1):
#         result = round(((1+1/i)**i), 2)
#         result_list1.append(result)
#     sum1 = sum(result_list1)
#     return (sum1, result_list1)
#
# num = int(input("введите число:"))
# print(f' сумма числел последовательности {sum_digit(num)[1]} равна {sum_digit(num)[0]}')

def sum_digit(dig):
    result_list1 = []
    sum1 = 0
    for i in range(1, dig+1):
        result = round(((1+1/i)**i), 2)
        result_list1.append(result)
    sum1 = sum(result_list1)
    return (sum1)

num = int(input("введите число:"))
print(f' сумма числел последовательности равна {sum_digit(num)}')

