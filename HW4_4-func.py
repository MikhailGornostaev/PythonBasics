from HW4_lib import converter_inf

while True:
    yourCur = input("Выберите валюту из ['USD','EUR','CHF','GBP','CNY']: ")
    yourMoney = input('Введите сумму в рублях: ')
    converter_inf(yourCur, yourMoney)
