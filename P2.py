print("Este programa calcula el interes compuesto\n")

# Ingreso de datos por el usuario
ci = int(input("Capital inicial: $ "))
x = float(input("Tasa de nterés anual: % "))
n = int(input("Años: "))

# lógica del programa
cf = ci * (1 + x/100) ** n

print("\nEn {n} años el capital de ${ci} a una tasa de interés del {x}% será de ${cf:.2f}".format(n=n, ci=ci, x=x, cf=cf))