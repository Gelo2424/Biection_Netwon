from functions import funtions_value
from functions import funtions_pattern
import sympy as sp


def bisection(left, right, eps, iteration, function_number):
    counter = 0
    if funtions_value(left, function_number) * funtions_value(right, function_number) > 0:
        return False
    else:
        if eps != -1:
            xim1 = (left + right) / 2 - 100  # ???
            while True:
                xi = (left + right) / 2
                if abs(xi - xim1) < eps:
                    print("Bisekcja - " + str(counter) + " iteracji")
                    return xi
                elif funtions_value(xi, function_number) * funtions_value(left, function_number) < 0:
                    right = xi
                else:
                    left = xi
                counter += 1
                xim1 = xi
        else:
            xi = (left + right) / 2
            for n in range(iteration):
                if funtions_value(xi, function_number) == 0.0:
                    return xi
                elif funtions_value(xi, function_number) * funtions_value(left, function_number) < 0:
                    right = xi
                else:
                    left = xi
            counter = iteration
            # eps = abs(funtions_value(xi, function_number))
    return xi


def newton(left, right, eps, iteration, function_number):
    counter = 0
    if funtions_value(left, function_number) * funtions_value(right, function_number) > 0:
        return False
    x = sp.Symbol('x')
    df = sp.diff(funtions_pattern(function_number))
    xi = (left + right) / 2
    if eps != -1:
        xim1 = (left + right) / 2 - 100  # ???
        while True:
            fxi = funtions_value(xi, function_number)
            dfx = df.subs(x, xi)
            if abs(xi - xim1) < eps:
                print("Newton - " + str(counter) + " iteracji")
                return xi
            xim1 = xi
            xi = xi - float(fxi / dfx)
            counter += 1

    else:
        for n in range(iteration):
            fxi = funtions_value(xi, function_number)
            dfx = df.subs(x, xi)
            xi = xi - float(fxi / dfx)
        counter = iteration
        # eps = abs(funtions_value(xi, function_number))

    return xi
