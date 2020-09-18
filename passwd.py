# coding=utf-8
import getpass

p = getpass.getpass(prompt='Введите пароль: ')

if p.lower() == 'kramynina123':
    print('Верный пароль')

else:

    print('Неверный пароль')