i = 0
super_mayor = 0
i = int (input ('Ingrese el nro de veces que desea ingresar pares de datos de base y altura'))

for x in range (i):
    base = float (input ('Ingrese la base del triangulo'))
    altura = float(input ('Ingrese la altura del triangulo'))

    print ('La altura del triangulo es: ', altura, '. La base del triangulo es: ',base)
    superficie = (base * altura)/2
    print ('La superficie del triangulo es: ', superficie)

    if(superficie>12):
        super_mayor += 1
    
print ('La cantidad de triangulos cuya superficie es mayor a 12 es: ', super_mayor)    
    
