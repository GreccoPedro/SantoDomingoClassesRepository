num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))
num3 = int(input('Ingrese el tercer número. ' ))

if(num1==num2 and num1==num3) :
    print('Los numeros ingresados son iguales')    
    suma = num1 + num2
    print('Suma de num1 y num2: ', suma)
    producto = suma * num3
    print ('Producto de la suma y num3: ',producto)
else :
    print('Los numeros ingresados son diferentes')

