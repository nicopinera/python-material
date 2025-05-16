num = 2**14
f_osc = 32768
f_ins = f_osc/4
t_instruccion = 1/f_ins
prescaler = 4
tiempo = t_instruccion * prescaler * ((2**16) - num)
print(tiempo)
"""
nombre = input('ingrese nombre del beneficiario: ')
codigo = input('ingrese el codigo ISO: ')
monto = int(input('ingrese el monto nominal: '))
monto_base = 0
moneda = 0
if 'ARS' in codigo:

    if monto <= 50000:
        n = round(monto * 5 / 100, 2)
    else:
        if monto <= 200000:
            n = round(monto * 3.71 / 100, 2)
        else:
            if monto <= 500000:
                n = round(monto * 2.25 / 100, 2)
            else:
                n = round(monto * 1.8 / 100, 2)

    if monto >= 30000:
        n += 4000
    if n > 300000:
        monto_base = monto - 300000
        moneda = 'ARS'
    else:
        monto_base = monto - n
        moneda = 'ARS'

else:
    if 'USD' in codigo:
        n = round(monto * 7 / 100, 2)
        monto_base = monto - n
        moneda = 'USD'
    else:
        if 'EUR' in codigo:
            n = round(monto * 7 / 100, 2)
            monto_base = monto - n
            moneda = 'EUR'
        else:
            if 'GBP' in codigo:
                n = round(monto * 9 / 100, 2)
                monto_base = monto - n
                moneda = 'GBP'
            else:
                if 'JPY' in codigo:
                    n = round(monto * 9 / 100, 2)
                    monto_base = monto - n
                    moneda = 'JPY'
                else:
                    print('Moneda no valida')
if monto > 500000:
    R = monto * 21 / 100
    monto_final = round(monto_base - R, 2)
else:
    monto_final = monto_base
print("Beneficiario:", nombre)
print("Moneda:", moneda)
print("Monto base (descontadas las comisiones):", monto_base)
print("Monto final (descontados los impuestos):", monto_final)
"""