import re


def converter(money):
    if money.startswith('-'):
        print('Введите положительное число.')
    elif re.search(r'[!@#$%^&*()\[\]=+;\'{}\"/A-Za-z]', money):
        print('Вы ввели не число.')
    elif money == '':
        print('Вы ввели пустое поле. Введите число.')
    else:
        money = int(float(money))

        print('Ты ввёл', money, '(RUB)')

        to_usd = money / 73
        to_eur = money / 86
        to_chf = money / 79
        to_gbp = money / 101
        to_cny = money / 11

        print('Конвертированная сумма в USD =', int(to_usd))
        print('Конвертированная сумма в EUR =', int(to_eur))
        print('Конвертированная сумма в CHF =', int(to_chf))
        print('Конвертированная сумма в GBP =', int(to_gbp))
        print('Конвертированная сумма в CNY =', int(to_cny))


availableCur = ['USD', 'EUR', 'CHF', 'GBP', 'CNY']


def converter_inf(your_cur, your_money):
    if your_cur in availableCur:
        if your_money.startswith('-'):
            print('Введите положительное число.')
        elif your_money.isalpha() or re.search(r'[!@#$%^&*()\[\]=+;\'{}\"/A-Za-z]', your_money):
            print('Вы ввели не число.')
        elif your_money == '':
            print('Вы ввели пустое поле. Введите число.')
        else:
            your_money = int(float(your_money))

            print('Вы ввели сумму', your_money, '(RUB)')

            if your_cur == 'USD':
                to_usd = your_money / 73
                print('Конвертированная сумма в USD =', int(to_usd))
            elif your_cur == 'EUR':
                to_eur = your_money / 86
                print('Конвертированная сумма в EUR =', int(to_eur))
            elif your_cur == 'CHF':
                to_chf = your_money / 79
                print('Конвертированная сумма в CHF =', int(to_chf))
            elif your_cur == 'GBP':
                to_gbp = your_money / 101
                print('Конвертированная сумма в GBP =', int(to_gbp))
            else:
                to_cny = your_money / 11
                print('Конвертированная сумма в CNY =', int(to_cny))
    else:
        print('Валюта не поддерживается')
