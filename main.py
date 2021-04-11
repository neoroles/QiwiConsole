import pyqiwi
import os
import time
print('╭━━━╮╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╭╮')
print('┃╭━╮┃╱╱╱╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱┃┃')
print('┃┃╱┃┣┳╮╭╮╭┳┫┃╱╰╋━━┳━╮╭━━┳━━┫┃╭━━╮')
print('┃┃╱┃┣┫╰╯╰╯┣┫┃╱╭┫╭╮┃╭╮┫━━┫╭╮┃┃┃┃━┫')
print('┃╰━╯┃┣╮╭╮╭┫┃╰━╯┃╰╯┃┃┃┣━━┃╰╯┃╰┫┃━┫')
print('╰━━╮┣╯╰╯╰╯╰┻━━━┻━━┻╯╰┻━━┻━━┻━┻━━╯')
print('╱╱╱╰╯')


print('Разработчик - AmyTea (Или Booter. Кому как удобно :) )')
print('GitHub - https://github.com/AmyTea-code')
print('Донатик - https://www.donationalerts.com/r/amytea')


q = input('Введите токен! ')
a = int(input('Введите номер телефона! +'))

try:
    wallet = pyqiwi.Wallet(token = q, number = a)
    os.system('cls||clear')
except:
    print('Номер или токен неправильный!')
    exit()









while True:
    ass = input(f'Дроброе утро! Ваш баланс - {wallet.balance()} рубля. Что хотите сделать? \n 1 - Перевести деньги (не qiwi) \n 2 - Перевести деньги (qiwi) \n 3 - идентификация кошелька \n 4 - Создать ссылку оплаты \n 5 - Пополнить деньги на мобильный \n ')


#Перевод на карту
    try:
        if ass == '1':
            pid = int(input('Введите id вашего оператора (Узнать можно здесь - https://developer.qiwi.com/ru/qiwi-wallet-personal/#payments): '))
            recipient = int(input('Введите номер телефона или номер карты / счета получателя: '))
            amount = float(input('Введите сумму, которое хотите отправить: '))
            if amount <1:
                print('Нельзя отправить сумму меньше рубля.')
                time.sleep(4)
                os.system('cls||clear')
            else:
                wallet.send(pid, recipient, amount)
                print('Платеж отправлен!')
                time.sleep(3)
                os.system('cls||clear')
                
    except:
        print('Ошибка! Проверьте правильность данных! Или проверьте уровень вашей идентификации!')
        time.sleep(4)
        os.system('cls||clear')

#Отправка деняг
    if ass == '2':
        try:
            account = int(input('Введите номер телефона аккаунта: +'))
            if account == a:
                print('Нельзя отправить деньги самому себе')
                time.sleep(3)
                os.system('cls||clear')
            amount = int(input('Введите сумму: '))
            if amount <1:
                print('Нельзя отправить сумму меньше нуля!')
                time.sleep(3)
                os.system('cls||clear')
            else:
                wallet.qiwi_transfer(account, amount)
                print('Платеж отправлен!')
                time.sleep(3)
                os.system('cls||clear')
        except:
            print('Произошла ошибка! Пожалуйста, убедитесь, что ввели всё правильно и что ваш уровень верификации выше минимального!')
            time.sleep(3)
            os.system('cls||clear')



    if ass == '3':
        try:
            birth_date = str(input('Введите дату рождения формата "ГГГГ-ММ-ДД": '))
            first_name = str(input('Введите ваше имя: '))
            middle_name = str(input('Введите отчество: '))
            last_name = str(input('Введите вашу фамилию: '))
            passport = str(input('Серия и номер паспорта (Только цифры): '))
            wallet.identification(birth_date, first_name, middle_name, last_name, passport, inn=None, snils=None, oms=None)
            print('Верификация успешно пройдена!')
            time.sleep(3)
            os.system('cls||clear')
        except:
            print('Ошибка! Проврьте правильность данных!')
            time.sleep(3)
            os.system('cls||clear')
            
    if ass == '4':
        try:
            a = str(input('ID провайдера (Узнать можно здесь - https://developer.qiwi.com/ru/qiwi-wallet-personal/#payments): '))
            b = str(input('Счет получателя: '))
            c = float(input('Сумма платежа: '))
            if c <1:
                print('Нельзя!!!')
            d = str(input('Комментарий: '))
            os.system('cls||clear')
            print(f'Ваша ссылка - {pyqiwi.generate_form_link(a, b, c, d)}')
        except:
            print('Ошибка! Проверьте правильность данных!')
            time.sleep(3)
            os.system('cls||clear')
    #pyqiwi.detect_mobile
    if ass == '5':
        try:
            one = str(input('Введите номер телефона: '))
            two = float(input('Введите сумму платежа: '))
            if two <1:
                print('Нельзя переводить меньше нуля!')
                time.sleep(3)
                os.system('cls||clear')
            else:
                accept = input(f'Подтвердите информацию! {one} - номер телефона, {two} - сумма платежа. Всё правильно? Y/N \n')
                if accept == 'Y':
                    wallet.mobile(one, two)
                    print('Операция проведена!')
                    time.sleep(3)
                    os.system('cls||clear')
                if accept == 'N':
                    print('Операция отменена!')
                    time.sleep(3)
                    os.system('cls||clear')
                
        except:
            print('Ошибка! Проверьте ваш стаутс верификации!')
            time.sleep(3)
            os.system('cls||clear')
