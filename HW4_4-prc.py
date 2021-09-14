import re
availableCur = ['USD', 'EUR', 'CHF', 'GBP', 'CNY']

while True:
    yourCur = input("Выберите валюту из ['USD','EUR','CHF','GBP','CNY']: ")
    if yourCur in availableCur:
        yourMoney = input('Введите сумму (RUB): ')
        if yourMoney.startswith('-'):
            print('Введите положительное число.')
        elif re.search(r'[!@#$%^&*()\[\]=+;\'{}\"/A-Za-z]', yourMoney):
            print('Вы ввели не число.')
        elif yourMoney == '':
            print('Вы ввели пустое поле. Введите число.')
        else:
            yourMoney = int(float(yourMoney))

            print('Вы ввели сумму', yourMoney, '(RUB)')

            if yourCur == 'USD':
                toUsd = yourMoney / 73
                print('Конвертированная сумма в USD =', int(toUsd))
            elif yourCur == 'EUR':
                toEur = yourMoney / 86
                print('Конвертированная сумма в EUR =', int(toEur))
            elif yourCur == 'CHF':
                toChf = yourMoney / 79
                print('Конвертированная сумма в CHF =', int(toChf))
            elif yourCur == 'GBP':
                toGbp = yourMoney / 101
                print('Конвертированная сумма в GBP =', int(toGbp))
            else:
                toCny = yourMoney / 11
                print('Конвертированная сумма в CNY =', int(toCny))

    else:
        print('Валюта не поддерживается')
