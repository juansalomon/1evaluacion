def dni():
    numero = input("Introduzca los n�meros de su DNI ")
    intnumero = int(numero)
    diccionario = {0:"T",1:"R",2:"W",3:"A",4:"G",5:"M",6:"Y",7:"F",8:"P",9:"D",10:"X",
               11:"B",12:"N",13:"J",14:"Z",15:"S",16:"Q",17:"V",18:"H",19:"L",
               20:"C",21:"K",22:"E"}
    resto = intnumero%23
    letra = diccionario[resto]
 
    print("Su letra del DNi es", letra,  "Y su n�mero completo,", numero, letra)

dni()
