def validar_moneda(codigo_orden):
    monedas_validas = ["ARS", "USD", "EUR", "GBP", "JPY"]
    moneda_encontrada = None
    contador = 0

    for moneda in monedas_validas:
        if moneda in codigo_orden:
            moneda_encontrada = moneda
            contador += 1

    return moneda_encontrada if contador == 1 else None


def validar_destinatario(id_destinatario):
    if not id_destinatario:
        return False

    caracteres_validos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-"

    for caracter in id_destinatario:
        if caracter not in caracteres_validos:
            return False

    return True


def calcular_comision(moneda, monto_nominal, algoritmo):
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


def main():
    # Variables para resultados
    cant_minvalida = cant_binvalido = cant_oper_validas = 0
    suma_mf_validas = 0.0
    cant_ARS = cant_USD = cant_EUR = cant_GBP = cant_JPY = 0
    suma_mf_ARS = 0
    max_diferencia = -1
    cod_my = ""
    mont_nom_my = 0
    mont_fin_my = 0
    nom_primer_benef = ""
    cant_nom_primer_benef = 0
    total_ordenes = 0
    ordenes_ARS_validas = []

    try:
        with open("ordenes25.txt", "r", encoding="utf-8") as f:
            # Leer todas las líneas primero
            lineas = f.readlines()

            # Procesar primera línea (timestamp)
            if lineas:
                primera_linea = lineas[0]
                # Extraer primer beneficiario de la segunda línea
                if len(lineas) > 1:
                    segunda_linea = lineas[1]
                    nom_primer_benef = segunda_linea[0:20].strip()

            # Procesar órdenes (empezando desde la segunda línea)
            for linea in lineas[1:]:
                linea = linea.rstrip("\n")

                if len(linea) < 54:
                    continue

                total_ordenes += 1

                # Extraer datos de la línea
                nombre = linea[0:20].strip()
                id_destinatario = linea[20:30].strip()
                codigo_orden = linea[30:40].strip()

                try:
                    monto_str = linea[40:50].strip()
                    algo_comision_str = linea[50:52].strip()
                    algo_impuesto_str = linea[52:54].strip()

                    monto_nominal = int(monto_str) if monto_str else 0
                    algo_comision = int(algo_comision_str) if algo_comision_str else 0
                    algo_impuesto = int(algo_impuesto_str) if algo_impuesto_str else 0
                except ValueError:
                    continue

                # Validar moneda
                moneda = validar_moneda(codigo_orden)

                # Contar monedas (para r5-r9)
                if moneda == "ARS":
                    cant_ARS += 1
                elif moneda == "USD":
                    cant_USD += 1
                elif moneda == "EUR":
                    cant_EUR += 1
                elif moneda == "GBP":
                    cant_GBP += 1
                elif moneda == "JPY":
                    cant_JPY += 1
                else:
                    cant_minvalida += 1
                    continue

                # Validar destinatario
                if not validar_destinatario(id_destinatario):
                    cant_binvalido += 1
                    continue

                # Si llegamos aquí, la orden es válida
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
                    suma_mf_ARS += monto_final
                    ordenes_ARS_validas.append(monto_final)

                # Calcular diferencia para máxima diferencia
                diferencia = monto_nominal - monto_final
                if diferencia > max_diferencia:
                    max_diferencia = diferencia
                    cod_my = codigo_orden
                    mont_nom_my = monto_nominal
                    mont_fin_my = monto_final

                # Contar apariciones del primer beneficiario
                if nombre == nom_primer_benef:
                    cant_nom_primer_benef += 1

        # Calcular porcentaje y promedio
        porcentaje = (
            (cant_minvalida + cant_binvalido) * 100 // total_ordenes
            if total_ordenes > 0
            else 0
        )

        # Cálculo especial del promedio ARS (usando división normal para precisión)
        if ordenes_ARS_validas:
            promedio = int(sum(ordenes_ARS_validas) / len(ordenes_ARS_validas))
        else:
            promedio = 0

        # Imprimir resultados
        print(
            "(r1) - Cantidad de ordenes invalidas - moneda no autorizada:",
            cant_minvalida,
        )
        print(
            "(r2) - Cantidad de ordenes invalidas - beneficiario mal identificado:",
            cant_binvalido,
        )
        print("(r3) - Cantidad de operaciones validas:", cant_oper_validas)
        print(
            "(r4) - Suma de montos finales de operaciones validas:",
            round(suma_mf_validas, 2),
        )
        print("(r5) - Cantidad de ordenes para moneda ARS:", cant_ARS)
        print("(r6) - Cantidad de ordenes para moneda USD:", cant_USD)
        print("(r7) - Cantidad de ordenes para moneda EUR:", cant_EUR)
        print("(r8) - Cantidad de ordenes para moneda GBP:", cant_GBP)
        print("(r9) - Cantidad de ordenes para moneda JPN:", cant_JPY)
        print(
            "(r10) - Codigo de la orden de pago con mayor diferencia nominal - final:",
            cod_my,
        )
        print("(r11) - Monto nominal de esa misma orden:", mont_nom_my)
        print("(r12) - Monto final de esa misma orden:", mont_fin_my)
        print("(r13) - Nombre del primer beneficiario del archivo:", nom_primer_benef)
        print(
            "(r14) - Cantidad de veces que apareció ese mismo nombre:",
            cant_nom_primer_benef,
        )
        print("(r15) - Porcentaje de operaciones inválidas sobre el total:", porcentaje)
        print(
            "(r16) - Monto final promedio de las ordenes válidas en moneda ARS:",
            promedio,
        )

    except FileNotFoundError:
        print("Error: El archivo 'ordenes25.txt' no se encuentra en el directorio.")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")


if __name__ == "__main__":
    main()
