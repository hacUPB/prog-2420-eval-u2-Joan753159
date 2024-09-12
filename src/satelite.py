# Paso 1: Solicitar datos de entrada
altitud_inicial = float(input("Ingrese la altitud inicial del satélite (en kilómetros): "))
coeficiente_arrastre = float(input("Ingrese el coeficiente de arrastre inicial (un valor decimal pequeño, como 0.01): "))
altitud_minima_seguridad = float(input("Ingrese la altitud mínima de seguridad (en kilómetros): "))

# Inicializar variables
altitud_actual = altitud_inicial
orbita = 0
umbral_estabilidad = 0.001  # Un umbral para determinar si la pérdida de altitud es muy pequeña

# Paso 2: Simulación de la desintegración orbital
while altitud_actual > altitud_minima_seguridad:
    # Incrementar el número de órbitas
    orbita += 1
    
    # Calcular la pérdida de altitud debido al arrastre
    altitud_perdida = coeficiente_arrastre * altitud_actual
    
    # Reducir la altitud actual
    altitud_actual -= altitud_perdida
    
    # Incrementar el coeficiente de arrastre
    coeficiente_arrastre += 0.0001
    
    # Verificar si el satélite se ha estabilizado
    if altitud_perdida < umbral_estabilidad:
        print("El satélite se ha estabilizado en una órbita baja.")
        print(f"Altitud final: {altitud_actual:.2f} km")
        print(f"Número de órbitas completadas: {orbita}")
        break
else:
    # Si el satélite ha reingresado en la atmósfera
    print("El satélite ha reingresado en la atmósfera terrestre y se ha desintegrado.")
    print(f"Número total de órbitas completadas: {orbita}")

# Agradecimiento a Nelson Miranda por la ayuda en redacción del código