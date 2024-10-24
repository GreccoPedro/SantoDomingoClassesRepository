cant_preg = int (input('Ingrese la cantidad total de preguntas'))
cant_preg_correctas = int (input('Ingrese la cantidad de repuestas'))

porcentaje = cant_preg_correctas / cant_preg * 100

if (porcentaje>= 90):
    print ('Se alcanzo el nivel máximo ', porcentaje, '%' )
elif(porcentaje >= 75 and porcentaje < 90):
    print ('Se alcanzo el nivel medio', porcentaje, '%' )
elif(porcentaje >= 50 and porcentaje < 75):
    print ('Se alcanzo el nivel regular', porcentaje, '%' )
else:
    print ('Se encuentra fuera de nivel')
