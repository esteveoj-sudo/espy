import numpy as np
import matplotlib.pyplot as plt

def method(x0, xn, y0, h, f, metode="Euler"):  # metode com a paràmetre
    x = np.arange(x0, xn + h, h)
    y = np.zeros(len(x))
    y[0] = y0

    if metode == "Euler":
        for i in range(1, len(x)):
            y[i] = y[i-1] + h * f(x[i-1], y[i-1])

    elif metode == "Heun":
        for i in range(1, len(x)):
            # Predictor (Euler)
            y_predictor = y[i-1] + h * f(x[i-1], y[i-1])
            # Corrector (Heun)
            y[i] = y[i-1] + (h/2) * (f(x[i-1], y[i-1]) + f(x[i], y_predictor))

    else:
        raise ValueError(f"Mètode '{metode}' no reconegut. Usa 'Euler' o 'Heun'")

    return x, y
