class CuentaBancaria:
    def _init_(self, numero_cuenta, titular, saldo=0.0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo


    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito de ${monto} realizado. Nuevo saldo: ${self.saldo}")
        else:
            print("El monto del depósito debe ser mayor que cero.")

    def retirar(self, monto):
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de ${monto} realizado. Nuevo saldo: ${self.saldo}")
        else:
            print("Monto de retiro no válido o insuficiente saldo.")

    def calcular_interes(self, tasa_interes):
        if tasa_interes >= 0:
            interes = self.saldo * (tasa_interes / 100)
            print(f"Cálculo de interés: ${interes}")
        else:
            print("La tasa de interés debe ser mayor o igual a cero.")

    def imprimir_informacion(self):
        print(f"Información de la cuenta:")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Titular: {self.titular}")
        print(f"Saldo actual: ${self.saldo}")


numero_cuenta = input("Ingrese el número de cuenta: ")
titular = input("Ingrese el nombre del titular: ")
saldo_inicial = float(input("Ingrese el saldo inicial: "))

cuenta = CuentaBancaria(numero_cuenta=numero_cuenta, titular=titular, saldo=saldo_inicial)
cuenta.depositar(float(input("Ingrese la cantidad a depositar: ")))
cuenta.retirar(float(input("Ingrese la cantidad a retirar: ")))
cuenta.calcular_interes(float(input("Ingrese la tasa de interés a aplicar: ")))
cuenta.imprimir_informacion()