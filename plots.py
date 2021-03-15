import matplotlib.pyplot as mp
import numpy as np
from functions import funtions_value
from functions import funtions_pattern


def show_plot(left, right, funtion_number, result_bisection, result_newton):
    x = np.linspace(left, right, 1000)  # oś OX od lewego do prawego przedziału, 1000 wartości
    mp.plot(x, funtions_value(x, funtion_number))  # rysowanie wykresu
    mp.plot(result_bisection, 0, '+')  # miejsce zerowe wyliczone za pomocą bisekcji
    mp.plot(result_newton, 0, '*')  # miejsce zerowe wyliczone za pomocą netwona
    mp.title(str(funtions_pattern(funtion_number)))  # tytuł
    mp.ylabel("f(x)")  # nazwa osi OY
    mp.xlabel("x")  # nazwa osi OX
    mp.grid(True)  # siatka
    # legenda wykresu
    mp.legend(["Wykres funkcji f(x)", "Miejsce zerowe (bisekcja): " + str(result_bisection)
                  , "Miejsce zerowe (newton): " + str(result_newton)], loc="upper left")
    mp.show()
