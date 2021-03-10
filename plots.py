import matplotlib.pyplot as mp
import numpy as np
from functions import funtions_value
from functions import funtions_pattern


def show_plot(left, right, funtion_number, result_bisection, result_newton):
    x = np.linspace(left, right, 1000)
    mp.plot(x, funtions_value(x, funtion_number))
    mp.plot(result_bisection, 0, '+')
    mp.plot(result_newton, 0, '*')
    mp.title(str(funtions_pattern(funtion_number)))
    mp.ylabel("f(x)")
    mp.xlabel("x")
    mp.grid(True)
    mp.legend(["Wykres funkcji f(x)", "Miejsce zerowe (bisekcja): " + str(result_bisection)
                  , "Miejsce zerowe (newton): " + str(result_newton)], loc="upper left")
    mp.show()
