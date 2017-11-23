def longitud():
   numero=input("Dime un numero")
   n_cifras=0
   while numero>0:
        numero=numero/10
        n_cifras=n_cifras+1
   return n_cifras
def reordena_cifras():
