def saludador():
    h=input("Dime que hora es:?")
    if(h>=6 and h<14):
        print "Buenos dias"
    if(h>=14 and h<20):
        print "Buenas tardes"
    if((h>=20 and h<=24)or(h>=0 and h<6)):
        print "Buenas noches"
saludador()
