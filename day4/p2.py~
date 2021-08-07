#!/usr/bin/python3

def buscarCID(parametros):
    for i in range(0,len(parametros)):
        if "cid" == parametros[i].split(':')[0]:
            return True
    return False

def cuentaPassaportes():
    pasaportesValidos = 0
    parametros = []
    for i in range(0, len(passaportes)):
        parametros = passaportes[i].split()
        print(str(len(parametros)))
        print(str(parametros))
        if len(parametros) == 8:
            pasaportesValidos = pasaportesValidos + 1
        elif len(parametros) == 7:
            if buscarCID(parametros) == False:
                print("Passaporte Valido")
                pasaportesValidos = pasaportesValidos + 1
    return pasaportesValidos
                
passaportes = []
info = ''
with open('problem.in', 'r') as file:
    contenido = [linea.splitlines() for linea in file]

for i in range(0, len(contenido)):
    print(str(contenido[i]))
    if contenido[i] == ['']:
        passaportes.append(info)
        info = ''
    else:
        if info == '':
            info = info.join(contenido[i])
        else:
            info = info + ' ' + info.join(contenido[i])
passaportes.append(info)

print(str(cuentaPassaportes()))
