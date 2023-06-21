# Integrantes -> Sebastián Suárez, Steven Erazo

def magico(num):
    if num % 2 == 0:
        return False
    
    if num % 3 != 0:
        return False
    
    suma_digitos = sum(int(digito) for digito in str(num))

    if suma_digitos != 7:
        return False

    return True

def encontrar(inf, sup):

    for num in range(inf, sup + 1):

        if magico(num == True):
            return num
        
    return False


print('\t\t NUMERO MÁGICO\\n\n')
inf = int(input('Dame el limite inferior: '))
sup = int(input('Dame el limite superior: '))

find = encontrar(inf,sup)

if find == False:
    print('No se ha encontrado el número mágico')
else:
    print('El número mágico es: ' ,find)
