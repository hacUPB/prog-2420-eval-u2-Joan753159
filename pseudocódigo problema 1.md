# Pseudocódigo problema #1

```
Inicio

// Paso 1: Información del usuario
Print "Por favor, ingrese su título (Sr. o Sra.):"
Leer título
Print "Por favor, ingrese su nombre:"
Leer nombre
Print "Por favor, ingrese su apellido:"
Leer apellido

Print título  " " nombre " " apellido ", ¡Bienvenido a FastFast Airlines!"

// Paso 2: Selección de vuelo
Print "Seleccione su ciudad de origen (1. Medellín, 2. Bogotá, 3. Cartagena):"
Leer ciudad_origen

Print "Seleccione su ciudad de destino (1. Medellín, 2. Bogotá, 3. Cartagena):"
Leer ciudad_destino

Print "Ingrese el día de la semana en que desea viajar (por ejemplo, lunes):"
Leer dia_semana

Print "Ingrese el día del mes en que desea viajar (1-30):"
Leer dia_mes

// Paso 3: Determinar la distancia entre ciudades
SI ciudad_origen = ciudad_destino
    Print "El origen y el destino no pueden ser la misma ciudad."
    TERMINAR

SI ciudad_origen = "Medellín" y ciudad_destino = "Bogotá" O ciudad_origen = "Bogotá" y ciudad_destino = "Medellín"
    distancia = 240 km
SI ciudad_origen = "Medellín" y ciudad_destino = "Cartagena" O ciudad_origen = "Cartagena" y ciudad_destino = "Medellín"
    distancia = 461 km
SI ciudad_origen = "Bogotá" y ciudad_destino = "Cartagena" O ciudad_origen = "Cartagena" y ciudad_destino = "Bogotá"
    distancia = 657 km

// Paso 4: Calcular precio del billete
SI distancia < 400 km
    SI dia_semana = "lunes" O dia_semana = "martes" O dia_semana = "miércoles" O dia_semana = "jueves"
        precio = 79900
    Sino
        precio = 119900
Sino
    SI dia_semana = "lunes" O dia_semana = "martes" O dia_semana = "miércoles" O dia_semana = "jueves"
        precio = 156900
    Sino
        precio = 213000

// Paso 5: Asignación de asiento
Print "¿Prefiere un asiento en el pasillo, junto a la ventana o sin preferencia?"
Leer preferencia_asiento

SI preferencia_asiento = "pasillo"
    letra_asiento = "C"
SI preferencia_asiento = "ventana"
    letra_asiento = "A"
SI preferencia_asiento = "sin preferencia"
    letra_asiento = "B"
    
numero_asiento = random.randint(1, 29)
asiento_asignado = numero_asiento + letra_asiento

// Paso 6: Salida
Print "Resumen de su vuelo:"
Print "Nombre:   (nombre,    apellido)"
Print "Origen:  (ciudad_origen)"
Print "Destino:   (ciudad_destino)"
Print "Fecha de vuelo:   (dia_semana   dia_mes)"
Print "Precio del boleto: $ (precio)"
Print "Asiento asignado:   (asiento_asignado)"

Fin
```