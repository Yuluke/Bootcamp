romanos = {'M':1000,'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
error = {'mas de 3 repticiones':1}

mi_romano = {'M':0,'D':0, 'C':0, 'L':0, 'X':0, 'V':0, 'I':0}


r2d =input('Introduce tu dígito Romano: ')
cod_error=0
entero = 0
for letra in r2d:
    if letra in romanos:
        entero = entero + romanos [letra]
        mi_romano [letra] =  mi_romano [letra] +1
        if mi_romano [letra] >3 :
            print ("no cumple regla 3 repeticiones")
            cod_error=1
            break
    else:
        print ('nro romano no valido')
        
if cod_error== 0 :
    print (mi_romano)
    print ('tu número decimal es: ', entero)
else:
    print ("se ha producido un error de tipo: ",cod_error) #no sé como decodificar un diccionario desde el valor y obtener la clave



#for i in romanos.items():
   # div=r2d // romanos.items [i]
   # print (div)