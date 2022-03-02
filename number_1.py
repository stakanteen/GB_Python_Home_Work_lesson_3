#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division_operation (divisible, divisor):
    """
    Функция деления
    :param divisible: Делимиое
    :param divisor: Делитель
    :return: Результат деления
    """
    if divisor == 0:
        answer = 'На ноль делить нельзя, измените делитель'
    else:
        answer = divisible/divisor
    return answer

divisible = float(input('Введите делимое: '))
divisor = float(input('Введите делитель: '))
answer = division_operation(divisible, divisor)
print('Ответ: ', answer)