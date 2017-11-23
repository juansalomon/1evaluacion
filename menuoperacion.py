def menu_operacion():
    Seguir="Si"
    num1=input("Dime un numero: ")
    num2=input("Dime otro numero: ")
    while (seguir=="Si"):
        print "Que deseas hacer con los numeros: "
        print "1.Devolver la suma de las cifras pares"
        print "2.Devolver la suma de las cifras impares"
        print "3.Devolver la mayor de las cifras"
        print "4.Devolver un numero con las mismas cifras ordenadas de menor a mayor"
        respuesta=input()
    if(respuesta==1):
        suma=0
        n_pares=0
        n_impares=0
        numero=input("Dime un numero")
        while numero>0:
        cifra=numero%10
        if cifra%2==0:
            n_pares=n_pares+1
        else:
            n_impares=n_impares+1
        numero+numero/10
        print "Tiene", n_pares, "cifras pares"
    if(respuesta==2):
        suma=0
        n_pares=0
        n_impares=0
        numero=input("Dime un numero")
        while numero>0:
        cifra=numero%10
        if cifra%2==0:
            n_pares=n_pares+1
        else:
            n_impares=n_impares+1
        numero+numero/10
        print "Tiene", n_impares, "cifras impares"
    
menu_operacion()
