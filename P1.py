from math import sqrt

print("Este programa calcula el perímetro y área de un traingulo")

# Ingreso de datos por el usuario
a = float(input(" a: "))
b = float(input(" b: "))
c = float(input(" c: "))
    

# lógica del programa
P = a + b + c

s = P / 2
A = sqrt(s * (s - a) * (s - b) * (s - c))


print("\nEl perimetro es:", P)
print("El area es:", A)