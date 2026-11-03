mapa = [
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0]
]

N = len(mapa)


def labcam(f, c):

    if f >= N or c >= N:
        return 0

    if mapa[f][c] == 1:
        return 0

    if f == N - 1 and c == N - 1:
        return 1

 
    if f == N - 1:
        return labcam(f, c + 1) + 0


    elif c == N - 1:
        return 0 + labcam(f + 1, c)

   
    else:
        return labcam(f, c + 1) + labcam(f + 1, c)


print("=========================================")
print("       SIMULADOR DE RUTAS - RATON        ")
print("=========================================")
print("Este es el mapa que debe cruzar el raton:\n")

for fila in mapa:
    print(fila)

print("\nIniciando el analisis de caminos...")


labcam(0, 0)

print("\n>> Analisis completado. El raton logro explorar y trazar todas las salidas validas.")
print("=========================================")