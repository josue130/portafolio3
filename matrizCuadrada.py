def matrizCuadrada(matriz):
     if isinstance(matriz,list):
          return MC_aux(matriz,0,0,0,0),MC_aux2(matriz,0,0,0,0)
     else:
          print("Error en parametro de entrada")

def MC_aux(matriz,fila,columna,filasv2,columnav2):
     if filasv2==len(matriz):
          return True
     if fila==len(matriz):
          return MC_aux(matriz,0,columna+1,filasv2+1,0)
     else:
          if matriz[filasv2][columnav2]==matriz[fila][columna]:
               return MC_aux(matriz,fila+1,columna,filasv2,columnav2+1)
          else:
               return False
def MC_aux2(matriz,fila,columna,filasv2,columnav2):
     if filasv2==len(matriz):
          return True
     if fila==len(matriz):
          return MC_aux(matriz,0,columna+1,filasv2+1,0)
     else:
          if abs(matriz[filasv2][columnav2])==abs(matriz[fila][columna]):
               return MC_aux(matriz,fila+1,columna,filasv2,columnav2+1)
          else:
               return False
