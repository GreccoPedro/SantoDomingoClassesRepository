# desempeño 18

x = 0

while x <= 10 :
    nota = float (input ('Ingrese la nota: '))
    x += 1
    if (nota >= 7) :
        print ('La nota está aprobada')
    elif (nota >= 1 and nota < 7 ):
        print ('La nota esta desaprobada')
    else :
        print ('La nota ingresada no es válida')

    
