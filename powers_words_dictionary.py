import math
from itertools import product
from functools import reduce


class Power_1000_Text:
    def __init__(self, **kwargs):
        # lang, power_1000, sex, forms
        self.lang = kwargs['lang'] if 'lang' in kwargs else False
        self.power_1000 = kwargs['power_1000']
        self.sex = kwargs['sex']
        self.forms = kwargs['forms']
        

# цифры от 1 до 9
CIFS_0_10 = tuple(range(0, 10))

# Числовой и текст.формат чисел от 1 до 20
NUMS_0_20 = tuple(range(0, 20))
'''
{0: 'ноль', 1: {'male': 'один', 'female': 'одна'}, 2: {'male': 'два', 'female': 'две'}, 3: 'три', 4: 'четыре', 5: 'пять', 
6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 
13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 
18: 'восемнадцать', 19: 'девятнадцать'}
'''
SYMS_WORDS_0_20 = dict(zip(NUMS_0_20,
                           ('ноль', {'male': 'один', 'female': 'одна'},
                            {'male': 'два', 'female': 'две'}, 'три', 'четыре', 'пять',
                            'шесть', 'семь', 'восемь', 'девять', 'десять',
                            'одиннадцать', 'двенадцать', 'тринадцать',
                            'четырнадцать', 'пятнадцать', 'шестнадцать',
                            'семнадцать', 'восемнадцать', 'девятнадцать')))

SYMS_WORDS_1_10 = dict(zip(CIFS_0_10,
                           ('ноль', {'male': 'один', 'female': 'одна'},
                            {'male': 'два', 'female': 'две'}, 'три', 'четыре',
                            'пять', 'шесть', 'семь', 'восемь', 'девять')))
SYMS_WORDS_10 = dict(zip(CIFS_0_10, ('ноль', 'десять', 'двадцать', 'тридцать',
                                     'сорок', 'пятьдесят', 'шестьдесят',
                                     'семьдесят', 'восемьдесят', 'девяносто')))
SYMS_WORDS_100 = dict(zip(CIFS_0_10, ('ноль', 'сто', 'двести', 'триста',
                                      'четыреста', 'пятьсот', 'шестьсот',
                                      'семьсот', 'восемьсот', 'девятьсот')))
'''
{0: {1: {'male': 'один', 'female': 'одна'}, 2: {'male': 'два', 'female': 'две'}, 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}, 1: {1: 'десять', 2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят', 6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'}, 2: {1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста', 5: 'пятьсот', 6: 'шестьсот', 7: 'семьсот', 8: 'восемьсот', 9: 'девятьсот'}}
'''
POWERS_10_TEXTS = dict(zip((0, 1, 2), (SYMS_WORDS_1_10, SYMS_WORDS_10,
                                       SYMS_WORDS_100)))

# Падежи
CASES = ('imen_sing', 'rod_sing', 'rod_plur')

# Падежи и наборы чисел
CASES_NUMS = {'imen_sing': set(range(1, 100, 10)) - {11},
              'rod_sing': set(map(lambda x: x[0] * 10 + x[1],
                                  product(set(range(10)) - {1}, (2, 3, 4))))}
CASES_NUMS['rod_plur'] = tuple(set(range(0, 1000)) -
                               set(reduce(lambda x, y: x | y,
                                          CASES_NUMS.values())))

# Валюты. Чтобы добавить свою валюту, нужно создать 2 словаря для денежных единиц
# типа {падеж: название единицы в склонении} и добавить в список CURRENCIES объект
# типа Power_1000_Text(lang='<<ключ валюты>>', sex='<<пол>>', power_1000=<<0 или -2>>,
# forms=<<словарь валюты>>). Пример для рублей и копеек - ниже
RUBBLES_FORMS = dict(zip(CASES, ('рубль', 'рубля', 'рублей')))
COPECKS_FORMS = dict(zip(CASES, ('копейка', 'копейки', 'копеек')))
CURRENCIES = [Power_1000_Text(lang='ru', sex='male', power_1000=0,
                              forms=RUBBLES_FORMS),
              Power_1000_Text(lang='ru', sex='male', power_1000=-1.5,
                              forms=COPECKS_FORMS)]

# Степени (x), падежи и текст.форматы чисел типа 1000 ** x (x принадл. N)

MILLIARDS_FORMS = dict(zip(CASES, ('миллиардная', 'миллиардных', 'миллиардных')))
HUNDREDTH_MILLIONTH_FORMS = dict(zip(CASES, ('стомиллионная', 'стомиллионных',
                                     'стомиллионных')))
TENTH_MILLIONTH_FORMS = dict(zip(CASES, ('десятимиллионная', 
                                 'десятимиллионных', 'десятимиллионных')))
MILLIONTH_FORMS = dict(zip(CASES, ('миллионная', 'миллионных', 'миллионных')))
HUNDREDTH_THOUSANDTH_FORMS = dict(zip(CASES, ('стотысячная', 'стотысячных',
                                  'стотысячных')))
TENTH_THOUSANDTH_FORMS = dict(zip(CASES, ('десятитысячная', 'десятитысячных',
                                  'десятитысячных')))
THOUSANDTH_FORMS = dict(zip(CASES, ('тысячная', 'тысячных', 'тысячных')))
HUNDREDTH_FORMS = dict(zip(CASES, ('сотая', 'сотых', 'сотых')))
TENTH_FORMS = dict(zip(CASES, ('десятая', 'десятых', 'десятых')))
POWERS_1000_FRACTIONS_TEXTS = [Power_1000_Text(sex='female', power_1000=0, forms=WHOLES_FORMS),]



WHOLES_FORMS = dict(zip(CASES, ('целая', 'целые', 'целых')))
THOUSANDS_FORMS = dict(zip(CASES, ('тысяча', 'тысячи', 'тысяч')))
MILLIONS_FORMS = dict(zip(CASES, ('миллион', 'миллиона', 'миллионов')))
MILLIARDS_FORMS = dict(zip(CASES, ('миллиард', 'миллиарда', 'миллиардов')))
POWERS_1000_WHOLES_TEXTS = [Power_1000_Text(sex='female', power_1000=0, forms=WHOLES_FORMS),
                     Power_1000_Text(sex='female', power_1000=1, forms=THOUSANDS_FORMS),
                     Power_1000_Text(sex='male', power_1000=2, forms=MILLIONS_FORMS),
                     Power_1000_Text(sex='male', power_1000=3, forms=MILLIARDS_FORMS)]