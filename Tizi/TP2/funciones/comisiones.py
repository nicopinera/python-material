def calcular_comision(moneda, monto_nominal, algoritmo):
    """
    Calcula la comision en funcion de la moneda, el monto nominal y el algoritmo seleccionado

    Args:
        moneda (string):
        monto_nominal (float):
        algoritmo (int):

    Returns:
        int: comision
    """
    comision = 0 

    if algoritmo == 1 and moneda == "ARS":
        comision = monto_nominal * 0.09

    elif algoritmo == 2 and moneda == "USD":
        if monto_nominal < 50000:
            comision = 0
        elif 50000 <= monto_nominal < 80000:
            comision = monto_nominal * 0.05
        else:
            comision = monto_nominal * 0.078

    elif algoritmo == 3 and moneda in ["EUR", "GBP"]:
        comision = 100  # Monto fijo
        if monto_nominal > 25000:
            comision += monto_nominal * 0.06

    elif algoritmo == 4 and moneda == "JPY":
        comision = 500 if monto_nominal <= 100000 else 1000

    elif algoritmo == 5 and moneda == "ARS":

        if monto_nominal >= 500000:
            comision = monto_nominal * 0.07
            if comision > 50000:
                comision = 50000

    return round(comision, 2)

def calcular_impuesto(monto_base, algoritmo):
    """
    Calcula el impuesto a cobrar en funcion del munto base y el algoritmo

    Args:
        monto_base (float):
        algoritmo (int):

    Returns:
        int: impuesto
    """
    impuesto = 0

    if algoritmo == 1:
        if monto_base > 300000:
            excedente = monto_base - 300000
            impuesto = excedente * 0.25
    elif algoritmo == 2:
        impuesto = 50 if monto_base < 50000 else 100
    elif algoritmo == 3:
        impuesto = monto_base * 0.03

    return round(impuesto, 2)