"""Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_data_collector(**kwargs):
    return kwargs


data_row = user_data_collector(name=input('name: '), surname=input('surname: '), birth_year=int(input('birth_year: ')),
                               birth_city=input('birth_city: '), current_city=input('current_city: '),
                               email=input('email: '), phone_number=input('phone_number: '))
print(data_row)
