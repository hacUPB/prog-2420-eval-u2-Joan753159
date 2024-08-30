# Análisis problema #1

## constantes
```
-Distancias entre ciudades:
DISTANCIA_MEDELLIN_BOGOTA = 240 km
DISTANCIA_MEDELLIN_CARTAGENA = 461 km
DISTANCIA_BOGOTA_CARTAGENA = 657 km

-Precios para distancias menores de 400 km:
De lunes a jueves: PRECIO_CORTO_SEMANA = 79900 (COP)
De viernes a domingo: PRECIO_CORTO_FIN_SEMANA = 119900 (COP)

-Precios para distancias de 400 km o más:
De lunes a jueves: PRECIO_LARGO_SEMANA = 156900 (COP)
De viernes a domingo: PRECIO_LARGO_FIN_SEMANA = 213000 (COP)
```
## variables

```
-Información del usuario:
titulo: Título del usuario (Sr. o Sra.)
nombre: Nombre del usuario
apellido: Apellido del usuario

-Selección de vuelo:
ciudad_origen: Ciudad de origen seleccionada por el usuario
ciudad_destino: Ciudad de destino seleccionada por el usuario
distancia: Distancia entre la ciudad de origen y destino
dia_semana: Día de la semana seleccionado para el vuelo (ejm. lunes)
dia_mes: Día del mes seleccionado para el vuelo (número entre 1 y 30)
precio: Precio del boleto calculado

-Asignación de asiento:
preferencia_asiento: Preferencia de asiento del usuario (pasillo, ventana, sin preferencia)
letra_asiento: Letra del asiento asignada según la preferencia (A, B, C)
numero_asiento: Número del asiento asignado aleatoriamente (entre 1 y 29)
asiento: Asiento completo asignado al usuario (ejm. 20C)
```
## Ecuaciones

#### Las ecuaciones y la lógica del problema se encargan de calcular el precio del boleto, la distancia entre ciudades y la asignación de asientos, basándose en las entradas proporcionadas por el usuario. A continuación, se realiza un análisis detallado de estas ecuaciones y su funcionalidad dentro del programa.

```
Si (ciudad_origen, ciudad_destino) es (Medellín, Bogotá) o (Bogotá, Medellín)
    distancia = DISTANCIA_MEDELLIN_BOGOTA
Sino si (ciudad_origen, ciudad_destino) es (Medellín, Cartagena) o (Cartagena, Medellín)
    distancia = DISTANCIA_MEDELLIN_CARTAGENA
Sino si (ciudad_origen, ciudad_destino) es (Bogotá, Cartagena) o (Cartagena, Bogotá)
    distancia = DISTANCIA_BOGOTA_CARTAGENA
```
Esta ecuación determina la distancia entre las ciudades seleccionadas, que es esencial para calcular el precio del boleto.

```
Si distancia < 400 Entonces
    Si dia_semana es "lunes" o "martes" o "miércoles" o "jueves"
        precio = PRECIO_CORTO_SEMANA
    Sino
        precio = PRECIO_CORTO_FIN_SEMANA
Sino
    Si dia_semana es "lunes" o "martes" o "miércoles" o "jueves"
        precio = PRECIO_LARGO_SEMANA
    Sino
        precio = PRECIO_LARGO_FIN_SEMANA
```

Esta ecuación utiliza un enfoque condicional para calcular el precio del boleto basado en dos factores principales:
Distancia: Si es menor o mayor a 400 km.
Día de la semana: Si es entre lunes y jueves o entre viernes y domingo.

```
Si preferencia_asiento es "pasillo"
    letra_asiento = "C"
Sino si preferencia_asiento es "ventana"
    letra_asiento = "A"
Sino
    letra_asiento = "B"
```
Esta ecuación determina la letra del asiento asignado en función de la preferencia del usuario.
```
numero_asiento = random.randint(1, 29)
```
Estaescuación asigna un numero aleatorio para elegir la silla del usuario.
```
asiento = numero_asiento + letra_asiento
```
Esta ecuación combina el número de asiento aleatorio y la letra del asiento (según preferencia) para formar un identificador de asiento completo, como "20-C".

