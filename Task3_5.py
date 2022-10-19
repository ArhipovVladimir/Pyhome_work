# *Пример:*

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#  [Негафибоначчи] (https://ru.wikipedia.org/wiki/Негафибоначчи)


def dex_bin (num):
    result = str('z')
    while num >0:
        resalt = str(num % 2) + resalt
        num = num // 2
    return result



dig=int(input("введите число: "))
print (dex_bin(dig))
