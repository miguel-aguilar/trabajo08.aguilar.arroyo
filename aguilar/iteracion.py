print("="*50)
#EJERCICIO 1 - ITERACION
#dar el total de vocales
alumno="AGUILAR VERONA MIGUEL"
vocalA=0
vocalE=0
vocalI=0
vocalO=0
vocalU=0
#iteracion
for letra in alumno:
    if(letra=="A"):
        vocalA+=1
    if(letra=="E"):
        vocalE+=1
    if(letra=="I"):
        vocalI+=1
    if(letra=="O"):
        vocalO+=1
    if(letra=="U"):
        vocalU+=1
    #fin_if
    con=(vocalA+vocalE+vocalI+vocalO+vocalU)
#fin_iterador
print("el total de vocales que hay en mi nombre es: "+ str(con))
print("="*50)
#fin_ejercicio

#EJERCICIO 2 - ITERACION
universidad="PEDRO RUIZ GALLO"
#ITERADOR
for letra in universidad:
    print(letra)
print("="*50)
#fin_iteracion

#EJERCICIO 3 - ITERACION
msg="TEN A TUS AMIGOS CERCA Y A TUS ENEMIGOS MAS CERCA"
token=msg.split(" ")
for item in token:
    print(item)
print("="*50)
#fin_iterador

#EJERCICIO 4 - ITERACION
msg="colmena".upper()
for letra in msg:
    if(letra == "C"):
        print("CUANDO ESCUCHEN")
    if(letra == "O"):
        print("POR UN ALTAVOZ")
    if(letra == "L"):
        print("LA PALABRA DEL MENSAJE")
    if(letra == "M"):
        print("TIENEN QUE")
    if(letra == "E"):
        print("INMEDIATAMENTE ")
    if(letra == "N"):
        print("OCULTARSE PARA NO SER")
    if(letra == "A"):
        print("ASESINADOS POR LOS ALIENIGENAS")
print("="*50)
#fin_iterador

#EJERCICIO 5 - ITERACION
#dar el total de S que hay en la frase
frase="LA VIDA ES MUY SIMPLE PERO INSISTIMOS EN HACERLA COMPLICADA"
letraS=0
for item in frase:
    if(item=="S"):
        letraS+=1
    #fin_if
#fin_iterador
print("el total de letras S son: "+ str(letraS))
print("="*50)
#fin_ejercicio

#EJERCICIO 6 - ITERACION
frase1="QUE VALIENTE TE VES TEMBLANDO DE MIEDO, PERO ARRIESGANDOTE A VIVIRLO"
toker1=frase1.split(" ")
for item in toker1:
    print(item)
    #fin_iterador
print("="*50)

#EJERCICIO 7 - ITERACION
#hallar el total de solamente las letras
frase2="EMPIEZA YA A VIVIR CON GANAS"
token1=frase2.split(" ")
pos=1
lon1=0
for item in token1:
    if(pos==1):
        lon1+=len(item)
    suma=(lon1)
    #fin_if
print("el total de letras son: "+ str(suma))
#fin_iterador
print("="*50)
#fin_ejercicio

#EJERCICIO 8 - ITERACION
operador="MOVISTAR"
for letra in operador:
    print(operador)
#fin_iterador
print("="*50)

#ejercicio 9 - ITERADOR
msg="MI NOTA SUPERO LO DESEADO"
for letra in msg:
    if(letra == "M"):
        print("FELICIDADES")
    if(letra == "N"):
        print("BIEN HECHO")
    if(letra == "S"):
        print("SIGUE ASI")
#fin_iterador
print("="*50)

#EJERCICIO 10 - ITERACION
#cuantas letras desde las B F hay en la frase
frase3="HAY UN FUERZA MOTRIZ MAS PODEROSA QUE EL VAPOR, LA ELECTRICIDAD Y LA ENERGIA ATOMICA: LA VOLUNTAD"
letraB=0
letraC=0
letraD=0
letraE=0
letraF=0
#iteracion
for letra in frase3:
    if(letra=="B"):
        letraB+=1
    if(letra=="C"):
        letraC+=1
    if(letra=="D"):
        letraD+=1
    if(letra=="E"):
        letraE+=1
    if(letra=="F"):
        letraF+=1
    #fin_if
    con1=letraB+letraC+letraD+letraE+letraF
#fin_iterador
print("el numero de letras desde B hasta la F que hay en la frase son: "+ str(con1))
print("="*50)
#fin_ejercicio

#EJERCICIO 11 - ITERACION
frase4="NADA SE OLVIDA MAS DESPACIO QUE UNA OFENSA; Y NADA, MAS RAPIDO QUE UN FAVOR"
token2=frase4.split(" ")
for item in token2:
    print(item)
print("="*50)
#fin_iterador

#EJERCICIO 12 - ITERACION
lenguaje="PHYTON"
for letra in lenguaje:
    print(letra)
#fin_iterador
print("="*50)

#EJERCICIO 13 - ITERACION
mensaje="AMORTIGUAR EL PESO"
for letra in mensaje:
    if(letra == "A"):
        print("tienes")
    if(letra == "M"):
        print("una excelente")
    if(letra == "O"):
        print("comprension")
    if(letra == "R"):
        print("de textos")
#FIN_ITERADOR
print("="*50)

#EJERCICIO 14 - ITERACION
#hallar el total de solamente las letras
frase5="QUIEN REVISA LO QUE NO DEBE. SE ENTERA DE LO QUE NO QUIERE"
token3=frase5.split(" ")
pos1=1
lon2=0
for item1 in token3:
    if(pos1==1):
        lon2+=len(item1)
    suma=(lon2)
    #fin_if
print("el total de letras son: "+ str(suma))
#fin_iterador
print("="*50)

#EJERCICIO 15 - ITERACION
#cuantas letras hay desde la R HASTA U
frase6="INCLUSO LA GENTE QUE AFIRMA QUE NO PODEMOS HACER NADA PARA CAMBIAR NUESTRO DESTINO, MIRA ANTES DE CRUZAR LA CALLE"
letraR=0
letraS=0
letraT=0
letraU=0
#iteracion
for letra in frase6:
    if(letra=="R"):
        letraR+=1
    if(letra=="S"):
        letraS+=1
    if(letra=="T"):
        letraT+=1
    if(letra=="U"):
        letraU+=1
    #fin_if
    con1=(letraR+letraS+letraT+letraU)
#fin_iterador
print("el total de letras que hay desde la R hasta la U es: "+ str(con1))
print("="*50)
