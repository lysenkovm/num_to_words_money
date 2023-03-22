import math
from itertools import product
from functools import reduce
from string import whitespace
import sys

from main_dictionary import MainDictionary


def get_print(el, row='GP'):
    print(el, row)
    return el


class Digit:  # Разряд
    def __init__(self, part, powers_digit):
        self.part = part
        self.digit_str, self.powers_10 = self.get_digit_powers(powers_digit)
        self.digit_int = int(self.digit_str)
        self.text = self.get_text_forms()
    
    def get_digit_powers(self, powers_digit):
        powers = powers_digit[0]
        return powers_digit[1], dict(powers)
    
    def get_number_in_three(self):
        return self.digit_int * 10 ** self.powers['in_number'][1]  # Число, представляемое разрядом
        
    def get_text_forms(self):
        return MainDictionary.Powers10Words.POWERS_10_WORDS \
               [self.powers_10['in_three'][1]
                ][self.digit_int]
        

class Digits_10:
    def __init__(self, three, digits):
        self.three = three
        # Разряды фильтруются по числовому значению цифры
        self.digits_10 = tuple(sorted((filter(lambda d: d.digit_int, digits)),
                                      key=lambda dig:
                                      dig.powers_10['in_three'][1],
                                      reverse=True))
        if self.digits_10:
            self.number_str, self.number_int = self.get_number()
        else:
            self.number_str, self.number_int = '', 0
        self.text = self.get_text()

    def get_number(self):
        number_int = sum(map(lambda d: d.digit_int * d.powers_10
                             ['in_three'][0] ** d.powers_10['in_three'][1], 
                             self.digits_10))
        number_str = str(number_int)
        return number_str, number_int
    
    def get_text(self):
        if len(self.digits_10):  # Если длина: 1 или 2 символа
            # Если это число от 1 до 20
            if self.number_int in MainDictionary.MainConstants.NUMS_0_20:
                words_forms = (MainDictionary.Powers10Words.SYMS_WORDS_0_20 \
                               [self.number_int],)
                # Если получен словарь (пол: форма_числа)
                # if isinstance(words_forms, dict):
                    # # Получить слово-число по полу
                    # text = words_forms[self.three.sex]
                # else:
                    # # Иначе получить переменную 'text'
                    # text = words_forms
            # Если это !не! число от 1 до 20
            else:
                # Получить список форм числа
                words_forms = tuple(map(lambda d: MainDictionary.Powers10Words.
                                    POWERS_10_WORDS[d.powers_10['in_three'][1]]
                                    [d.digit_int], self.digits_10))
            words = tuple(map(lambda forms: forms[self.three.sex]
                              if isinstance(forms, dict) else forms,
                              words_forms))
            return ' '.join(words)
        else:
            return ''
        
        

class Three:
    def __init__(self, part, three_str, powers_1000):
        self.part = part
        self.three_str = three_str  # '345'
        self.powers_1000 = powers_1000  # {'in_part': (1000, 0)}
        self.len_three = len(self.three_str)  # 3
        self.three_int = int(self.three_str)  # 345
        self.digits = self.get_digits()  # [Digit, Digit, ...]
        self.sex, self.forms = self.get_sex_forms()
        self.digits_10 = Digits_10(self, filter(lambda d: d.powers_10['in_three'][1]
                                                in (0, 1), self.digits))
        if self.three_int:
            self.case = self.get_case()
        self.text = self.get_text()
    
    def get_sex_forms(self):
        if self.powers_1000['in_part'] != (1000, 0):
            source_objs = MainDictionary.Powers1000WholesForms.POWERS_1000_WHOLES_TEXTS
            power = self.powers_1000['in_part']
        else:
            source_objs = self.part.units
            if self.part.part_type == 'int_part':  # ЦЧ
                power = (1000, 0)
            else:
                power = (10, -self.part.len_str)
        obj = tuple(filter(lambda obj: obj.power == power, source_objs))[0]
        sex = obj.sex
        forms = obj.forms
        return sex, forms
    
    def get_case(self):
        case = tuple(filter(lambda item: self.three_int in item[1],
                            MainDictionary.CasesNums.
                            CASES_NUMS.items()))[0][0]
        return case
    
    # По степени 1000 фильтрует все Разряды в Части
    def get_digits(self):
        digits = list(filter(lambda digit: digit.powers_10['in_part'][1] in
                             self.get_digits_range_in_part(),
                             self.part.digits))
        return digits

    # Возвращает диапазон индексов (== ПоказСтеп) Разрядов ('in_part') внутри Тройки
    def get_digits_range_in_part(self):
        return range(self.powers_1000['in_part'][1] * 3,
                     self.powers_1000['in_part'][1] * 3 + 3)
    
    def get_digit_by_idx(self, three_idx):
        if three_idx in range(self.len_three):
            return tuple(filter(lambda d: d.powers_10['in_three'][1] == three_idx,
                                self.digits))[0]
        else:
            return False
    
    def get_text(self):
        # Разряд с индексом 2
        digit_2_text = ''  # Начальное значение, кот.м.б.изменено следующим кодом
        if self.len_three == 3:
            digit_2 = self.get_digit_by_idx(2)
            if digit_2.digit_int:
                digit_2_text = digit_2.text
        # Степень 1000 в текстовом выражении
        if self.three_int:
            unit_name = self.forms[self.case]
        else:
            unit_name = ''
        text_list = [digit_2_text, self.digits_10.text, unit_name]
        text = ' '.join(filter(bool, text_list))
        return text

    def __str__(self):
        return self.text
    


class PartText:
    def __init__(self, number, part_type, part_str):
        self.number = number  # Родительский объект
        self.units = self.get_units()
        
        self.part_type = part_type
        self.part_str = part_str
        self.len_str = len(self.part_str)
        self.len_threes = math.ceil(self.len_str / 3)
        # ['1', '2', '3', '4', '5']
        self.digits = self.get_digits()
        self.threes = self.get_threes()
    
    def get_units(self):
        if self.number.currency_key:
            # Получить список ден.едениц по ключу
            units = list(filter(lambda curr: curr.currency_key ==
                                self.number.currency_key, MainDictionary.
                                Currencies.CURRENCIES))
        else:
            units = [MainDictionary.Powers1000WholesForms.WHOLES_FORMS] + \
                    MainDictionary.Powers10FractionsTexts. \
                    POWERS_10_FRACTIONS_TEXTS
        return units

    # Разряды не фильтруются
    def get_digits(self):
        
        def powered(tuple_, base, power_type):
            return tuple(map(lambda x: (power_type, (base, x)), tuple_))
        
        # Степени 10 в общем числе
        if self.part_type == 'int_part':
            powers_10_in_number = tuple(reversed(range(self.len_str)))
        else:
            powers_10_in_number = tuple(reversed(range(-self.len_str, 0)))
        # Степени 10 в части
        powers_10_in_part = tuple(map(lambda p: (p + self.len_str) % 
                                      self.len_str, powers_10_in_number))
        # Степени 10 в тройке
        powers_10_in_three = tuple(map(lambda p: p % 3, powers_10_in_part))
        
        powers_10_in_number = powered(powers_10_in_number, 10, 'in_number')
        powers_10_in_part = powered(powers_10_in_part, 10, 'in_part')
        powers_10_in_three = powered(powers_10_in_three, 10, 'in_three')
        
        powers = tuple(zip(powers_10_in_number, powers_10_in_part,
                          powers_10_in_three))
        powers_digits = tuple(zip(powers, self.part_str))
        # Фильтрация нулевых разрядов
        # powers_digits = tuple(filter(lambda pd: int(pd[1]), powers_digits))
        return tuple(map(lambda pd: Digit(self, pd), powers_digits))

    def get_threes(self):
        
        def powered(tuple_, base, power_type):
            return tuple(map(lambda x: (power_type, (base, x)), tuple_))
        
        # Степени 1000 в Части
        # кортеж диапазона чисел от 0 в кол-ве троек
        powers_1000_in_part = tuple(range(self.len_threes))
        # кортеж кортежей: (тип_степени, степень (base, exp))
        # (('in_part', (1000, 0)), ('in_part', (1000, 1)))
        powers_1000_in_part = powered(powers_1000_in_part, 1000, 'in_part')
        # кортеж троек разрядов
        # ('345', '12')
        threes_strs = tuple([self.part_str[(self.len_str - 3 * (i + 1))
                                           if i < self.len_threes - 1 else 0:
                                           self.len_str - 3 * i]
                                           for i in range(self.len_threes)])
        # ((('in_part', (1000, 0)), '345'), (('in_part', (1000, 1)), '12'))
        powers_threes = tuple(zip(powers_1000_in_part, threes_strs))
        threes = []
        for p3 in powers_threes:
            # '345'
            three_str = p3[1]
            # {'in_part': (1000, 0)}
            powers_1000 = dict((p3[0],))
            threes.append(Three(self, three_str, powers_1000))
        threes.sort(key=lambda three: three.powers_1000['in_part'][1], reverse=True)
        return threes
    
    def __str__(self):
        # < Временно
        if self.number.currency_key and self.part_type == 'float_part':
            text = f'{self.part_str.lstrip("0")} коп.'
        else:
        # > Временно
            text = ' '.join([str(three) for three in self.threes])
        # На печать возвращается строковое представление списка троек разрядов
        return text


class Number:
    def __init__(self, number_str, currency_key=False, symbol=',', fract_conv=True):
        self.number_str = number_str
        wspaces = set(whitespace + '\xa0') & set(number_str)
        for wspace in wspaces:
            self.number_str = number_str.replace(wspace, '')
        self.symbol = symbol
        self.currency_key = currency_key
        self.fraction_convert = fract_conv
        self.int_str, self.float_str = self.get_int_float_str()
        self.int_, self.float_ = self.get_int_float()

    def get_text(self):
        int_threes = self.int_.threes
        float_threes = self.float_.threes
        return self.__str__()

    def get_int_float_str(self):
        if self.symbol in self.number_str:
            int_str, float_str = self.number_str.split(self.symbol)
        else:
            int_str, float_str = self.number_str, '0'
        if self.currency_key:
            len_float = len(float_str)
            float_str = str(round(int(float_str) / 10 ** (len(float_str) - 2))).zfill(len_float)
        return (int_str, float_str)

    def get_int_float(self):
        return (PartText(self, 'int_part', self.int_str), 
                PartText(self, 'float_part', self.float_str) 
                if int(self.float_str) else '')
            
    def __str__(self):
        # На печать возвращается строка объединенных строковых представлений объектов
        # 'self.int_', 'self.float', разделенных пробелом
        text = ' '.join((str(self.int_), str(self.float_)))
        return text.capitalize()
        
