import math
from itertools import product
from functools import reduce
from main_constants import MainConstants as MC
# CIFS_0_10 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
# NUMS_0_20 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
# CASES = (imen_sing, rod_sing, rod_plur)
# CurrKey_Sex_Power_Forms: currency_key, sex, power (base, exponent), forms


class CasesNums:
    # Падежи и наборы чисел
    def sum_product(seq1, seq2):
        return set(map(sum, product(seq1, seq2)))

    CIFS_1_101_10_rem11 = set(range(1, 101, 10)) - {11}
    CIFS_0_100_10_rem10 = set(range(0, 100, 10)) - {10}
    HUNDREDS = set(range(0, 1000, 100))

    imen_sing = sum_product(CIFS_1_101_10_rem11, HUNDREDS)
    rod_sing = sum_product(HUNDREDS, sum_product(CIFS_0_100_10_rem10, (2, 3, 4)))
    rod_plur = set(range(1, 1000)) - imen_sing - rod_sing

    CASES_NUMS = {'imen_sing': imen_sing, 'rod_sing': rod_sing,
                  'rod_plur': rod_plur}
