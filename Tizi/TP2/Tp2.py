from moneda import validar_moneda
from destinatario import validar_destinatario
from comisiones import calcular_comision
from comisiones import calcular_impuesto

def main():
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
    archivo = "ordenes25.txt"
    try:
        with open(archivo, "r") as f:
            next(f) # Ignorar la primera línea (timestamp)

            for linea in f:
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
                        comision = calcular_comision(
                            moneda, monto_nominal, algo_comision
                        )
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
                    mont_fin_my = (
                        monto_final
                        if moneda is not None and validar_destinatario(id_destinatario)
                        else 0
                    )

                # Contar apariciones del primer beneficiario
                if nombre == nom_primer_benef:
                    cant_nom_primer_benef += 1

        # Calcular porcentaje y promedio
        porcentaje = (cant_minvalida + cant_binvalido) * 100 // total_ordenes
        promedio = int(suma_mf_ARS // cant_ARS) if cant_ARS > 0 else 0

        # Imprimir resultados (formato exigido)
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
        print("Error: El archivo 'ordenes.txt' no se encuentra en el directorio.")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")


if __name__ == "__main__":
    main()
