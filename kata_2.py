class subest():
    def __init__(self,nombr, circuit, tens):
       self.nombre=nombr
       self.circuito=circuit
       self.tension=tens
    
    def segmentos (self):
        self.S=self.circuito*3
        print (self.S)
        return self.S

    
    def __str__ (self):
        return "subestacion {} con {} circuitos de {} kv".format( self.nombre, self.circuito, self.tension)

bolarque=subest('bolarque',1,2)

print (bolarque)
print (bolarque.circuito)
print (bolarque.tension)
#print (bolarque.S) #¿porque no funciona esto? quiero sacar S como un parametro de la clase
S=bolarque.segmentos() 
print (S)

