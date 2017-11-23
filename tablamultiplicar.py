def multiplicador():
    n= input ("Dime la tabla de multiplicar que deseas: ")
    print "Tabla del ",n
    for cont in range (1,11,1):
         print n,"x",cont,"=",n*cont
multiplicador()
