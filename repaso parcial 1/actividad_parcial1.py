cantidad = 0
acum_promedio = 0
print('Este programa calculará el promedio del conjunto de numeros ingresados. Al ingresar un numero negativo el programa finaliza.')
numero = float (input ('Ingrese un numero flotante positivo'))

while numero>=0 :
    cantidad += 1
    acum_promedio = acum_promedio + numero

    numero = float (input ('Ingrese un numero flotante positivo'))

if cantidad > 0:
    promedio = acum_promedio / cantidad
    print ('El promedio es: ', promedio)
else:
    print('La cantidad de numeros debe ser mayor a 0 para poder calcular el promedio')
