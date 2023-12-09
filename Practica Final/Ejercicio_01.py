class Persona:
    nombre = ""
    apellidos = ""
    edad= ""
    sexo = ""
    dirreción = ""

    def Nombre_Persona(self):
        return self.nombre + " " + self.apellidos + " , " + self.edad + self.sexo + " ," + self.dirreción

Person = Persona()
Person.nombre = input("Nombre..:")
Person.apellidos = input("Apellidos..:")
Person.edad = input("Edad..:")
Person.dirreción = input("Dirreción..:")

print(Person.Nombre_Persona())