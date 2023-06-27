# Integrantes -> Sebastián Suárez, Steven Erazo
from collections import deque

def find_shortest_path(maze, start, goal):
    # Obtener las dimensiones del laberinto
    rows = len(maze)
    cols = len(maze[0])
    
    # Verificar si una posición está dentro del laberinto
    def is_valid_position(row, col):
        return 0 <= row < rows and 0 <= col < cols and maze[row][col] == 0
    
    # Definir las direcciones arriba, abajo, izquierda y derecha
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Cola para almacenar las posiciones a explorar
    queue = deque([(start, 0)])  # La tupla (posición, distancia)
    
    # Conjunto para almacenar las posiciones visitadas
    visited = set([start])
    
    # Bucle principal de búsqueda en anchura
    while queue:
        position, distance = queue.popleft()
        row, col = position
        
        # Verificar si se alcanzó la posición objetivo
        if position == goal:
            return distance
        
        # Explorar las posiciones adyacentes
        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            
            if is_valid_position(new_row, new_col) and (new_row, new_col) not in visited:
                queue.append(((new_row, new_col), distance + 1))
                visited.add((new_row, new_col))
    
    # No se encontró una ruta válida hasta la posición objetivo
    return -1

maze = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)  # Posición inicial
goal = (3, 3)   # Posición objetivo

distance = find_shortest_path(maze, start, goal)
if distance != -1:
    print("La ruta más corta tiene una distancia de:", distance)
else:
    print("No se encontró una ruta válida hasta la posición objetivo.")
