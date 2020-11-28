def largo(lista):
    if isinstance(lista,list):
        return largo_Aux(lista,0)
    else:
        return "Error"
def largo_Aux(lista, cont):
    if lista == []:
        return cont
    else:
        return largo_Aux(lista [1:], cont+ 1)

        
def sumar_columnas (matriz):
    if isinstance (matriz, list) and (matriz != []):
        return sumar_columnas_aux (matriz, 0, 0, 0, [])
    else:
        return "Error, el elemento de entrada es inválido"

    
def sumar_columnas_aux (matriz, filas, columnas, suma, res):
    if columnas == largomatriz [0], 0):
        return res
    if filas == largo(matriz, 0):
        return sumar_columnas_aux (matriz, 0, columnas + 1, 0, res + [suma])
    else:
        suma += matriz[filas][columnas]
        return sumar_columnas_aux (matriz, filas + 1, columnas, suma, res)
