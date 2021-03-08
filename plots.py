import matplotlib.pyplot as mp
import numpy as np
from functions import funtions_value
from functions import funtions_pattern


def show_plot(left, right, funtion_number, result, name):
    x = np.linspace(left, right, 1000)
    mp.plot(x, funtions_value(x, funtion_number))
    mp.plot(result, 0, '+')
    mp.title(name + "\n" + str(funtions_pattern(funtion_number)))
    mp.ylabel("f(x)")
    mp.xlabel("x")
    mp.grid(True)
    mp.legend(["Wykres funkcji f(x)", "Miejsce zerowe (bisekcja): " + str(result)], loc="upper left")
    mp.show()
