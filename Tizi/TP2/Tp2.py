import os

# Funcion para calcular comisiones
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

# Funcion para calcular impuestos
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

# Funcion para validar el destinatario
def validar_destinatario(id_destinatario):
    """
    Se comprueba que el destinatario sea valido o este escrito de manera correcta y no este vacio

    Args:
        id_destinatario (string): Id del destinatario

    Returns:
        Booleano: True si la id de destinatario es correcta, False si no lo es o tiene caracteres invalidos
    """
    if not id_destinatario: # Si no esta definido o esta vacio, devuelve False
        return False

    caracteres_validos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-" # Caracteres validos

    for caracter in id_destinatario:
        if caracter not in caracteres_validos:
            return False

    return True

# Funcion para validar moneda
def validar_moneda(codigo_orden):
    """
    Funcion que valida la moneda de la orden

    Args:
        codigo_orden (string): Codigo de orden

    Returns:
        String: Codigo de orden encontrado
    """
    
    monedas_validas = ["ARS", "USD", "EUR", "GBP", "JPY"] # Monedas aceptadas
    moneda_encontrada = None
    contador = 0

    for moneda in monedas_validas:
        if moneda in codigo_orden:
            moneda_encontrada = moneda
            contador += 1

    return moneda_encontrada if contador == 1 else None


# ------------- Inicio -----------------

# Variables para resultados
cant_minvalida = cant_binvalido = cant_oper_validas = 0
suma_mf_validas = 0.0
cant_ARS = cant_USD = cant_EUR = cant_GBP = cant_JPY = 0
suma_mf_ARS = 0
max_diferencia = -1
cod_my = mont_nom_my = mont_fin_my = ""
nom_primer_benef = ""
cant_nom_primer_benef = 0
total_ordenes = 0
archivo = os.path.join(os.path.dirname(__file__), "ordenes25.txt")

with open(archivo, "r") as f: # Abre el archivo en modo lectura
    next(f) # Ignorar la primera línea (timestamp)

    for linea in f: # Recorre todas las lineas del archivo
        total_ordenes += 1

        # Extraer datos de la línea (54 caracteres)
        nombre = linea[0:20].strip()
        id_destinatario = linea[20:30].strip()
        codigo_orden = linea[30:40].strip()
        monto_nominal = int(linea[40:50].strip())
        algo_comision = int(linea[50:52].strip())
        algo_impuesto = int(linea[52:54].strip())
        
        # Guardar primer beneficiario
        if total_ordenes == 1:
            nom_primer_benef = nombre
        # Validar moneda
        moneda = validar_moneda(codigo_orden)

        if moneda is None:
            cant_minvalida += 1
            # Contar para estadísticas de monedas (si es que aparece alguna)
            for m in ["ARS", "USD", "EUR", "GBP", "JPY"]:
                if m in codigo_orden:
                    if m == "ARS":
                        cant_ARS += 1
                    elif m == "USD":
                        cant_USD += 1
                    elif m == "EUR":
                        cant_EUR += 1
                    elif m == "GBP":
                        cant_GBP += 1
                    elif m == "JPY":
                        cant_JPY += 1
                    break
        else:
            # Validar destinatario
            if not validar_destinatario(id_destinatario):
                cant_binvalido += 1
            else:
                cant_oper_validas += 1

                # Calcular comisión y monto base
                comision = calcular_comision(moneda, monto_nominal, algo_comision)
                monto_base = round(monto_nominal - comision, 2)

                # Calcular impuesto y monto final
                impuesto = calcular_impuesto(monto_base, algo_impuesto)
                monto_final = round(monto_base - impuesto, 2)

                        # Acumular para estadísticas
                suma_mf_validas += monto_final

                if moneda == "ARS":
                    cant_ARS += 1
                    suma_mf_ARS += monto_final
                elif moneda == "USD":
                    cant_USD += 1
                elif moneda == "EUR":
                    cant_EUR += 1
                elif moneda == "GBP":
                    cant_GBP += 1
                elif moneda == "JPY":
                    cant_JPY += 1

                # Para todas las órdenes (válidas e inválidas) calcular diferencia nominal-final
        if moneda is not None and validar_destinatario(id_destinatario):
            diferencia = monto_nominal - monto_final
        else:
            # Para órdenes inválidas, asumimos monto_final = 0
            diferencia = monto_nominal

        if diferencia > max_diferencia:
            max_diferencia = diferencia
            cod_my = codigo_orden
            mont_nom_my = monto_nominal
            mont_fin_my = (monto_final if moneda is not None and validar_destinatario(id_destinatario) else 0)

                # Contar apariciones del primer beneficiario
        if nombre == nom_primer_benef:
            cant_nom_primer_benef += 1

        # Calcular porcentaje y promedio
porcentaje = (cant_minvalida + cant_binvalido) * 100 // total_ordenes
promedio = int(suma_mf_ARS // cant_ARS) if cant_ARS > 0 else 0

# Imprimir resultados (formato exigido)
print("(r1) - Cantidad de ordenes invalidas - moneda no autorizada:",cant_minvalida,)
print("(r2) - Cantidad de ordenes invalidas - beneficiario mal identificado:",cant_binvalido)
print("(r3) - Cantidad de operaciones validas:", cant_oper_validas)
print("(r4) - Suma de montos finales de operaciones validas:",round(suma_mf_validas, 2))
print("(r5) - Cantidad de ordenes para moneda ARS:", cant_ARS)
print("(r6) - Cantidad de ordenes para moneda USD:", cant_USD)
print("(r7) - Cantidad de ordenes para moneda EUR:", cant_EUR)
print("(r8) - Cantidad de ordenes para moneda GBP:", cant_GBP)
print("(r9) - Cantidad de ordenes para moneda JPN:", cant_JPY)
print("(r10) - Codigo de la orden de pago con mayor diferencia nominal - final:",cod_my)
print("(r11) - Monto nominal de esa misma orden:", mont_nom_my)
print("(r12) - Monto final de esa misma orden:", mont_fin_my)
print("(r13) - Nombre del primer beneficiario del archivo:", nom_primer_benef)
print("(r14) - Cantidad de veces que apareció ese mismo nombre:",cant_nom_primer_benef)
print("(r15) - Porcentaje de operaciones inválidas sobre el total:", porcentaje)
print("(r16) - Monto final promedio de las ordenes válidas en moneda ARS:",promedio,)


