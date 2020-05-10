

def romano_a_entero (numero_romano):
    romanos = {'M':1000,'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    mi_romano = {'M':0,'D':0, 'C':0, 'L':0, 'X':0, 'V':0, 'I':0}
    #orden_romano=romanos.keys()
    orden_romano = {'M':1,'D':2, 'C':3, 'L':4, 'X':5, 'V':6, 'I':7}
    signo_romano = {'M':1,'D':1, 'C':1, 'L':1, 'X':1, 'V':1, 'I':1}
    cod_error=0
    entero = 0
    orden_anterior=1
    rep=1
    letra_anterior="M"
    par=[]
    for letra in numero_romano:
        if letra not in romanos:
            cod_error=1
            return ('no existe ese numero romano')
        
        mi_romano [letra] =  mi_romano [letra] +1
        if mi_romano [letra]>(3*rep) :
            if letra_anterior == letra :
                cod_error=2
                return("no cumple regla 3 repeticiones")
            rep= rep+1

        par= letra_anterior+letra
        if par == "IL" or par == "IC" or par == "ID" or par == "IM" or par == "XD" or par == "XM":
            cod_error=3
            return("resta no permitida")   

        
        if orden_romano [letra]<orden_anterior and letra_anterior != "V" and letra_anterior != "L" and letra_anterior != "D":
                signo_romano [letra_anterior] = -1

        orden_anterior=orden_romano [letra]
        letra_anterior=letra

    valor=0
    signo=0
    if cod_error== 0 :
        for valor, signo in zip (mi_romano, signo_romano):
            entero=entero + (mi_romano[valor]*signo_romano[signo]*romanos[valor])   
       
        return (int (entero))
    else:
        print ("se ha producido un error de tipo: ",cod_error) #no sé como decodificar un diccionario desde el valor y obtener la clave
