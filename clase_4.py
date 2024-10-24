repeticiones = int (input('Ingrese la cantidad de triangulos'))
cantidad = 0
for x in range(0,repeticiones,1):
    base = float(input('Ingrese la base del triangulo'))
    altura = float (input('Ingrese la altura del triangulo'))
    superficie = (base * altura) / 2
    print ('La superficie es ', superficie)
    if superficie > 12:
        cantidad = cantidad + 1


print ('La cantidad de triangulos con superficie mayor a 12 es: ', cantidad)
