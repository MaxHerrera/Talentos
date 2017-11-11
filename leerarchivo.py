# Modulo de lectura de txt #
# Max Sebastian Herrera Salazar #
# Octubre 2017 #
# version 1 #

import matplotlib.pyplot as plt

archivo = open("EBIKE.txt", 'r')
cadencia = []
seg = []
cont = 0
for linea in archivo:
    columnas = linea.split(',')
    try:
        #print(columnas[3])
        cadencia.append(int(columnas[3]))
        seg.append(cont)
    except IndexError:
        continue
    except ValueError:
        continue
    cont = cont +1

#print(cadencia)
cad = []
for linea,columnas in enumerate(cadencia):
    try :
        cad.append((1/cadencia[linea])*60000)
    except ZeroDivisionError:
        cad.append(0)
    print("Velocidad de pedaleo: " + str(cad[linea]) + " RPM")

#plt.figure(num=1, )
plt.plot(seg,cad)
plt.show()