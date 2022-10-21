# *Пример:*

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#  [Негафибоначчи] (https://ru.wikipedia.org/wiki/Негафибоначчи)


def dex_bin (num):
    x = [1, 1]
    for i in range(2, num):
        x.append(x[i-1] + x[i-2])
    
    y= [-x[num-1], x[num-2]]
    for i in range(2, num*2+1):
        y.append(y[i-1] + y[i-2])
    return y


dig=int(input("введите число: "))
print (dex_bin(dig))
