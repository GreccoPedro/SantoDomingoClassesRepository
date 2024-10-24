cor_x = int (input ('Ingrese la coordenada "x"'))
cor_y = int (input ('Ingrese la coordenada "y"'))

if (cor_x != 0 and cor_y != 0) :
    print ('Coordenadas bien ingresadas')
else :
    print ('Las coordenadas deben ser diferentes de 0')

if (cor_x > 0 and cor_y < 0) :
    print ('El punto se encuentra en el primer cuadrante')
elif (cor_x > 0 and cor_y > 0):
    print ('El punto se encuentra en el segundo cuadrante')
elif (cor_x < 0 and cor_y > 0):
    print ('El punto se encuentra en el tercer cuadrante')
elif (cor_x < 0 and cor_y < 0):
    print ('El punto se encuentra en el cuarto cuadrante')
