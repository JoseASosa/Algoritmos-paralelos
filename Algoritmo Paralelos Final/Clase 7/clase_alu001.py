class Alumno:
    nombre= ""
    apellido=""
    edad= int 
    Id= int
    carrera=""
    telefono=int
    direccion= ""

    def NombreCompleto(selt, nombre, apellido):
        return nombre +" "+ apellido
    
alu = Alumno()
nombre=input("Nombre...:")
apellido=input("Apellido...:")

print(alu.NombreCompleto(nombre, apellido))
