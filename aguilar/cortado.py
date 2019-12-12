print("="*50)
#ejercicio 1 - cortado
#cortar la palabra: felicidad
#                 10        20        30        40        50        60
#       01234567890123456789012345678901234567890123456789012345678901234567
frase1="Algunas personas causan felicidad a donde van; otras, cuando se van"
fra1=frase1[24:34] # => devuelve: felicidad
print("la palabra cortada sera: " + fra1)
print("="*50)
#fin_cortado

#ejercicio 2 - cortado
#cortar y formar el mensaje: oigeloc
#                 10        20        30        40        50        60        70        80        90       100       110       120       130
#       0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345
frase2="La amistad no es algo que aprendes en el colegio. Pero si no has aprendido el significado de la amistad realmente no has aprendido nada"
fra2=frase2[47:40:-1] # => devuelve: oigeloc
print("la palabra cortada sera: " + fra2)
print("="*50)
#fin_cortado

#ejercicio 3 - cortado
#cortar y formar el mensaje: construimos y SORUM
#                 10        20        30        40        50        60
#       012345678901234567890123456789012345678901234567890123456789012345
frase3="Los hombres construimos demasiados muros y no suficientes puentes"
cor1=frase3[12:23] # => devuelve: construimos
cor2=frase3[41] # => devuelve: Y
cor3=frase3[39:34:-1].upper() # => devuelve: sorum
fra3=cor1 + " " + cor2 + " " + cor3
print("el mesaje cortado sera: " + fra3)
print("="*50)
#fin_cortado

#ejercicio 4 - cortado
#cortar y formar el mensaje: fanatico e INCURABLE
#                 10        20        30        40        50        60        70
#       0123456789012345678901234567890123456789012345678901234567890123456789012
frase4="Cuando el fanatismo ha gangregado el cerebro, la enfermedad es incurable"
cor4=frase4[10:16] # => devuelve: fanati
cor5=frase4[65] # => devuelve: c
cor6=frase4[5:8]  # => devuelve: o e
cor7=frase4[63:].upper() # => devuelve: INCURABLE
fra4=cor4 + cor5 + cor6 + " " + cor7
print("el mesaje cortado sera: " + fra4)
print("="*50)
#fin_cortado

#ejercicio 5 - cortado
#cortar y formar el mensaje: gallo nacional
#                 10        20        30
#       0123456789012345678901234567890123456789
frase5="UNIVERSIDAD NACIONAL 'PEDRO RUIZ GALLO'"
cor8=frase5[33:38].lower() # => devuelve: gallo
cor9=frase5[12:20].lower() # => devuelve: nacional
fra5=cor8 + " " + cor9
print("el mesaje cortado sera: " + fra5)
print("="*50)
#fin_cortado

#ejercicio 6 - cortado
#cortar y formar el mensaje: SISILANA
#                 10        20        30
#       01234567890123456789012345678901234567
frase6="introduccion al 'analisis matematico'"
cor10=frase6[24:16:-1].upper() # => devuelve: SISILANA
fra6=cor10
print("la palabra cortada sera: " + fra6)
print("="*50)
#fin_cortado

#ejercicio 7 - cortado
#cortar y formar el mensaje: escuela ACINOR
#                 10        20        30        40
#       01234567890123456789012345678901234567890123
frase7="Escuela profesional: Ingieneria Electronica"
cor11=frase7[0:7].lower() # => devuelve: escuela
cor12=frase7[42:36:-1].upper() # => devuelve: ACINOR
fra7=cor11 +" "+ cor12
print("el mesaje cortado cortado sera: " + fra7)
print("="*50)
#fin_cortado

#ejercicio 8 - cortado
#cortar y formar el codigo: AENV NOC
#                 10        20        30        40        50        60        70        80        90
#       0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123
frase8="Nunca discutas con un estupido, te hara descender a su nivel y ahi te vencera por experiencia"
cor13=frase8[76:69:-2].upper() # => devuelve: AENV
cor14=frase8[17:14:-1].upper() # => devuelve: NOC
fra8=cor13 +" " +  cor14
print("el codigo cortado cortado sera: " + fra8)
print("="*50)
#fin_cortado

#ejercicio 9 - cortado
#cortar y formar el mensaje: ACTUAR
#                 10        20        30        40        50        60
#       0123456789012345678901234567890123456789012345678901234567890123456
frase9="La obra maestra de la injusticia es parecer justo aunque no lo sea"
cor15=frase9[31:24:-2].upper() # => devuelve: ACTU
cor16=frase9[14:12:-1].upper() # => devuelve: AR
fra9=cor15 + cor16
print("el mesaje cortado sera: " + fra9)
print("="*50)
#fin_cortado

#ejercicio 10 - cortado
#cortar y formar el mensaje: nunca cuestione todo
#                 10        20        30        40        50        60        70
#        01234567890123456789012345678901234567890123456789012345678901234567890123456789
frase10="Nunca fui consiente de cualquier otra opcion que no fuera la de cuestionar todo"
cor17=frase10[0:6].lower() # => devuelve: nunca
cor18=frase10[64:72] # => devuelve: cuestion
cor19=frase10[18]  # => devuelve: e
cor20=frase10[74:] # => devuelve: todo
fra10=cor17 + cor18 + cor19  + cor20
print("el mesaje cortado sera: " + fra10)
print("="*50)
#fin_cortado

#ejercicio 11 - cortado
#cortar y formar el mensaje: TIENE PENSAMIENTOS GRANDES
#                 10        20        30        40        50        60
#        01234567890123456789012345678901234567890123456789012345678901234
frase11="El que tiene grandes pensamientos, menudo comete grandes errores"
cor21=frase11[7:13].upper() # => devuelve: TIENE
cor22=frase11[21:33].upper() # => devuelve: PENSAMIENTOS
cor23=frase11[48:56].upper()  # => devuelve: GRANDES
fra11=cor21 + cor22 + cor23
print("el mesaje cortado sera: " + fra11)
print("="*50)
#fin_cortado

#ejercicio 12 - cortado
#cortar y formar el mensaje: amo los perros
#                 10        20        30        40        50
#        012345678901234567890123456789012345678901234567890123456789
frase12="EL AMOR NO TIENE CURA, PERO ES LA CURA PARA TODOS LOS MALES"
cor24=frase12[3:6].lower() # => devuelve: amo
cor25=frase12[49:54].lower() # => devuelve: los
rep=frase12.replace("PERO","PERROS")
cor26=rep[23:29].lower()  # => devuelve: perros
fra12=cor24 + cor25 + cor26
print("el mesaje cortado sera: " + fra12)
print("="*50)
#fin_cortado

#ejercicio 13 - cortado
#cortar y formar el mensaje: DEBES VIVIR
#                 10        20        30        40        50        60
#        012345678901234567890123456789012345678901234567890123456789012345678
frase13="La vida debe ser comprendida hacia atras. Pero vivida hacia adelante"
cor27=frase13[8:12].upper() # => devuelve: DEBE
cor28=frase13[13].upper() # => devuelve: S
rep1=frase13.replace("vivida","vivir")
cor29=rep1[47:52].upper()  # => devuelve: VIVIR
fra13=cor27+cor28+" "+cor29
print("el mesaje cortado sera: " + fra13)
print("="*50)
#fin_cortado

#ejercicio 10 - cortado
#cortar y formar el mensaje: NECESITAMOS DINERO
#                 10        20        30        40        50        60        70
#        0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901
frase14="gastamos dinero que no tenemos, en cosas que no necesitamos, para impresionar a gente a la que no le importamos"
cor30=frase14[48:59].upper() # => devuelve: NECESITAMOS
cor31=frase14[8:15].upper() # => devuelve:  DINERO
fra14=cor30 + cor31
print("el mesaje cortado sera: " + fra14)
print("="*50)
#fin_cortado

#ejercicio 15 - cortado
#cortar y formar el mensaje: EL SABIO OPINA
#                 10        20        30        40        50
#        012345678901234567890123456789012345678901234567890
frase15="EL SABIO QUIERE CAMBIAR DE OPINION, EL NECIO NUNCA"
cor32=frase15[0:9] # => devuelve: EL SABIO
rep3=frase15.replace("OPINION","opina")
cor33=rep3[27:32].upper() # => devuelve: OPINA
fra15=cor32 + cor33
print("el mesaje cortado sera: " + fra15)
print("="*50)
#fin_cortado
