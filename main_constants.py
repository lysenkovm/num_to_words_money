# CIFS_0_10 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
# NUMS_0_20 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
# CASES = (imen_sing, rod_sing, rod_plur)
# CurrKey_Sex_Power_Forms: currency_key, sex, power (base, exponent), forms
class MainConstants:
    # цифры от 1 до 9
    CIFS_0_10 = tuple(range(0, 10))
    # Числовой и текст.формат чисел от 1 до 20
    NUMS_0_20 = tuple(range(0, 20))
    # Падежи
    CASES = ('imen_sing', 'rod_sing', 'rod_plur')


class CurrKey_Sex_Power_Forms:
    # currency_key, sex, power (base, exponent), forms
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.currency_key = self.get_kwarg('currency_key')
        self.sex = self.get_kwarg('sex')
        self.power = self.get_kwarg('power')  # (base, exponent)
        self.forms = self.get_kwarg('forms')
    
    def get_kwarg(self, kwarg_name, alter=False):
        if kwarg_name in self.kwargs:
            return self.kwargs[kwarg_name]
        else:
            return alter