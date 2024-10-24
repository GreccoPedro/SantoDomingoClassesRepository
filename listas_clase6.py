# estructura de datos tipo lista

# creacion de listas por asignacion
"""
lista1=[10, 5, 3] #lista de enteros
lista2=[1.78, 2.66, 1.55, 89,4] #lista float
lista3=["lunes", "martes", "miercoles"] #lista str
lista4=["juan", 45, 1.92]  #lista con elementos de varios tipos
"""

"""
# conocer la cantidad de elementos de una lista
lista1 = [10,2,3,4,7]
print(len(lista1))
"""

"""
#ejemplo29
lista = [0,1,2,3,4]
suma = 0
x = 0
while x<len(lista):
    suma = suma + lista[x]
    x += 1
print('Los elementos de la lista son ', lista, ' y la suma de los elementos es: ', suma )
"""

"""
#ejemplo30
meses = ['enero', 'febrero', 'marzo', 'abril']
print('La lista de meses tiene como elementos: ', meses)
print('El primer elemento es: ', meses[0])
print('El segundo elemento es: ', meses[3])
"""

"""
#ejemplo31

alumno = ['Pedro', 10, 2]
print('El nombre del alumno es: ', alumno[0])
print('Las notas del alumno son: ', alumno[1], ' y ', alumno[2])
promedio = (alumno[1] + alumno[2])//2
print('El promedio del alumno es: ', promedio)
"""

#desempeño39

lista = [100,200,50,222,300,222,300,222]
cantidad = 0
x = 0
print ('La lista contiene ', len(lista), ' elementos, y  son: ', lista)
while x<len(lista):
    if lista[x]>100:
        cantidad += 1
    x += 1

print('La cantidad de numeros mayores a 100 dentro de la listas son: ', cantidad)

















