#Menú operaciones básicas
print("s. sumar\nR. Restar\nM. Multiplicar\nD. Dividir\nT. Residuo")
opcion = input("ingrese la opción deseada: ")
opcion = opcion.upper

if opcion not in ["S","R","M","D","T"]:
    print ("opción no válida")
else:
    numero1 = float(input("ingrese el primer valor: "))
    numero2 = float(input("ingrese el segundo valor: "))

    if opcion = "S":
       resultado = numero1 + numero2
    #si no, si opcion es R
    elif opcion = "R":
       resultado = numero1 - numero2
    elif opcion == "M":
       resultado = numero1 * numero2
    elif opcion == "D":
       resultado = numero1 / numero2
    elif opcion == "T":
       resultado = numero1 % numero2
    else:
      print("opción no válida :(")
        
print(f"el resultado es {resultado}")

