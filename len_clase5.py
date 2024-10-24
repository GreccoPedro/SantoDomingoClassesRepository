#lectura de material:

#variables de cadenas de caracteres

    #input() por defecto devuelve un string

#ejemplo22

"""print('Datos de la primera persona')
nombre1 = input('Ingrese el nombre: ')
edad1 = int(input('Ingrese la edad: '))
altura1 = float(input('Ingrese la altura (en cm): '))

print('Datos de la segunda persona')
nombre2 = input('Ingrese el nombre: ')
edad2 = int (input('Ingrese la edad: '))
altura2 = float(input('Ingrese la altura (en cm): '))

if altura1>altura2 :
    print('La persona con mayor altura es: ', nombre1)
elif altura2>altura1 :
    print('La persona con mayor altura es: ', nombre2)
else :
    print ('Ambas personas tienen la misma altura.')
"""

#ejemplo23
"""
nombre1 = input('Ingrese el primer nombre: ')
nombre2 = input('Ingrese el segundo nombre: ')

if nombre1 ==nombre2:
    print('Los nombres son alfabeticamente iguales')
elif nombre1>nombre2:
    print('El nombre1: ', nombre1, ' es el mayor alfabeticamente')
else:
    print('El nombre2: ', nombre2, ' es el mayor alfabeticamente')
"""
#ejemplo24 (Identificador de nombres alfabéticamente mayores )
"""
opcion = 'si'
suma = 0
while opcion == 'si':
    valor = int(input('Ingrese un valor: '))
    suma= suma+valor
    opcion = input('Desea cargar otro numero? (si/no)')

print ('La suma de los valores ingresados es: ', suma)
"""

# len (ejemplo25)
"""
nombre = input('Ingrese un nombre: ')
print('El primer caracter del nombre ingresado es: ', nombre[0], ' y lo componen ', len(nombre), ' letras')

"""

#ejemplo26
"""
nombre = input('Ingrese su nombre en minuscula y voy a determinar si empieza o no, con vocal: ')
if nombre[0] == 'a' or nombre[0] =='e' or nombre[0] =='i' or nombre[0] == 'o' or nombre[0] =='u':
    print('El nombre ingresado empieza con vocal')
else:
    print('El nombre ingresado no empieza con vocal')
"""

#ejemplo27 (validador de correo electronico)
"""
mail = input('Ingrese un mail: ')
cantidad = 0
x = 0
while x<len(mail):
    if mail[x] == '@':
        cantidad += 1
    x += 1
if cantidad ==1:
    print('El email ingresado contiene un solo arroba')
else:
    print('El email ingresado no contiene un solo arroba')

"""

#Los string en Python son inmutables, esto quiere decir que una vez que los inicializamos no podemos modificarlos

#upper() / lower() /capitalize()














