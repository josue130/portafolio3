#Matriz Simétirca

def matrizSimetrica(matriz):
    if isinstance(matriz,list) and (matriz!=[]):
        if len(matriz)==len(matriz[0]):
            return AuxSimetrica(matriz)
        else:
            print("La matriz no es cuadrada")
    else:
        print("Error en parámetros de entrada")
def AuxSimetrica(matriz):
    if matriz==transpuesta(matriz):
        return ("Sime")
    elif matriz!=transpuesta(matriz):
        return ("anti")
                             
#transpuesta    
def transpuesta(matriz):
    if isinstance (matriz,list) and (matriz!=[]):
        if largo(matriz)==largo(matriz[0]):
            return Transpuesta_aux(matriz,0,0,[],[])
        else:
            print("Error la matriz no es cuadrada")
    else:
        print("Error en parámetros de entrada")


def Transpuesta_aux(m,filas,columnas,lista_temp,res):
    if filas==largo(m):
        return Transpuesta_aux(m,0,columnas+1,[],res+[lista_temp])
    if columnas==largo(m[0]):
        return res
    else:
        if m[filas][columnas]:
            return Transpuesta_aux(m,filas+1,columnas,lista_temp+[m[filas][columnas]],res)
        else:
            print("Error en parámetros")
