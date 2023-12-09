class Persona:
    def __init__(self, nombre="", apellidos="", edad="", sexo="", direccion="", carrera="", email="", sueldo=""):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.sexo = sexo
        self.direccion = direccion
        self.carrera = carrera
        self.email = email
        self.sueldo = sueldo

    def asignar_sueldo(self, sueldo):
        self.sueldo = sueldo

    def calcular_afp(self):
       
        tasa_afp = 0.07
        afp = self.sueldo * tasa_afp
        return afp

    def calcular_sfs(self):
        
        tasa_sfs = 0.0287
        sfs = self.sueldo * tasa_sfs
        return sfs

    def calcular_irs(self):
      
        tasa_irs = 0.15
        irs = self.sueldo * tasa_irs
        return irs

    def calcular_descuento_total(self):
        afp = self.calcular_afp()
        sfs = self.calcular_sfs()
        irs = self.calcular_irs()
        return afp + sfs + irs

    def calcular_sueldo_neto(self):
        descuento = self.calcular_descuento_total()
        return self.sueldo - descuento

    def imprimir_informacion(self):
        print("Información de la Persona:")
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Edad: {self.edad}")
        print(f"Sexo: {self.sexo}")
        print(f"Dirección: {self.direccion}")
        print(f"Carrera: {self.carrera}")
        print(f"Email: {self.email}")
        print(f"Sueldo: {self.sueldo}")
        print(f"AFP: {self.calcular_afp()}")
        print(f"SFS: {self.calcular_sfs()}")
        print(f"IRS: {self.calcular_irs()}")


nombre = input("Ingrese el nombre: ")
apellidos = input("Ingrese los apellidos: ")
edad = input("Ingrese la edad: ")
sexo = input("Ingrese el sexo: ")
direccion = input("Ingrese la dirección: ")
carrera = input("Ingrese la carrera: ")
email = input("Ingrese el email: ")
sueldo = float(input("Ingrese el sueldo: "))


persona = Persona(nombre, apellidos, edad, sexo, direccion, carrera, email, sueldo)
persona.imprimir_informacion()
print("\nInformación de la Nómina:")
print("AFP          : {:0.2f}".format(persona.calcular_afp()))
print("SFS          : {:0.2f}".format(persona.calcular_sfs()))
print("IRS          : {:0.2f}".format(persona.calcular_irs()))
print("Descuento    : {:0.2f}".format(persona.calcular_descuento_total()))
print("Sueldo Neto  : {:0.2f}".format(persona.calcular_sueldo_neto()))