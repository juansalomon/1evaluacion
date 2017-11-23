def mayor(num1,num2):
    if (num1>num2):
        respuesta=num1
    else:
        respuesta=num2
    return respuesta
def comparador_principal():
    num1=input("Dime un numero: ")
    num2=input("Dime otra numero: ")
    print mayor(num1,num2)
comparador_principal()
    
