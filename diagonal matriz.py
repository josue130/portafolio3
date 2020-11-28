def diagonal(matriz):
     if isinstance(matriz,list):
          return diagonal_aux(matriz,0,0,[])
     else:
          print("El resultado tiene que ser una matriz")
def diagonal_aux(matriz,fila,columnas,new):
     if fila==len(matriz):
          return new
     else:
          return diagonal_aux(matriz,fila+1,columnas+1,new + [matriz[fila][columnas]])
