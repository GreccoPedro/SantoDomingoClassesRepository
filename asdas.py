x = 0
cant_aprobadas = 0
cant_promocionado = 0
cant_desaprobado = 0

if x <= 3:
    x += 1
    nota = float (input ('Ingresar la nota'))

    if (nota >= 4 and nota < 7):
        cant_aprobadas += 1
    elif (nota >= 7):
        cant_promocionado += 1
    else :
        cant_desaprobado += 1
        
