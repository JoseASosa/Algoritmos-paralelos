class Estudiante:
    nombre = ""
    apellidos = ""
    edad= ""
    sexo = ""
    dirreción = ""
    carrera = ""
    email = ""
    telefono = ""

    def DetallesEstudiante(self):
        return self.nombre + " " + self.apellidos + " , " + self.edad + self.sexo + " ," + self.dirreción + " ," + self.carrera + " ," + self.email + " ," + self.telefono

estu = Estudiante()
estu.nombre = input("Nombre..:")
estu.apellidos = input("Apellidos..:")
estu.edad = input("Edad..:")
estu.dirreción = input("Dirreción..:")
estu.carrera = input("Carrera..:")
estu.email = input("Email..:")
estu.telefono = input("Telefono..:")

print(estu.DetallesEstudiante())