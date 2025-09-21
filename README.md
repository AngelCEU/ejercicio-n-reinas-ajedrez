# ejercicio-n-reinas-ajedrez

https://github.com/AngelCEU/ejercicio-n-reinas-ajedrez.git

🧩 Reto de Algoritmos: El Desafío de las N-Reinas

Presentación del Problema

En este ejercicio, abordaremos uno de los problemas clásicos de la informática y la teoría de algoritmos: ubicar n reinas en un tablero de ajedrez de tamaño n × n de forma que ninguna se amenace entre sí. Este problema es ideal para desarrollar habilidades de:

Representación de soluciones
Recursividad
Backtracking
Optimización algorítmica
Reglas del Juego

La reina en ajedrez se mueve en líneas rectas: horizontal, vertical y diagonal. Por tanto, dos reinas se amenazan si están en la misma fila, columna o diagonal.

Objetivo del Reto

Diseñar un algoritmo que permita encontrar una solución válida para el problema de las n-reinas, y reflexionar sobre:

¿Cómo se representa el tablero y la posición de las reinas?
¿Qué estrategia algorítmica es más adecuada?
¿Cómo se puede escalar la solución para diferentes valores de n?
Actividades Propuestas

Representación del Problema:
Usar un vector de tamaño n donde el índice representa la columna y el valor la fila de la reina.
Ejemplo: [1, 3, 0, 2] representa una solución para 4 reinas.
Diseño del Algoritmo:
Reflexionarsobre una función recursiva que coloque reinas una por una en cada columna.
Reflexionar sobre una solución probabilista (empleando aleatoriedad).
Verificar en cada paso si la posición es válida (sin amenazas).
Exploración de Soluciones:
Encontrar una solución para n = 4, 5, 6, 7, 8.
¿Cuántas soluciones distintas existen para cada n?
¿Cómo cambia el tiempo de ejecución al aumentar n en cada caso?
