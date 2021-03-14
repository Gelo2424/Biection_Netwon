import numpy as np
import sympy as sp


def funtions_value(x, function_number):
    # function_number = 1 -> 5x^3 + 2x^2 - 1x - 1
    # function_number = 2 -> 2sin(x) + 2cos(x)
    # function_number = 3 -> 2^x + 3^x - 5
    # function_number = 4 -> 2x^2 + 2^x + 2sin(x) - 2

    if function_number == 1:
        value = horner([5, 2, -1, -1], x)
    elif function_number == 2:
        value = 2 * np.sin(x) + 2 * np.cos(x)
    elif function_number == 3:
        value = 2 ** x + 3 ** x - 5
    elif function_number == 4:
        value = 2 * x ** 2 + 2 ** x + 2 * np.sin(x) - 2
    else:
        value = None
    return value


def funtions_pattern(function_number):
    x = sp.Symbol('x')
    if function_number == 1:
        pattern = 5 * sp.Pow(x, 3) + 2 * sp.Pow(x, 2) - 1 * x - 1
    elif function_number == 2:
        pattern = 2 * sp.sin(x) + 2 * sp.cos(x)
    elif function_number == 3:
        pattern = 2 ** x + 3 ** x - 5
    elif function_number == 4:
        pattern = 2 * x ** 2 + 2 ** x + 2 * sp.sin(x) - 2
    else:
        pattern = None
    return pattern


def horner(factors, x):
    result = factors[0]
    for a in range(1, len(factors)):
        result = result * x + factors[a]
    return result
