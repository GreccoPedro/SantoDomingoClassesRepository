sueldo = float( input('Ingrese el sueldo del operario: '))
antiguedad = int(input ('Ingrese los años de antigüedad del operario: '))

if (sueldo<500 and antiguedad >= 10) :
    sueldo_nuevo = sueldo + ((20/100)*sueldo)
    print ('Se le asigna un aumento del 20%. El sueldo a pagar es: ', sueldo_nuevo)
