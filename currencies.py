# CIFS_0_10 = tuple(0, ..., 9),
# NUMS_0_20 = tuple(0, ..., 19),
# CASES= (imen_sing, rod_sing, rod_plur)
# CurrKey_Sex_Power_Forms: currency_key, sex, power (base, exponent), forms
from main_constants import MainConstants, CurrKey_Sex_Power_Forms


class Currencies:
    RUBBLES_FORMS = dict(zip(MainConstants.CASES, ('рубль', 'рубля', 'рублей')))
    COPECKS_FORMS = dict(zip(MainConstants.CASES, ('копейка', 'копейки', 'копеек')))
    # [Object: currency_key, sex, power (base, exponent), forms]
    CURRENCIES = [CurrKey_Sex_Power_Forms(currency_key='ru', sex='male',
                                          power=(1000, 0), forms=RUBBLES_FORMS),
                  CurrKey_Sex_Power_Forms(currency_key='ru', sex='female',
                                          power=(10, -2), forms=COPECKS_FORMS)]