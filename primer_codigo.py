of=3
a=of
b=0
lista=[]
listb=[]
listc=[] #lista
listd={} #diccionario
def printlist(list):
    long=len(list)
    i=0
    for i in range(long):
        print (list[i],end=" ")
    print ("")    
    return (long)
while a<10:
  
    if b<a:
        print ("todavia soy pequeño")
    else:
        print ("ya soy mayor")
    
    lista.append(a)
    lista.append(b)
    c=a,b #sto es una tupla
    d=a,b,a,b  #esto también funciona
    listb.append(c) #se hace una lista de listas pero cada "listando" crece a la vez que lista
        
    b=b+2
    a +=1 
    
print ("a es ",a," y b es ",b)

long=printlist (lista)
print ("long=",long)

printlist (lista[:4]) #desde comeienzo hasta

printlist (lista[4:8])#entre

printlist (lista[4:])#desde hasta fin

ulti=lista[-1] #ultimo
penulti = lista[-2] #penultimo
print (ulti, penulti, lista [-2:])

final = {'penulti':lista[-2], 'ulti':lista [-1]} #diccionario
print (final)

print (listb)
printlist(listb)

print (final['penulti'])

listd= listb #hacer una lista disccionario ¿como usar beneficios del diccionario?


