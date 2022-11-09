# Написать функцию-декоратор для кеширования значений функции
# Написать функцию seq(n)
# n = 0 ....N
# (1 + n) ** n возвращает [x1, x2, x3, , , , xn]
#

import datetime
import time
from functools import wraps


def cacher(func):
    cach = {}

    @wraps(func)
    def wrapper(*args):
        key = args
        if key not in cach:
            cach[key] = func(*args)
        print(cach)
        return cach[key]

    return wrapper


def log_func(log_lvl=0):
    def logger2(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_msg = f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}\t'
            if log_lvl >= 1:
                log_msg += f'функция: {func.__name__}\t'
                if log_lvl == 2:
                    log_msg += f"параметры: {', '.join(map(str, args))}\t"
            res = func(*args, **kwargs)
            log_msg += f'результат: {res}\n'
            with open('log_file.log', 'a', encoding='utf-8') as fp:
                fp.write(log_msg)
            return res

        return wrapper

    return logger2


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        res = func(*args, **kwargs)
        finish = time.time_ns()
        print(finish - start)
        return res

    return wrapper


@cacher
@timer
@log_func(2)
def seq(n):
    result = []
    for n in range(n):
        result.append((1 + n) ** n)
    return result

seq(3)
seq(5)
seq(12)
seq(3)
seq(8)
seq(12)
seq(24)


#
# @cacher
# @timer
# @log_func(2)
# map(seq, range (5))git