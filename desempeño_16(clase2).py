def calcular_mayor (num1, num2, num3):
    return max(num1, num2, num3) # funcion integrada max(...)

def calcular_menor (num1, num2, num3):
    return min(num1, num2 ,num3) # funcion integrada min(...)

num1 = int (input ('Ingres el primer numero'))
num2 = int (input ('Ingres el segundo numero'))
num3 = int (input ('Ingres el tercer numero'))

mayor = calcular_mayor(num1, num2, num3)
menor = calcular_menor (num1, num2, num3)

print ('El numero mayor es ', mayor)
print ('El numero menor es ', menor)
