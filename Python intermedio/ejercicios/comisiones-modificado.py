import os
os.system('cls')

class Comision():
    ejecutando = True

    def menu(self):
        print("---"*10)
        self.nombre = input('Ingrese nombre del beneficiario: ')
        print("Codigos ISO:")
        print("1. ARS")
        print("2. USD")
        print("3. EUR")
        print("4. GBP")
        print("5. JPY")
        print("6. Salir")
        self.opcion = int(input("Ingrese la opcion de Codigo ISO: "))
        self.monto = int(input('Ingrese el monto nominal: '))
        self.monto_base = 0
        self.moneda = 0
        print("---"*10)

    def arg(self):
        if self.monto <= 50000:
            n = round(self.monto * 5 / 100, 2)
        elif self.monto <= 200000:
            n = round(self.monto * 3.71 / 100, 2)
        elif self.monto <= 500000:
            n = round(self.monto * 2.25 / 100, 2)
        if self.monto >= 30000:
            n += 4000
        else:
            n = round(self.monto * 1.8 / 100, 2)
               
        if n > 300000:
            self.monto_base = self.monto - 300000
            self.moneda = 'ARS'
        else:
            self.monto_base = self.monto - n
            self.moneda = 'ARS'

        self.corroborar_monto_final()
        self.resumen()
    
    def dolar_euro(self):
        n = round(self.monto * 7 / 100, 2)
        self.monto_base = self.monto - n
        if self.opcion == 2:
            self.moneda = "USD"
        elif self.opcion == 3:
            self.moneda = 'EUR'
        self.corroborar_monto_final()
        self.resumen()
    
    def gbp_jpy(self):
        n = round(self.monto * 9 / 100, 2)
        self.monto_base = self.monto - n
        if self.opcion == 4:
            self.moneda = "GBP"
        elif self.opcion == 5:
            self.moneda = 'JPY'
        self.corroborar_monto_final()
        self.resumen()

    def corroborar_monto_final(self):
        if self.monto > 500000:
            R = self.monto * 21 / 100
            self.monto_final = round(self.monto_base - R, 2)
        else:
            self.monto_final = self.monto_base

    def resumen(self):
        print("---"*10)
        print(f"Beneficiario: {self.nombre}")
        print(f"Moneda: {self.moneda}")
        print(f"Monto base (descontadas las comisiones): {self.monto_base}")
        print(f"Monto final (descontados los impuestos): {self.monto_final}")
        print("---"*10)

com = Comision()
while com.ejecutando:
    
    com.menu()
    if com.opcion == 1:
        com.arg()
    elif com.opcion == 2 or com.opcion == 3:
        com.dolar_euro()
    elif com.opcion == 4 or com.opcion == 5:
        com.gbp_jpy()
    elif com.opcion == 6:
        com.ejecutando = False
    else:
        print("Opcion Invalida")

