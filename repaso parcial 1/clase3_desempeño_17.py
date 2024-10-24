cant_triangulos = int (input ('Ingrese la cantidad de triangulos'))
cant_equilatero = 0
cant_isoceles = 0
cant_escaleno = 0



for triangulo in range (cant_triangulos):
    
    lado1 = float (input ('Ingrese el lado uno'))
    lado2 = float (input ('Ingrese el lado dos'))
    lado3 = float (input ('Ingrese el lado tres'))

    if(lado1==lado2 and lado1==lado3):
        print('es equilatero')
        cant_equilatero = cant_equilatero + 1
    elif(lado1==lado2 and lado1 != lado3):
        print ('es isoceles')
        cant_isoceles = cant_isoceles + 1
    else :
        print ('es escaleno')
        cant_escaleno = cant_escaleno + 1

print ('La cantidad de equilateros es: ',cant_equilatero)
print ('La cantidad de isoceles es: ',cant_isoceles)
print ('La cantidad de escalenos es: ',cant_escaleno)
