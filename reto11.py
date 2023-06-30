# Integrantes -> Sebastián Suárez, Steven Erazo

def decodificar_mensaje(mensaje):
    clave = {
        '0': 'a',
        '1': 'b',
        '2': 'c',
        '3': 'd',
        '4': 'e',
        '5': 'f',
        '6': 'g',
        '7': 'h',
        '8': 'i',
        '9': 'j'
    }
    mensaje_decodificado = ""
    
    for caracter in mensaje:
        if caracter.isdigit():
            mensaje_decodificado += clave[caracter]
        else:
            mensaje_decodificado += caracter
    
    return mensaje_decodificado

mensaje_cifrado = "T24st5z7 S9y y9 d5 n15v9 H735 t450p9 q15 n9s v509s N9 p92q15 q14527 p529 b15n9 1st5d s450p25 05 q14s9 0as"
mensaje_descifrado = decodificar_mensaje(mensaje_cifrado.lower())

print(mensaje_descifrado)

