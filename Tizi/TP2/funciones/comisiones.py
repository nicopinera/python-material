def calcular_comision(moneda, monto_nominal, algoritmo):
    """
    Calcula la comision en funcion de la moneda, el monto nominal y el algoritmo seleccionado

    Args:
        moneda (string):
        monto_nominal (float):
        algoritmo (int):

    Returns:
        int: Monto Base
    """
    if algoritmo == 1 and moneda == "ARS":
        return round(monto_nominal * 0.09, 2)
    elif algoritmo == 2 and moneda == "USD":
        if monto_nominal < 50000:
            return 0
        elif 50000 <= monto_nominal < 80000:
            return round(monto_nominal * 0.05, 2)
        else:
            return round(monto_nominal * 0.078, 2)
    elif algoritmo == 3 and moneda in ["EUR", "GBP"]:
        comision = 100  # Monto fijo
        if monto_nominal > 25000:
            comision += round(monto_nominal * 0.06, 2)
        return comision
    elif algoritmo == 4 and moneda == "JPY":
        return 500 if monto_nominal <= 100000 else 1000
    elif algoritmo == 5 and moneda == "ARS":
        if monto_nominal < 500000:
            return 0
        else:
            comision = round(monto_nominal * 0.07, 2)
            return min(comision, 50000)
    return 0

def calcular_impuesto(monto_base, algoritmo):
    if algoritmo == 1:
        if monto_base <= 300000:
            return 0
        else:
            excedente = monto_base - 300000
            return round(excedente * 0.25, 2)
    elif algoritmo == 2:
        return 50 if monto_base < 50000 else 100
    elif algoritmo == 3:
        return round(monto_base * 0.03, 2)
    return 0