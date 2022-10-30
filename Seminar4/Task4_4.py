# 4 Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def get_urovn(k):
    resalt =""
    for i in range (k, 0 , -1):
        resalt = resalt + str(random.randint(0, 101)) + " x^" + str(i) + " + " 
    resalt = resalt + str(random.randint(0, 101)) + " = 0"
    return resalt


pow = int(input("степень: "))
urov = get_urovn(pow)
print (urov)

data = open ('file.txt', 'w') 
data.write (urov)
data.close()


# 4 Р—Р°РґР°РЅР° РЅР°С‚СѓСЂР°Р»СЊРЅР°СЏ СЃС‚РµРїРµРЅСЊ k. РЎС„РѕСЂРјРёСЂРѕРІР°С‚СЊ СЃР»СѓС‡Р°Р№РЅС‹Рј РѕР±СЂР°Р·РѕРј СЃРїРёСЃРѕРє
# РєРѕСЌС„С„РёС†РёРµРЅС‚РѕРІ (Р·РЅР°С‡РµРЅРёСЏ РѕС‚ 0 РґРѕ 100) РјРЅРѕРіРѕС‡Р»РµРЅР° Рё Р·Р°РїРёСЃР°С‚СЊ РІ С„Р°Р№Р» РјРЅРѕРіРѕС‡Р»РµРЅ
# СЃС‚РµРїРµРЅРё k.
# РџСЂРёРјРµСЂ:
# k=2 => 2xВІ + 4x + 5 = 0 РёР»Рё xВІ + 5 = 0 РёР»Рё 10*xВІ = 0

import random


def get_urovn(k):
    resalt = ""
    for i in range(k, 0 , -1):
        resalt = resalt + str(random.randint(0, 101)) + " x^" + str(i) + " + " 
    resalt = resalt + str(random.randint(0, 101)) + " = 0"
    return resalt


pow = int(input("СЃС‚РµРїРµРЅСЊ: "))
urov = get_urovn(pow)
print(urov)

data = open('file.txt', 'w')
data.write(urov)
data.close()


# pow - СЌС‚Рѕ РІСЃС‚СЂРѕРµРЅРЅР°СЏ С„СѓРЅРєС†РёСЏ! Р›СѓС‡С€Рµ РїРµСЂРµРёРјРµРЅРѕРІР°С‚СЊ РїРµСЂРµРјРµРЅРЅСѓСЋ!
# pow -> input_pow
# Р»СѓС‡С€Рµ РёСЃРїРѕР»СЊР·РѕРІР°С‚СЊ РЅРµ С‚СЂР°РЅСЃР»РёС‚РµСЂР°С†РёСЋ, Р° Р°РЅРіР»РёР№СЃРєРёРµ СЃР»РѕРІР°:
# resalt -> result
# urov -> level
# get_urovn -> get_level
