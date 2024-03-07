while True:
    print("convierte tus temperaturas  \n1.de Celsius a Fahrenheit\n2.de Fahrenheit a Celsius\n3. Finalizar")

    numero = input("Ingrese el número de la opción que desea realizar: ")

    if numero == "1":
        temperatura = float(input(" temperatura en grados Celsius: "))
        fahrenheit = (temperatura * 9/5) + 32
        print(temperatura, "grados Celsius son equivalentes a" ,fahrenheit, "grados Fahrenheit.\n")
    elif numero == "2":
        temperatura = float(input(" temperatura en grados Fahrenheit: "))
        celsius = (temperatura - 32) * 5/9
        print(temperatura, "grados Fahrenheit son equivalentes a" ,celsius, "grados Celsius.\n")
    elif numero == "3":
        print("que bueno que te vas")
        break
    else:
        print("ingresa algo valido \n")
        