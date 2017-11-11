# Modulo registro #
# Max Sebastian Herrera Salazar #
# Octubre 2017 #
# Version 1 #


import random

data = []
data2 = []
length=random.randrange(1,1000)
i=0
while i <= length :
    data.append(random.randrange(150,1000))
    data2.append(random.randrange(1,10000))
    i = i + 1
#print(data)

archivo = open("registro.txt", 'r+')
for i,j in enumerate(data):
    archivo.write(str(data[i])+ ',' + str(data2[i]))
    archivo.write('\n')
archivo.close()