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


def multiplicarMatrices(matriz, matriz2):
    if isinstance(matriz, list) and (matriz != []) and isinstance(matriz2, list) and (matriz2 != []):
        if largo(matriz[0]) != largo(matriz2):
            return "Error en las matrices"
        else:
            return multiplicarMatrices_aux(matriz, matriz2, 0, [])
    else:
        return "Error los parametros de entrada"


def multiplicarMatrices_aux(matriz, matriz2, cont, res):
    if cont == largo(matriz):
        return res
    else:
        res += [multiplicarFilaMatriz(matriz[cont], matriz2)]
        return multiplicarMatrices_aux(matriz, matriz2, cont + 1, res)


def obtenerColumna(matriz, indice, conti):
    if conti == largo(matriz):
        return []
    else:
        return [matriz[conti][indice]] + obtenerColumna(matriz, indice, conti + 1)


def multiplicarFilaColumna(filas, columnas, cont):
    if cont == largo(filas) and cont == largo(columnas):
        return 0
    else:
        return filas[cont] * columnas[cont] + multiplicarFilaColumna(filas, columnas, cont + 1)


def multiplicarFilaMatriz(filas, matriz):
    return multiplicarFilaMatriz_aux(filas, matriz, 0, largo(matriz[0]), [])


def multiplicarFilaMatriz_aux(filas, matriz, columnas_actual, total, res):
    if columnas_actual == total:
        return res
    else:
        columnas = obtenerColumna(matriz, columnas_actual, 0)
        res += [multiplicarFilaColumna(filas, columnas, 0)]
        return multiplicarFilaMatriz_aux(filas, matriz, columnas_actual + 1, total, res)

     
               
          
          
