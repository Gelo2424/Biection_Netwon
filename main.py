from functions import funtions_value
from functions import funtions_pattern
from methods import bisection
from methods import newton
from plots import show_plot
import sympy as sp

# =========================== #
#   Grzegorz Kucharski 229932 #
#   Wojciech Cwynar           #
#   Grupa 5                   #
# =========================== #

while True:
    correct = False
    function_number = 0
    while correct is not True:
        print("""\nWybierz numer funkcji:
        1 - wielomianowa: 5x^3 + 2x^2 - 1x - 1
        2 - trygonometryczna: 2sin(x) + 2cos(x)
        3 - wykładnicza: 2^x + 3^x - 5
        4 - złożona: 2x^2 + 2^x + 2sin(x) - 2""")
        try:
            function_number = int(input())
            if 0 < function_number < 5:
                correct = True
            else:
                print("Bledny numer funkcji")
                correct = False
        except ValueError:
            print("Bledny numer funkcji")

    correct = False
    left = 0
    right = 0
    while correct is not True:
        print("\nOkresl przedział poszukiwań")
        try:
            left = int(input("Podaj lewy przedzial: "))
            right = int(input("Podaj prawy przedzial: "))
            if left > right:
                print("Bledny przedzial")
            else:
                correct = True
        except ValueError:
            print("Bledny przedzial")

    correct = False
    stop_condition = 0
    while correct is not True:
        print("""\nWybierz kryterium zatrzymania
        1 - Dokładność
        2 - iteracja""")
        try:
            stop_condition = int(input())
            if 0 < stop_condition < 3:
                correct = True
            else:
                print("Brak takiego kryterium")
        except ValueError:
            print("Brak takiego kryterium")

    accuracy = 0
    iteration = 0
    if stop_condition == 1:
        accuracy = abs(float(input("Podaj dokładność epsilon: ")))
        iteration = -1
    else:
        iteration = int(input("Podaj liczbe iteracji: "))
        accuracy = -1

    result_bisection = bisection(left, right, accuracy, iteration, function_number)
    result_newton = newton(left, right, accuracy, iteration, function_number)

    if result_bisection is False:
        print("Bisekcja: Funkcja nie spełnia założeń na danym przedziale")
    else:
        print(result_bisection)

    if result_newton is False:
        print("Newton: Funkcja nie spełnia założeń na danym przedziale")
    else:
        print(result_newton)

    show_plot(left, right, function_number, result_bisection, result_newton)
