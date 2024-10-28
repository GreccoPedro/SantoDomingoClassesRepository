# estrucutura de datos tipo tupla: dato tupla permite almacenar una coleccion de datos no necesariamente del mismo tipo. Los datos de la tupla son inmutables (a diferenceia de las listas) -> no se puede agregar, borrar o modificar sus elementos una vez inicializada [datos que no vamos a modificar ]

# tupla -> var = (1,2,3)
# lista -> var = [1,2,3]

# ej62
"""""
tupla = (1,2,3)
fecha = (25, 'Diciembre', 2016)
punto = (10,2)
persona = ('Rodriguez', 'Pablo', 43)

print(tupla)
print(fecha)
print(punto)
print(persona)

print(punto[0]) #acceso a elementos de la tupla [x]
print(punto[1])
"""
# punto[0] = 70 (arroja error ya que no podemos mutar elemetnos de la tupla)

#ej 63
""""
def cargar_fecha():
    dd = int(input('Ingrese el nro de dia: '))
    mm = int(input('Ingrese el nro de mes: '))
    aa = int(input('Ingrese el nro de año: '))
    return (dd,mm,aa)

def imprimir_fecha (fecha):
    print(fecha[0],fecha[1],fecha[2],sep='-') #var sep como separador 

# bloque principal
fecha = cargar_fecha()


imprimir_fecha(fecha)
"""

# conversion de datos 
# ej 64
""""
tupla_fecha = (30,7,2004)
print('Primer tupla: ',tupla_fecha)

# conversion a lista
fechalista = list(tupla_fecha)
print('Lista copiada de la tupla anterior: ',fechalista)

#modificacion de ahora la lista
fechalista[0]  = 31

print('Impresion de la lista modificada: ',fechalista)

#conversion a tupla
tupla_fecha2 = tuple(fechalista)
print('Se imprime la segunda tupla que se le copio a la lista: ',tupla_fecha2)

"""

# desempeño 76
lista = []
for x in range(5):
    num = 0
    num = int(input('Ingresar un numero entero'))
    lista.append(num)

"""""
for k in range(4):
    for x in range(4-k):
        if lista[x] > lista[x+1]:
            aux = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = aux

tupla = tuple(lista)

print('Impresion de tupla de lista ordenada de menor a mayor: ', tupla)

lista2 = list(tupla)

for k in range(4):
    for x in range(4-k):
        if lista2[x] < lista2[x+1]:
            aux = lista2[x]
            lista2[x] = lista2[x+1]
            lista2[x+1] = aux

tupla2 = tuple(lista2)

print('Impresion de tupla de lista ordenada de mayor a menor: ', tupla2)
"""

tupla = tuple(lista)
def mayor_menor(tupla):
    mayor = tupla[0] 
    menor = tupla[0]

    for x in range(len(tupla)):
        if tupla[x] > mayor:
            mayor = tupla[x]
        if tupla[x] < menor:
            menor = tupla[x]
    
    return (mayor, menor)

mayor , menor = mayor_menor(lista)
print('El menor de la tupla de la lista es: ', menor, ' y el mayor es: ',mayor)