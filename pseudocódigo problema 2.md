# pseudocódigo problema #2
#### (mas complicado que el anterior)

```
Inicio

// Paso 1: Solicitar datos de entrada
print "Ingrese la altitud inicial del satélite (en kilómetros):"
Leer altitud_inicial

print "Ingrese el coeficiente de arrastre inicial (un valor decimal pequeño, como 0.01):"
Leer coeficiente_arrastre

print "Ingrese la altitud mínima de seguridad (en kilómetros):"
Leer altitud_minima_seguridad

// Inicializar variables
altitud_actual = altitud_inicial
orbita = 0
umbral_estabilidad = 0.001 // Un umbral para determinar si la pérdida de altitud es muy pequeña

// Paso 2: Simulación de la desintegración orbital
Mientras altitud_actual > altitud_minima_seguridad
    // Incrementar el número de órbitas
    orbita = orbita + 1
    
    // Calcular la pérdida de altitud debido al arrastre
    altitud_perdida = coeficiente_arrastre * altitud_actual
    
    // Reducir la altitud actual
    altitud_actual = altitud_actual - altitud_perdida
    
    // Incrementar el coeficiente de arrastre
    coeficiente_arrastre = coeficiente_arrastre + 0.0001
    
    // Verificar si el satélite se ha estabilizado
    SI altitud_perdida < umbral_estabilidad
        print "El satélite se ha estabilizado en una órbita baja."
        print "Altitud final:  (altitud_actual )  (km)"
        print "Número de órbitas completadas: (orbita)"
        TERMINAR

Fin si

// Si el satélite ha reingresado en la atmósfera
print "El satélite ha reingresado en la atmósfera terrestre y se ha desintegrado."
print "Número total de órbitas completadas:   orbita"

Fin
```
