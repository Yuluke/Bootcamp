import romanos

convert = input ("Elige conversión: r2d o d2r: ")
if convert=='r2d':
    r2d =input('Introduce tu dígito Romano: ')
    print ("Tu romano es en decimal: ", romanos.romano_a_entero (r2d))
elif convert=='d2r':
    d2r= input("introduce tu numero entero: ")
    print ('tu numero de decimal es: ', romanos.entero_a_romano(d2r))
else:
    print ('elección errónea')