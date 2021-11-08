from turtle import Screen, Turtle

# Ingreso de datos por el usuario
while True:
    try:
        print("Ingrese la figura a dibujar, si desea salir ingrese (0)")
        print("(1) triangulo")
        print("(2) cuadrado")
        print("(3) circulo")
        
        eleccion = int(input("Elección: "))
        if eleccion < 0 or eleccion > 3:        
            raise
        
        break
    except:
        print('\nElección invalida, intente nuevamente')        


if eleccion == 0:
    exit()

# definir variables para la GUI
pantalla = Screen()
tortuga = Turtle()
lado = 300

pantalla.setup(425, 425)
pantalla.screensize(400,400)
pantalla.setworldcoordinates(-50,-50, 350, 350)

tortuga.pensize(3)
tortuga.penup()


# dibuja un triangulo
if eleccion == 1:    
    tortuga.pendown()
    tortuga.forward(lado)
    tortuga.left(120)
    tortuga.forward(lado)
    tortuga.left(120)
    tortuga.forward(lado)
    
# dibuja un cuadrado
elif eleccion == 2:    
    tortuga.pendown()
    cuenta = 0
    while cuenta < 4:
        tortuga.forward(lado)
        tortuga.left(90)
        cuenta += 1
    
# dibuja un circulo
elif eleccion == 3:
    tortuga.forward(lado/2)
    tortuga.pendown()
    tortuga.circle(lado/2)
    
tortuga.penup()