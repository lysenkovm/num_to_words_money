# CIFS_0_10 = tuple(0, ..., 9),
# NUMS_0_20 = tuple(0, ..., 19),
# CASES= (imen_sing, rod_sing, rod_plur)
# CurrKey_Sex_Power_Forms: currency_key, sex, power (base, exponent), forms
from main_constants import MainConstants, CurrKey_Sex_Power_Forms


class Powers10FractionsTexts:
    MILLIARDS_FORMS = (-9, dict(zip(MainConstants.CASES,
                                    ('миллиардная', 'миллиардных',
                                     'миллиардных'))))
    HUNDREDTH_MILLIONTH_FORMS = (-8, dict(zip(MainConstants.CASES, 
                                              ('стомиллионная', 'стомиллионных',
                                               'стомиллионных'))))
    TENTH_MILLIONTH_FORMS = (-7, dict(zip(MainConstants.CASES, 
                                          ('десятимиллионная', 'десятимиллионных',
                                           'десятимиллионных'))))
    MILLIONTH_FORMS = (-6, dict(zip(MainConstants.CASES,
                                    ('миллионная', 'миллионных', 'миллионных'))))
    HUNDREDTH_THOUSANDTH_FORMS = (-5, dict(zip(MainConstants.CASES, 
                                               ('стотысячная', 'стотысячных',
                                                'стотысячных'))))
    TENTH_THOUSANDTH_FORMS = (-4, dict(zip(MainConstants.CASES,
                                           ('десятитысячная', 'десятитысячных',
                                            'десятитысячных'))))
    THOUSANDTH_FORMS = (-3, dict(zip(MainConstants.CASES,
                                     ('тысячная', 'тысячных', 'тысячных'))))
    HUNDREDTH_FORMS = (-2, dict(zip(MainConstants.CASES,
                                    ('сотая', 'сотых', 'сотых'))))
    TENTH_FORMS = (-1, dict(zip(MainConstants.CASES,
                                ('десятая', 'десятых', 'десятых'))))
    FRACTIONS_FORMS = [TENTH_FORMS, HUNDREDTH_FORMS, THOUSANDTH_FORMS,
                       TENTH_THOUSANDTH_FORMS, HUNDREDTH_THOUSANDTH_FORMS,
                       MILLIONTH_FORMS, TENTH_MILLIONTH_FORMS,
                       HUNDREDTH_MILLIONTH_FORMS, MILLIARDS_FORMS]
    # [Object: sex, power (base, exponent), forms]
    POWERS_10_FRACTIONS_TEXTS = list(map(lambda fraction_forms:
                                         CurrKey_Sex_Power_Forms
                                         (sex='female',
                                          power=(10, fraction_forms[0]),
                                          forms=fraction_forms[1]),
                                         FRACTIONS_FORMS))
