#sin terminar
import random

# Paso 1: Información del usuario
titulo = input("Por favor, ingrese su título (Sr. o Sra.): ")
nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")

print(f"{titulo} {nombre} {apellido}, ¡Bienvenido a FastFast Airlines!")

# Paso 2: Selección de vuelo
print("Seleccione su ciudad de origen (escriba el número) (1. Medellín, 2. Bogotá, 3. Cartagena):")
ciudad_origen_opcion = input()
ciudad_origen = ""
if ciudad_origen_opcion == "1":
    ciudad_origen = "Medellín"
elif ciudad_origen_opcion == "2":
    ciudad_origen = "Bogotá"
elif ciudad_origen_opcion == "3":
    ciudad_origen = "Cartagena"

print("Seleccione su ciudad de destino (escriba el número) (1. Medellín, 2. Bogotá, 3. Cartagena):")
ciudad_destino_opcion = input()
ciudad_destino = ""
if ciudad_destino_opcion == "1":
    ciudad_destino = "Medellín"
elif ciudad_destino_opcion == "2":
    ciudad_destino = "Bogotá"
elif ciudad_destino_opcion == "3":
    ciudad_destino = "Cartagena"

dia_semana = input("Ingrese el día de la semana en que desea viajar (por ejemplo, lunes): ")
dia_mes = input("Ingrese el día del mes en que desea viajar (1-30): ")

# Paso 3: Determinar la distancia entre ciudades
if ciudad_origen == ciudad_destino:
    print("El origen y el destino no pueden ser la misma ciudad.")
    exit() # debería repetir el proceso y no cerrar, el profesor dice que con while control y continue

distancia = 0
if (ciudad_origen == "Medellín" and ciudad_destino == "Bogotá") or (ciudad_origen == "Bogotá" and ciudad_destino == "Medellín"):
    distancia = 240
elif (ciudad_origen == "Medellín" and ciudad_destino == "Cartagena") or (ciudad_origen == "Cartagena" and ciudad_destino == "Medellín"):
    distancia = 461
elif (ciudad_origen == "Bogotá" and ciudad_destino == "Cartagena") or (ciudad_origen == "Cartagena" and ciudad_destino == "Bogotá"):
    distancia = 657

# Paso 4: Calcular precio del billete
precio = 0
if distancia < 400:
    if dia_semana.lower() in ["lunes", "martes", "miércoles", "jueves"]:
        precio = 79900
    else:
        precio = 119900
else:
    if dia_semana.lower() in ["lunes", "martes", "miércoles", "jueves"]:
        precio = 156900
    else:
        precio = 213000

# Paso 5: Asignación de asiento
preferencia_asiento = input("¿Prefiere un asiento en el pasillo, junto a la ventana o sin preferencia?: ").lower()
letra_asiento = ""
if preferencia_asiento == "pasillo":
    letra_asiento = "C"
elif preferencia_asiento == "ventana":
    letra_asiento = "A"
else:
    letra_asiento = "B"

numero_asiento = random.randint(1, 29)
asiento_asignado = f"{numero_asiento}{letra_asiento}"

# Paso 6: Salida
print("\nResumen de su vuelo:")
print(f"Nombre: {nombre} {apellido}")
print(f"Origen: {ciudad_origen}")
print(f"Destino: {ciudad_destino}")
print(f"Fecha de vuelo: {dia_semana} {dia_mes}")
print(f"Precio del boleto: $ {precio}")
print(f"Asiento asignado: {asiento_asignado}")
# Agradecimiento a Nelson Miranda por la ayuda en redacción del código