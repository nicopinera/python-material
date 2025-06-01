def validar_moneda(codigo_orden):
    """
    Funcion que valida la moneda de la orden

    Args:
        codigo_orden (string): Codigo de orden

    Returns:
        String: Codigo de orden encontrado
    """

    # Monedas aceptadas
    monedas_validas = ["ARS", "USD", "EUR", "GBP", "JPY"]
    moneda_encontrada = None
    contador = 0

    for moneda in monedas_validas:
        if moneda in codigo_orden:
            moneda_encontrada = moneda
            contador += 1

    return moneda_encontrada if contador == 1 else None