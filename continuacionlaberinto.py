# Comenzamos definiendo una funcion denominada crear_laberinto, esta va a tomar tres parámetros, el parámetro 'muro' va a hacer referencia a las coordenadas con las casillas de muros, mientras que `'filas' y 'columnas' van a hacer referencia a las dimensiones del laberinto.
def crear_laberinto(muro, filas, columnas):

# Se inicializa una lista bidimensional (lista de listas) llamada 'laberinto', utilizamos la lista bidimensional para representar visualmente la estructura de laberinto, donde cada elemento de la lista bidimensional es una celda en el laberinto, y los indices de fila y columna se emplean para acceder y modificar esas celdas.
    laberinto = [['' for _ in range(columnas)] for _ in range(filas)]
    laberinto = [
    [' ', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ]
# Utilizamos el bucle 'for' para itinerar sobre cada par de coordenadas en la tupla 'muro', muro_coordenadas, representa una tupla de coordenadas de un muro específico. Desglosamos las variables además en las variables fila y columna.
    for muro_coordenadas in muro:
        fila, columna = muro_coordenadas
        laberinto[fila][columna] = 'X'

    return laberinto

# Tupla de coordenadas de las casillas con muros
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

# Definimos las dimensiones del laberinto
filas = 5
columnas = 5

laberinto = crear_laberinto(muro, filas, columnas)

for fila in laberinto:
    print(fila)

def recorrer_laberinto(laberinto):
# Posición actual del jugador
  fila = 0
  columna = 0
# Movimientos realizados
  movimientos = []
# Mientras no se encuentra la salida se sigue explorando el recorrido del laberinto
  while laberinto[fila][columna] != "S" and laberinto[fila][columna] != "X":
    # comprobamos si podemos movernos hacia abajo.
    if fila +1 < len(laberinto):
      if laberinto[fila +1][columna] == "":
        fila += 1
        movimientos.append("Abajo")
        continue
    # comprobamos si podemos movernos hacia la derecha.
    if columna +1 < len(laberinto[0]):
      if laberinto[fila][columna + 1] == "":
        columna += 1
        movimientos.append("Derecha")
        continue
    # comprobamos si podemos movernos hacia arriba.
    if fila -1 >= 0:
      if laberinto[fila -1 ][columna] == "":
        fila -= 1
        movimientos.append("Arriba")
        continue
    # comprobamos si podemos movernos hacia la izquierda.
    if columna -1 >= 0: 
      if laberinto[fila][columna -1] == "":
        columna -= 1
        movimientos.append("Izquierda")
        continue
    # en el caso de que no podamos movernos significará quenos hemos quedado atascados por lo que devolveremos una lista vacía.
    return []
  return movimientos
if __name__== "__main__":
  muros = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
  laberinto = crear_laberinto(muro, filas, columnas)
  movimientos = recorrer_laberinto(laberinto)
  print(movimientos)
