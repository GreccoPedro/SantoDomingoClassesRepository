sueldo = float (input('Ingrese el sueldo del operario'))
anio_antig = int (input ('Ingrese los años de antigüedad del operario'))

if (sueldo < 500 and anio_antig >= 10):
    print ('Se le otorga al operario un 20% de aumento')
    sueldo_nuevo_1 = sueldo + (sueldo * 20 / 100)
    print ('El nuevo sueldo es de  $', sueldo_nuevo_1)
elif (sueldo < 500 and anio_antig < 10):
    print ('Se le otorga al operario un 5% de aumento')
    sueldo_nuevo_2 = sueldo + (sueldo * 5 / 100)
    print ('El nuevo sueldo es de  $', sueldo_nuevo_2)
elif (sueldo >= 500) :
    print ('El sueldo del operario es  $', sueldo)
