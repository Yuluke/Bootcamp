

def romano_a_entero (numero_romano):
    romanos = {'M':1000,'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    mi_romano = {'M':0,'D':0, 'C':0, 'L':0, 'X':0, 'V':0, 'I':0}
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

def decimalizar (numero_entero):
    mi_decimal = {'m':0,'c':0, 'd':0, 'u':0}
    mi_decimal['m'] = int (numero_entero) // 1000
    mi_decimal['c'] = int(numero_entero)-(mi_decimal['m']*1000)
    mi_decimal['c'] = int(mi_decimal['c']) // 100
    mi_decimal['d'] = int(numero_entero)-(mi_decimal['c']*100)-(mi_decimal['m']*1000)
    mi_decimal['d'] = int(mi_decimal['d']) // 10
    mi_decimal['u'] = int(numero_entero)-(mi_decimal['d']*10)-(mi_decimal['c']*100)-(mi_decimal['m']*1000)
    return (mi_decimal)

def encaje_letra_I (mi_decimal,Dec,Roman_M,Roman_m,mi_romano) :
    romanos = {'M':1000,'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    for i in range (mi_decimal[Dec]):
        mi_romano.append(Roman_M)
    over= abs (romanos [Roman_M]- mi_decimal['c']*100 - mi_decimal['d']*10- mi_decimal['u'])
    under=abs (mi_decimal['c']*100 + mi_decimal['d']*10 + mi_decimal['u']-romanos [Roman_m])
    mi_decimal[Dec]=0
    return (over, under, mi_romano, mi_decimal)

def encaje_letra_V (mi_decimal,Dec,Roman_M,Roman_m,mi_romano) :
    romanos = {'M':1000,'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    count=0
    for i in range (mi_decimal[Dec]//5):
        mi_romano.append(Roman_M)
        count +=1
    over= abs (romanos [Roman_M]- mi_decimal['c']*100 - mi_decimal['d']*10- mi_decimal['u'])
    under=abs (mi_decimal['c']*100 + mi_decimal['d']*10 + mi_decimal['u']-romanos [Roman_m])
    mi_decimal[Dec]=mi_decimal[Dec]-(romanos[Roman_M]*count)
    return (over, under, mi_romano, mi_decimal)


def entero_a_romano (numero_entero):
    decimal = {'m':1000,'c':100, 'd':10, 'u':1}
    romanos = {'M':1000,'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    mi_romano=[]

    mi_decimal=decimalizar (numero_entero)
    over, under, mi_romano, mi_decimal = encaje_letra_I (mi_decimal,'m','M','D',mi_romano)
    over_chk=False
    for letra in romanos:
        if over == romanos [letra]:
            mi_romano.append(letra)
            mi_romano.append('M')
            over_chk=True
    
    if over_chk==False:
        over, under, mi_romano, mi_decimal = encaje_letra_V (mi_decimal,'c','D','C',mi_romano)
    over_chk=False
    for letra in romanos:
        if over == romanos [letra]:
            mi_romano.append(letra)
            mi_romano.append('D')
            over_chk=True
    if over_chk==False:
        over, under, mi_romano, mi_decimal = encaje_letra_I (mi_decimal,'c','C','L',mi_romano)

    over_chk=False
    for letra in romanos:
        if over == romanos [letra]:
            mi_romano.append(letra)
            mi_romano.append('C')
            over_chk=True
    if over_chk==False:
        over, under, mi_romano, mi_decimal = encaje_letra_V (mi_decimal,'d','L','X',mi_romano)  

    over_chk=False
    for letra in romanos:
        if over == romanos [letra]:
            mi_romano.append(letra)
            mi_romano.append('L')
            over_chk=True
    if over_chk==False:
        over, under, mi_romano, mi_decimal = encaje_letra_I (mi_decimal,'d','X','V',mi_romano)
    
    over_chk=False
    for letra in romanos:
        if over == romanos [letra]:
            mi_romano.append(letra)
            mi_romano.append('X')
            over_chk=True
    if over_chk==False:
        over, under, mi_romano, mi_decimal = encaje_letra_V (mi_decimal,'u','V','I',mi_romano) 

    over_chk=False
    for letra in romanos: 
        if over == romanos [letra]:
            mi_romano.append(letra)
            mi_romano.append('V')
            over_chk=True
    if over_chk==False:
        over, under, mi_romano, mi_decimal = encaje_letra_I (mi_decimal,'u','I','I',mi_romano) 
    
    mi_romano_txt=''
    mi_romano_txt="".join (mi_romano)
   
    return mi_romano_txt
