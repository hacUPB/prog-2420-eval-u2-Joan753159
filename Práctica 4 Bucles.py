control = True
#programa que dice si un numero es primo o no

while control == True:
    print("1. Calcular primo \n2. Calcular factorial \n3. Salir") #\n es nueva linea
    opcion = int(input("ingrese la opción"))
    if opcion == 1:
        numero = int(input("ingrese el número a probar: "))
        cont = 0
        for divisor in range(1,numero + 1):
            if (numero % divisor) == 0:
                cont += 1
        if cont > 2:
         print(f"{numero} no es primo")
        else:
         print(f"{numero} sí es primo")
    elif opcion == 2:
        numero = int(input("ingrese el número a probar: "))
        fact = 1
        for i in range (1, numero +1):
            fact *= i
        print(f"{numero}! = {fact}")
    elif opcion == 3:
      control = False

    else:
       print("Opcion no válida")