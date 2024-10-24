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