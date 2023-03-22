import math
from itertools import product
from functools import reduce


class MainDictionary:
    # CIFS_0_10 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    # NUMS_0_20 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
    # CASES= (imen_sing, rod_sing, rod_plur)
    # CurrKey_Sex_Power_Forms: currency_key, sex, power (base, exponent), forms
    from main_constants import MainConstants

    # {Степень 10-ти: {Число: {Пол: Число_слово} | Число_слово}}
    from wholes_powers_10_words import Powers10Words  # SYMS_WORDS_0_20, POWERS_10_WORDS

    # {imen_sing: tuple(int, int, ...),
    #  rod_sing: tuple(int, int, ...),
    #  rod_plur: tuple(int, int, ...)}
    from cases_nums import CasesNums  # CASES_NUMS

    # [Object: sex, power (base, exponent), forms]
    from fractions_words import Powers10FractionsTexts  # POWERS_10_FRACTIONS_TEXTS

    # [Object: currency_key, sex, power (base, exponent), forms]
    from currencies import Currencies  # CURRENCIES

    # [Object: sex, power (base, exponent), forms] - 1000 ** x (x принадлежит N)
    from Powers_1000_Wholes_Words import Powers1000WholesForms  # POWERS_1000_WHOLES_TEXTS
