#nota = float(input('Ingrese la nota'))

#if (nota >= 4): print ('Felicitaciones, aprobaste')

#print ('Fin de programa')

#---------------------------------------------------------

#num1 = int(input("Ingrese el primer numero "))
#num2 = int(input("Ingrese el segundo numero "))

#if (num1>num2): print('El primer numero es mayor que el segundo')
#elif(num1<num2) : print ('El segundo numero es mayor que el primero')
#else : print ('Los numeros son iguales')

#---------------------------------------------------------

nota1 = float(input('Ingrese la primera nota '))
print (nota1)
nota2 = float(input('Ingrese la segunda nota '))
nota3 = float(input('Ingrese la tercera nota '))

promedio = (nota1+nota2+nota3) / 3

print ("El promedio del alumno es ", promedio)

if (promedio>=7) :
    print ("El alumno esta promocionado")
elif (promedio>=4 and promedio<7) :
    print ('El alumno esta regular') #else + if = elif
else :
    print ('El alumno esta reprobado')


# 012345678910111213....
# 0 0,1 0,2 0,3 0,4 ....
