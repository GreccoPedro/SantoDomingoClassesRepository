# validar fecha de navidad

dd = int(input('Ingrese el día: '))
mm = int(input('Ingrese el mes: '))
aa = int(input('Ingrese el año: '))

if (dd == 25 and mm == 12) :
    print ('La fecha de navidad es correcta')
    print (dd , '/' , mm , '/' , aa)
else :
    print('La fecha de navidad no es correcta')
