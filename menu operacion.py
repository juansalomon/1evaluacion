def menu_operacion():
    seguir="si"
    num1=input("Dime un numero: ")
    num2=input("Dime otro numero: ")
    while (seguir=="si"):
        print ("Que deseas hacer con los numeros?: ")
        print ("1. Sumarlos")
        print ("2. Restarlos")
        print ("3. Multiplicarlos")
        print ("4. Dividirlos")
        respuesta=input()
        if (respuesta==1):
            suma=num1+num2
            print "La suma es igual a ", suma
        if (respuesta==2):
            resta=num1-num2
            print "La resta es igual a ", resta
        if (respuesta==3):
            multiplicacion=num1*num2
            print "La multiplicacion es igual a ", multiplicacion
        if (respuesta==4):
            division=num1/num2
            print "La division es igual a ", division
            
        
menu_operacion()
