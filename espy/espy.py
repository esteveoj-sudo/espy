import numpy as np

def method(x0, xn, y0, h, f, metode="Euler"):
    """
    Resol una EDO amb mètode d'Euler o Heun
    
    Paràmetres:
    -----------
    x0 : float
        Valor inicial de x
    xn : float
        Valor final de x
    y0 : float
        Condició inicial y(x0)
    h : float
        Mida del pas
    f : function
        Funció f(x,y) de l'EDO y' = f(x,y)
    metode : str
        "Euler" o "Heun"
    
    Retorna:
    --------
    x : np.array
        Valors de x
    y : np.array
        Valors de y aproximats
    """
    x = np.arange(x0, xn + h, h)
    y = np.zeros(len(x))
    y[0] = y0
    
    if metode == "Euler":
        for i in range(1, len(x)):
            y[i] = y[i-1] + h * f(x[i-1], y[i-1])
    
    elif metode == "Heun":
        for i in range(1, len(x)):
            y_predictor = y[i-1] + h * f(x[i-1], y[i-1])
            y[i] = y[i-1] + (h/2) * (f(x[i-1], y[i-1]) + f(x[i], y_predictor))
    
    else:
        raise ValueError(f"Mètode '{metode}' no reconegut. Usa 'Euler' o 'Heun'")
    
    return x, y
