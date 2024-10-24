# ordenamiento de listas

# ej 37

"""
sueldos = []
sueldo = 0

for x in range(5):
    sueldo = float(input('Ingrese el sueldo'))
    sueldos.append(sueldo)

print('Lista sin ordenar', sueldos)

for x in range(4):
    if sueldos[x]>sueldos[x+1]:
        aux = sueldos[x]
        sueldos[x] = sueldos[x+1]
        sueldos[x+1] = aux

print('Lista con el ultimo elemento ordenado (mayor) ',sueldos )

"""
# ej 38

"""
Se debe crear y cargar una lista donde almacenar 5 sueldos. Ordenar de menor a mayor la lista.

"""
""""
sueldos = []
for x in range(5):
    sueldo = int(input('Ingrese  el sueldo: '))
    sueldos.append(sueldo)

print ('La lista sin ordenar: ', sueldos)

for k in range(4):
    for x in range(4):
        if sueldos[x]>sueldos[x+1]:
            aux = sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux

print('La lista ordenada quedaria: ',sueldos)

"""

#desempeño 50
""""
lista = []

for x in range (5):
    pais = input('Ingrese el nombre del pais').lower()
    lista.append(pais)

print('La lista con los nombres de paises desordenados: ',lista)

for k in range(4):
    for x in range(4-k):
        if lista[x] > lista[x+1]:
            aux = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = aux


print('La lista con los nombres de paises ordenados: ', lista)

"""

# desempeño 51
""""
cant_empleados = 0
sueldos = []
sueldo = 0

cant_empleados = int(input('Ingrese la cantidad de empleados que posee la empresa: '))

for x in range(cant_empleados):
    sueldo = int(input('Ingrese el sueldo exacto del empleado: '))
    sueldos.append(sueldo)

for k in range(cant_empleados-1):
    for x in range((cant_empleados-1)-k):
        if sueldos[x] > sueldos[x+1]:
            aux = sueldos[x]
            sueldos[x] = sueldos[x+1]
            sueldos[x+1] = aux

print('Lista de sueldos ordenada de menor a mayor: ',sueldos)
"""

#desempeño 52

"""""
lista = []
valor = 0

for x in range(5):
    valor = int(input('Ingrese un valor entero: '))
    lista.append(valor)

for k in range(4):
    for x in range(4-k):
        if lista[x] > lista[x+1]:
            aux = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = aux

print('Lista ordenada de menor a mayor: ',lista)

for k in range(4):
    for x in range(4-k):
        if lista[x] < lista[x+1]:
            aux = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = aux

print('Lista ordenada de mayor a menor: ', lista)


"""

# ordenamiento de listas pararelas 
# al trabajar con listas pararelas, y se ordenan los elementos de una de ellas, hay que tener la precaucion de intercambiar de la misma manera los elemetnos de las restantes



#ejemplo 39 - ordenar alumnos y notas 

""""
alumnos = []
notas = []
nota = 0
nombre = ' '

for x in range (5):
    nombre = input('Ingrese el nombre del alumno: ')
    alumnos.append(nombre)
    nota = float(input('Ingrese la nota del alumno: '))
    notas.append(nota)

for x in range(5):
    print('Se imprime la lista desordenada: ', alumnos[x], notas[x])

for k in range(4):
    for x in range(4-k):
        # la estrucutra la englobamos dentro del if segun la lista notas[]
        if notas[x] < notas[x+1]:
            aux1 = notas[x]
            notas[x] = notas[x+1]
            notas[x+1] = aux1
            aux2 = alumnos[x]
            alumnos[x] = alumnos[x+1]
            alumnos[x+1] = aux2

print ('------------------------------------------------------')
for x in range(5):
    print('Se imprime la lista ordenada(mayor a menor): ', alumnos[x], notas[x])

"""


# desempeño 53
""""
paises = []
poblaciones = []
cant_hab = 0
pais = ' '
aux1 = 0
aux2 = 0

for x in range(5):
    pais = input('Ingrese el nombre de un pais: ')
    paises.append(pais.capitalize())
    print(paises)
    cant_hab = int(input('Ingrese la cantidad de habitantes: '))
    poblaciones.append(cant_hab)

for k in range(4):
    for x in range(4-k):
        if paises[x] > paises[x+1]:
            aux1 = paises[x]
            paises[x] = paises [x+1]
            paises[x+1] = aux1
            aux2 = poblaciones[x]
            poblaciones[x] = poblaciones[x+1]
            poblaciones[x+1] = aux2

print('--------------------------------------------------')
print ('Las listas pararelas ordenadas alfabeticamente: ')
for x in range(5):
    print  (paises[x], poblaciones[x])

# ordenamiento segun la cantidad de habitantes 
for k in range(4):
    for x in range(4-k):
        if poblaciones[x] > poblaciones[x+1]:
            aux1 = poblaciones[x]
            poblaciones[x] = poblaciones[x+1]
            poblaciones[x+1] = aux1
            #-------------------------------
            aux2 = paises[x]
            paises[x] = paises[x+1]
            paises[x+1] = aux2

print('-----------------------------------------------------------------------')
print('Listas ordenadas segun la cantidad de habitantes de menor a mayor: ')
for x in range(5):
    print(paises[x],poblaciones[x])    

"""

# sumando listas con componentes de tipo lista

#ejemplo 41

# primera manera:

""""
lista = [[1,2,3,4,5],[1,2,3,4,5]]

suma1 = lista[0][0] + lista[0][1] + lista[0][2] + lista[0][3] + lista[0][4]

suma2 = lista[1][0] + lista[1][1] + lista[1][2] + lista[1][3] + lista[1][4]

print('La suma de elementos del elemento N°1 es :', suma1)
print('La suma de elementos del elemento N°2 es :', suma2)

print('-----------------------------------------------------')

#segunda manera:

suma3 = 0
suma4 = 0

for x in range(len(lista[0])):
    suma3 += lista[0][x]

for x in range(len(lista[1])):
    suma4 += lista[1][x]

print(suma3)
print(suma4)


print ('--------------------------------------------------------')

suma5 = 0


for k in range(len(lista)):
    suma5 = 0
    for x in range(len(lista[k])):
        suma5 += lista[k][x]
    print(suma5)

    
"""


#ejemplo 42
""""
lista = [[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5]]

suma = 0

for k in range(len(lista)):
    for x in range(len(lista[k])):
        suma += lista[k][x]
    
print(suma)

"""

""""
#desempeño54
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]

print(lista)
for k in range(len(lista)):
    for x in range(len(lista[k])):
        if (lista[k][x]>50):
            lista[k][x] = 0


print(lista)

"""

#desempeño55
""""
lista=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]

print(lista)


for i in range(len(lista)):
    for x in range(len(lista[0])):
        if (lista[0][x]>10):
            lista[0][x] = 0
            print('Se modifico la lista')

print(lista)

"""

# desempeño56
"""""
lista = [[9,8,7,6,5],[5,6,7,8,9],[1,2,3,4],[4,3,2,1]]

print(lista[3])

"""

# carga por teclado de componentes tipo lista

# ej 43 Alumnos y notas cargados por teclado 
"""
nombres = []
notas = []

for x in range(3):
    nombre = input('Ingrese el nombre del alumno: ')
    nombres.append(nombre)
    nota1 = float(input('Ingrese la primera nota del alumno: '))
    nota2 = float(input('Ingrese la segunda nota del alumno: '))
    notas.append([nota1,nota2])

for x in range(3):
    print('Nombre: ',nombres[x],'| Notas :', notas[x][0], notas[x][1])
    
"""

#ejemplo44

# cargar(3): nombre, sueldo, cobrado en 3 meses

# a| Realizar la carga de los nombres de empleados y los tres sueldos por cada empleado. 
# b| Generar una lista que contenga el ingreso acumulado en sueldos en los últimos 3 meses para cada empleado. 
# c|  Mostrar por pantalla el total pagado en sueldos a cada empleado en los últimos 3 meses d|  Obtener el nombre del empleado que tuvo el mayor ingreso acumulado

nombres = []
sueldos = []
sumas = []

for x in range(3):
    nombre = input('Ingrese el nombre del empleado ')
    nombres.append(nombre)
    sueldo1 = float(input('Ingrese el sueldo cobrado hace 3 meses '))
    sueldo2 = float(input('Ingrese el sueldo cobrado hace 2 meses '))
    sueldo3 = float(input('Ingrese el sueldo cobrado hace 1 mes '))
    sueldos.append([sueldo1,sueldo2,sueldo3])

suma = 0
for k in range(len(sueldos)):
    suma = 0
    for x in range(len(sueldos[k])):
        suma += sueldos[k][x]
    sumas.append(suma)

for x in range(3):
    print('Las sumas totales de sueldos de 3 meses son: ', nombres[x], sumas[x])
    
posmayor = 0
mayor = sumas[0]
for x in range(1,3):
    if sumas[x]>mayor:
        posmayor=x
        mayor = sumas[x]

print('Empleado con mayores ingresos en los ultimos 3 meses es: ', nombres[posmayor], ' con un ingreso de: ', mayor)