#2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data (name = None,
               last_name = None,
               date_of_birth = None,
               city = None,
               email = None,
               phone_number = None):
    """
    Вывод строкой данных о пользователе
    :param name: Имя
    :param last_name: Фамилия
    :param date_of_birth: Дата рождения
    :param city: Город
    :param email: Электронная почта
    :param phone_number: Номер телефона
    :return:
    """
    print("{}, {}, {}, {}, {}, {}".format(name, last_name, date_of_birth, city, email, phone_number))

name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
date_of_birth = input('Введите дату рождения: ')
city = input('Введите город: ')
email = input('Введите электронную почту: ')
phone_number = input('Введите номер телефона: ')

user_data(name=name, last_name=last_name,
          date_of_birth=date_of_birth, email=email, phone_number=phone_number, city=city)