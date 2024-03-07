numero = int(input("ingresa la tabla que deseas ver"))
if numero <= 0:
    print("debes ingresar un numero entero positivo")
else:
    i = 1
while i <= 10:
    resultado = numero * i 
    print(numero, "x", i, "=", resultado )
    i += 1
