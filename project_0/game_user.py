"""Функция для поиска загаданного числа
"""


def middle_predict(number:int=1) -> int:
    """Угадываем число "от середины"

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    n = 100 # максимум для загаданного числа
    predict_number = n/2 # число для сравнения с загаданным
    while True:
        count += 1
        n = int((n+1) / 2)  # корректировка коэффициента
        if predict_number > number: # если больше загаданного,
           predict_number -= n      # то вычитаем коэффициент
        elif predict_number < number:
           predict_number += n
        else: break # если угадали, заканчиваем цикл
    return(count)