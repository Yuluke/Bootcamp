

def romano_a_entero (numero_romano):
    romanos = {'M':1000,'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    mi_romano = {'M':0,'D':0, 'C':0, 'L':0, 'X':0, 'V':0, 'I':0}
    #orden_romano=romanos.keys()
    orden_romano = {'M':1,'D':2, 'C':3, 'L':4, 'X':5, 'V':6, 'I':7}
    cod_error=0
    entero = 0
    orden_anterior=1
    for letra in numero_romano:
        if letra in romanos:
            entero = entero + romanos [letra]
            mi_romano [letra] =  mi_romano [letra] +1
            if mi_romano [letra]>3:
                cod_error=2
                return("no cumple regla 3 repeticiones")
        else:
            cod_error=3
            return ('no existe ese numero romano')
        
        if orden_romano [letra]<orden_anterior:
                cod_error=1
                return("no cumple orden")
        orden_anterior=orden_romano [letra]    
        
    if cod_error== 0 :
        
        return (int (entero))
    else:
        print ("se ha producido un error de tipo: ",cod_error) #no sé como decodificar un diccionario desde el valor y obtener la clave
