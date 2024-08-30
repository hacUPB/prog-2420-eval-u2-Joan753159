# Análisis problema #2

## Constantes
```
 -umbral_estabilidad:

 Valor: 0.001 (o cualquier valor pequeño).
 Descripción: Define el valor por debajo del cual la pérdida de altitud se considera insignificante y se puede asumir que el satélite se ha estabilizado en su órbita.
 ```

 ## Variables

 ```
altitud_inicial:
Tipo: Entrada del usuario.
Descripción: Altitud inicial del satélite en kilómetros.

coeficiente_arrastre:
Tipo: Entrada del usuario / Variable.
Descripción: Coeficiente que determina la rapidez con la que el satélite pierde altitud. Este valor aumenta con cada órbita.

altitud_minima_seguridad:
Tipo: Entrada del usuario.
Descripción: Altitud por debajo de la cual se considera que el satélite ha reingresado en la atmósfera terrestre.

altitud_actual:
Tipo: Variable.
Descripción: Altitud del satélite en kilómetros en una órbita determinada.

orbita:
Tipo: Variable.
Descripción: Contador que registra el número de órbitas completadas por el satélite.

altitud_perdida:
Tipo: Variable.
Descripción: Cantidad de altitud que el satélite pierde en cada órbita debido a la resistencia atmosférica.
```

### Ecuaciones
```
altitud_perdida = coeficiente_arrastre * altitud_actual
-Descripción: Esta ecuación calcula la cantidad de altitud que el satélite pierde durante una órbita específica.

altitud_actual = altitud_actual - altitud_perdida
-Descripción: Esta ecuación actualiza la altitud del satélite después de cada órbita.

coeficiente_arrastre = coeficiente_arrastre + 0.0001
-Descripción: Simula el incremento de la resistencia atmosférica a medida que el satélite desciende en altitud.
```
