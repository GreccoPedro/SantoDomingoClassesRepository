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

