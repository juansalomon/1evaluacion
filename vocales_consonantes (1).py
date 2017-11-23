def vocales_consonantes():
    nombre=raw_input("Dime una palabra")
    print "Esa palabra tiene",len(nombre),"letras"
    vocales=0
    for cont in range(0,len(nombre),1):
        if nombre[cont]=='a'or nombre[cont]=='e'or nombre[cont]=='i' or nombre[cont]=='o'or nombre[cont]=='u':
            vocales = vocales+1
    print "de las cuales",vocales ,"son vocales y",len(nombre)-vocales,"consonantes"
vocales_consonantes()
