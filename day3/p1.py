#!/usr/bin/python3

def cuentaArboles(down, right):
    arbolesEncontrados = 0
    j = 0
    for i in range(0, len(terreno)):
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
with open('sample.in', 'r') as file:
    terreno = [linea.rstrip('\n') for linea in file]

print(str(cuentaArboles(1,1)*cuentaArboles(1,3)*cuentaArboles(1,5)*cuentaArboles(1,7)*cuentaArboles(2,1)))
