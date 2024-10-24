x = float(input('Ingrese el punto en x: '))
y = float(input('Ingrese el punto en y: '))

if (x>0 and y>0):
    print('El punto se encuentra en el primer cuadrante')
elif (x<0 and y>0):
    print ('El punto se encuentra en el segundo cuadrante')
elif (x<0 and y<0):
    print ('El punto se encuentra en el tercer cuadrante')
else:
    print ('El punto se encuentra en el cuarto cuadrante ')
