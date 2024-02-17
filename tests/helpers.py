import random


def correct_login_and_password():
    login_lst = []
    name = f'andrew_5_{random.randint(100, 999)}'
    login = f'{name}@ya.ru'
    login_lst.append(name)
    login_lst.append(login)
    login_lst.append(str(random.randint(100000, 999999)))
    return login_lst
