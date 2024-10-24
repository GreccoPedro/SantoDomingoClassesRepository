# desempeño 19

cant_alturas = int (input ('Ingrese la cantidad de alturas'))
x=0
promedio = 0
suma_alturas = 0

while x < cant_alturas :
    x += 1
    altura = float (input ('Ingrese la altura en cm'))
    print ('Ingresó: ', altura,'cm')
    suma_alturas = suma_alturas + altura
    
    if x == cant_alturas :
        promedio = suma_alturas / cant_alturas

print ('El promedio de alturas es: ', promedio)

