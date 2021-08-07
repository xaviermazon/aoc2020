#!/usr/bin/python3

def validarPID(parametros):
    for i in range(0,len(parametros)):
        if "pid" == parametros[i].split(':')[0]:
            print("pid -> " + parametros[i].split(':')[1])
            if int(parametros[i].split(':')[1]) < 1000000000:
                return True
    return False

def validarECL(parametros):
    for i in range(0,len(parametros)):
        if "ecl" == parametros[i].split(':')[0]:
            print("ecl -> " + parametros[i].split(':')[1])
            color = parametros[i].split(':')[1]
            if color == "amb" or color == "blu" or color == "brn" or color == "gry" or color == "grn" or color == "hzl" or color == "oth":
                return True
    return False

def validarHCL(parametros):
    for i in range(0,len(parametros)):
        if "hcl" == parametros[i].split(':')[0]:
            if parametros[i].split(':')[1][0] == '#':
                print("hcl -> " + parametros[i].split(':')[1])
                return True
    return False

def validarHGT(parametros):
    for i in range(0,len(parametros)):
        if "hgt" == parametros[i].split(':')[0]:
            print("hst -> " + parametros[i].split(':')[1])
            if len(parametros[i].split(':')[1]) == 5:
                height = int(parametros[i].split(':')[1].split('cm')[0])
                if height >= 150 and height <= 193:
                    return True
            else:
                height = int(parametros[i].split(':')[1].split('in')[0])
                if height >= 59 and height <= 76:
                    return True
    return False

def validarEYR(parametros):
    for i in range(0,len(parametros)):
        if "eyr" == parametros[i].split(':')[0]:
            if int(parametros[i].split(':')[1]) >= 2020 and int(parametros[i].split(':')[1]) <= 2030:
                print("eir -> " + parametros[i].split(':')[1])
                return True
    return False

def validarIYR(parametros):
    for i in range(0,len(parametros)):
        if "iyr" == parametros[i].split(':')[0]:
            if int(parametros[i].split(':')[1]) >= 2010 and int(parametros[i].split(':')[1]) <= 2020:
                print("iyr -> " + parametros[i].split(':')[1])
                return True
    return False

def validarBYR(parametros):
    for i in range(0,len(parametros)):
        if "byr" == parametros[i].split(':')[0]:
            if int(parametros[i].split(':')[1]) >= 1920 and int(parametros[i].split(':')[1]) <= 2002:
                print("byr -> " + parametros[i].split(':')[1])
                return True
    return False

def buscarCID(parametros):
    if len(parametros) == 8:
        return True
    if len(parametros) == 7:
        for i in range(0,len(parametros)):
            if "cid" == parametros[i].split(':')[0]:
                print("cid -> " + parametros[i].split(':')[1])
                return True
    return False

def cuentaPassaportes():
    pasaportesValidos = 0
    parametros = []
    for i in range(0, len(passaportes)):
        parametros = passaportes[i].split()
        print(str(parametros))
        if buscarCID(parametros) == False and validarBYR(parametros)==True and validarIYR(parametros)==True and validarEYR(parametros)==True and validarHGT(parametros)==True and validarHCL(parametros)==True and validarECL(parametros)==True and validarPID(parametros)==True:
            print("Passaporte Valido")
            pasaportesValidos = pasaportesValidos + 1
        else:
            print("Passaporte Invalido")
    return pasaportesValidos
                
passaportes = []
info = ''
with open('sample2p2.in', 'r') as file:
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
