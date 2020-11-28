def largo(lista):
    if isinstance(lista,list):
        return largo_Aux(lista,0)
    else:
        return "Error"
def largo_Aux (lista, cont):
    if lista == []:
        return cont
    else:
        return largo_Aux (lista [1:], cont + 1)

def sumaMatrices (matriz, matriz2):
    if matriz == [] and matriz2 == []:
        return []
    elif largo(matriz) != largo(matriz2):
        return "Error, la cantidad de los elementos debe ser igual"
    else:
        return Suma_aux(matriz, matriz2, 0, [])


def Suma_aux(matriz, matriz2, filas, res):
    if filas == largo(matriz):
        return res
    else:
        suma = suma_matrices(matriz[filas], matriz2[filas], 0)
        return Suma_aux(matriz, matriz2, filas + 1, res + [suma])


def suma_matrices(lista, lista2, filas):
    if filas == largo(lista):
        return []
    else:
        return [lista [filas] - lista2 [filas]] + suma_matrices(lista, lista2, filas + 1)
