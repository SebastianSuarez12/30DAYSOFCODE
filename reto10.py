# Integrantes -> Sebastián Suárez, Steven Erazo

from itertools import permutations

def generar_combinaciones(palabras):
    for palabra in palabras:
        letras = list(palabra)
        for r in range(1, len(letras) + 1):
            posibles_combinaciones = list(permutations(letras, r))
            for combinacion in posibles_combinaciones:
                posible_palabra = ''.join(combinacion)
                print(posible_palabra)

palabras = ['AITLAI', 'AMOR', 'NOITCAAV']

generar_combinaciones(palabras)


