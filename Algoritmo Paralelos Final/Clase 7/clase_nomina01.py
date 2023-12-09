class nomina:

    def Afp(selt, sb):
        return sb * 0.07
    
    def Ars(selt, sb):
        return sb * 0.02
    
    def TotalDesc(setl, afp, ars):
        return afp+ars
    
    def SueldoNeto(selt, sb, td):
        return sb -td
    
nom = nomina()
sueldo=float(input("Entre sueldo base :"))
afp=nom.Afp(sueldo)
ars=nom.Ars(sueldo)
descuento= nom.TotalDesc(afp, ars)
sn= nom.SueldoNeto(sueldo, descuento)

print("Afp          : {:0.2f}".format(afp))
print("Ars          : {:0.2f}".format(ars))
print("Descuento    : {:0.2f}".format(descuento))
print("Sueldo Neto  : {:0.2f}".format(sn))
