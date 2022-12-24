"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [i**2 for i in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    k = 0
    for i in range(1, n+1):
        if n % i == 0:
            k += 1
    if k == 2:
        return True
    return False


def filter_numbers(sp, param):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if param == ODD:
        return list(filter(lambda x: x % 2 == 1, sp))
    if param == EVEN:
        return list(filter(lambda x: x % 2 == 0, sp))
    if param == PRIME:
        return list(filter(is_prime, sp))
