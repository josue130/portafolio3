def sumatoriaF(inicio,fin):
     if isinstance(inicio,int) and isinstance(fin,int):
          return sumatoriaF_aux(inicio,fin,0)
     else:
          print("Error en los parametros de entrada")
def sumatoriaF_aux(inicio,fin,res):
     for i in range(inicio,fin+1):
          res+=i
     return res
