# CIFS_0_10 = tuple(0, ..., 9),
# NUMS_0_20 = tuple(0, ..., 19),
# CASES = (imen_sing, rod_sing, rod_plur)
# CurrKey_Sex_Power_Forms: currency_key, sex, power (base, exponent), forms
from main_constants import MainConstants, CurrKey_Sex_Power_Forms


# [Object: sex, power (base, exponent), forms] - 1000 ** x (x принадлежит N)
class Powers1000WholesForms:
    # Степени (x), падежи и текст.форматы чисел типа 1000 ** x (x принадл. N)
    WHOLES_FORMS = CurrKey_Sex_Power_Forms(sex='female', power=(1000, 0), 
                                           forms=dict(zip(MainConstants.CASES,
                                           ('целая', 'целые', 'целых'))))
    THOUSANDS_FORMS = dict(zip(MainConstants.CASES, 
                               ('тысяча', 'тысячи', 'тысяч')))
    MILLIONS_FORMS = dict(zip(MainConstants.CASES,
                              ('миллион', 'миллиона', 'миллионов')))
    MILLIARDS_FORMS = dict(zip(MainConstants.CASES,
                               ('миллиард', 'миллиарда', 'миллиардов')))
    TRILLIONS_FORMS = dict(zip(MainConstants.CASES,
                               ('триллион', 'триллиона', 'триллионов')))
    QUADRILLIONS_FORMS = dict(zip(MainConstants.CASES,
                                  ('квадриллион', 'квадриллиона', 'квадриллионов')))
    QUINTILLIONS_FORMS = dict(zip(MainConstants.CASES,
                                  ('квинтиллион', 'квинтиллиона', 'квинтиллионов')))
    SEXTILLIONS_FORMS = dict(zip(MainConstants.CASES,
                                 ('секстиллион', 'секстиллиона', 'секстиллионов')))
    SEPTILLIONS_FORMS = dict(zip(MainConstants.CASES,
                                 ('септиллион	', 'септиллиона', 'септиллионов')))
    POWERS_1000_WHOLES_TEXTS = [WHOLES_FORMS,
                                CurrKey_Sex_Power_Forms
                                (sex='female', power=(1000, 1),
                                 forms=THOUSANDS_FORMS),
                                CurrKey_Sex_Power_Forms
                                (sex='male', power=(1000, 2),
                                 forms=MILLIONS_FORMS),
                                CurrKey_Sex_Power_Forms
                                (sex='male', power=(1000, 3),
                                 forms=MILLIARDS_FORMS),
                                 CurrKey_Sex_Power_Forms
                                (sex='male', power=(1000, 4),
                                 forms=TRILLIONS_FORMS),
                                 CurrKey_Sex_Power_Forms
                                (sex='male', power=(1000, 5),
                                 forms=QUADRILLIONS_FORMS),
                                 CurrKey_Sex_Power_Forms
                                (sex='male', power=(1000, 6),
                                 forms=QUINTILLIONS_FORMS),
                                 CurrKey_Sex_Power_Forms
                                (sex='male', power=(1000, 7),
                                 forms=SEXTILLIONS_FORMS),
                                 CurrKey_Sex_Power_Forms
                                (sex='male', power=(1000, 8),
                                 forms=SEPTILLIONS_FORMS)]
                                 