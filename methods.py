from functions import funtions_value
from functions import funtions_pattern
import sympy as sp


# metoda bisekcji, przyjmuje lewy i prawy kraniec przedziału, dokładność, liczbe iteracji i numer funkcji
def bisection(left, right, eps, iteration, function_number):
    counter = 0  # licznik pętli
    # założenie, jeżeli na krańcach przedziału są te same znaki to nie możemy korzystać z metody bisekcji
    if funtions_value(left, function_number) * funtions_value(right, function_number) > 0:
        return False
    else:
        if eps != -1:  # jeżeli eps nie jest -1 to używamy go jako warunek stopu
            xim1 = (left + right) / 2 - 100  # xi - 1
            while True:
                xi = (left + right) / 2
                if abs(xi - xim1) < eps:  # warunek stopu
                    print("Bisekcja - " + str(counter) + " iteracji")
                    return xi
                elif funtions_value(xi, function_number) * funtions_value(left, function_number) < 0:
                    right = xi
                else:
                    left = xi
                counter += 1
                xim1 = xi
        else:  # warunek stopu, liczba iteracji
            xi = 0
            for n in range(iteration):
                xi = (left + right) / 2
                if funtions_value(xi, function_number) == 0.0:
                    print("Bisekcja - znaleziono rozwiazanie po " + str(n + 1) + " iteracjach")
                    return xi
                elif funtions_value(xi, function_number) * funtions_value(left, function_number) < 0:
                    right = xi
                else:
                    left = xi
            eps = abs(funtions_value(xi, function_number))
            print("Bisekcja - znaleziono rozwiazanie po " + str(iteration) + " iteracjach z dokladnoscia " + str(eps))
            return xi


def newton(left, right, eps, iteration, function_number):
    counter = 0
    if funtions_value(left, function_number) * funtions_value(right, function_number) > 0:
        return False
    x = sp.Symbol('x')
    df = sp.diff(funtions_pattern(function_number))
    dff = sp.diff(df)
    if df.subs(x, left) * df.subs(x, right) < 0 or dff.subs(x, left) * dff.subs(x, right) < 0:
        return False
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
            if funtions_value(xi, function_number) == 0.0:
                print("Netwon - znaleziono rozwiazanie po " + str(n + 1) + " iteracjach")
                return xi

        eps = abs(funtions_value(xi, function_number))
        print(eps)
        print("Newton - znaleziono rozwiazanie po " + str(iteration) + " iteracjach z dokladnoscia " + str(eps))

    return xi
