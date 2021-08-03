#!/usr/bin/python3

def cuentaArboles(down, right):
    arbolesEncontrados = 0
    j = 0
    for i in range(0, len(terreno),down):
        i = i + down
        j = j + right
        print(str(len(terreno))+" - "+ str(i) +" - "+ str(j))
        if len(terreno) <= i:
            return arbolesEncontrados
        if len(terreno[i]) <= j:
            j = j - len(terreno[i])
        if terreno[i][j] == '#':
            arbolesEncontrados = arbolesEncontrados + 1
    return arbolesEncontrados
                
terreno = []
with open('problem.in', 'r') as file:
    terreno = [linea.rstrip('\n') for linea in file]

salto11=cuentaArboles(1,1)
salto13=cuentaArboles(1,3)
salto15=cuentaArboles(1,5)
salto17=cuentaArboles(1,7)
salto21=cuentaArboles(2,1)
print(str(salto11*salto13*salto15*salto17*salto21))
