import num_to_words_money
import pyperclip


def main():
    if __name__ == '__main__':
        print(79 * '*')
        print('''Приложение - конвертер числового представления суммы денежных
средств в виде текста''')
        print(79 * '*')
        invitation = 'Введите число, дробная часть которого не более 2-х' + \
                     ' разрядов\n' + \
                     '(Разделитель - запятая ",". Допускаются пробелы.): ' + \
                     'Ппример: 17,38\nВвод: '
        n = input(invitation).replace(' руб.', '')
        num = num_to_words_money.Number(number_str=n, currency_key='ru',
                                        symbol=',', fract_conv=False)
        # test
        num = str(num)
        # test
        return f'{n} руб. ({num})'


while True:
    n = main()
    print(n)
    pyperclip.copy(n)
    print('Результат скопирован в буфер обмена')
    
