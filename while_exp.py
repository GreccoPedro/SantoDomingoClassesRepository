# desempeño 17

# a)
#x = 0

#while x < 500 :
   # x += 1
   # print (x)

# b)
#x = 50

#while x < 100:
   # x+= 1
   # print (x)


# c)
#x = 0
#while x > -50 :
   # x -= 1
   # print (x)

# d)
#x=2
#while x < 100:
  #  print (x)
  # x = x+2

# ejemplo 12

#num = int (input('Ingrese un numero positivo '))

#if num>0 :
   # x = 0
   # while x < num :
        #x = x + 1
       # print (x)
#else :
   # print('El numero ingresado no es correcto')

#print ('El programa a finalizado')

# desempeño 18

#x = 0
#aprobados = 0
#desaprobados = 0

#while (x < 10) :
    #nota = float (input('Ingrese la nota'))
    #x += 1
    #if (nota >= 7):
        #aprobados += 1
        #print('Esta nota esta aprobada')
    #else :
        #desaprobados += 1
        #print ('Esta nota esta desaprobada')

#print ('La cantidad de notas aprobadas son: ', aprobados, ' y la cantidad de notas desaprobadas son: ', desaprobados)

# desempeño 20

num_empleados = int (input ('Ingrese el numero de empleados'))
x = 0
sueldo_medio = 0
sueldo_alto = 0
gasto_total = 0

while x < num_empleados :
    x += 1
    sueldo = float (input ('Ingrese el sueldo del empleado'))
    gasto_total = gasto_total + sueldo
    if (sueldo <= 500 and sueldo >= 100):
        print ('El sueldo ingresado es valido')
        if (sueldo >= 100 and sueldo <= 300):
            sueldo_medio += 1
        elif (sueldo > 300):
            sueldo_alto += 1
    else :
        print ('El sueldo ingresado no es valido')

print ('La cantidad de empleados que cobran entre $100 y $300 son: ', sueldo_medio)
print ('La cantidad de empleados que cobran mas de $300 son: ', sueldo_alto)
print ('La empresa en sueldos de personal, gasta: ', gasto_total)
    






















