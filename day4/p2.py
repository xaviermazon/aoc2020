#!/usr/bin/python3

import re

def validarPID(parametros):
    for i in range(0,len(parametros)):
        if "pid" == parametros[i].split(':')[0]:
            return bool(re.search("^[0-9]{9}$", parametros[i].split(':')[1]))
    return False

def validarECL(parametros):
    for i in range(0,len(parametros)):
        if "ecl" == parametros[i].split(':')[0]:
            color = parametros[i].split(':')[1]
            if color == "amb" or color == "blu" or color == "brn" or color == "gry" or color == "grn" or color == "hzl" or color == "oth":
                return True
    return False

def validarHCL(parametros):
    for i in range(0,len(parametros)):
        if "hcl" == parametros[i].split(':')[0]:
            try:
                regex = str(re.search("^#[0-9a-f]{6}$", parametros[i].split(':')[1]).span())
                if "(0, 7)" == regex:
                    return True
                else:
                    return False
            except AttributeError:
                return False
    return False

def validarHGT(parametros):
    for i in range(0,len(parametros)):
        if "hgt" == parametros[i].split(':')[0]:
            print(str(parametros[i]))
            if len(parametros[i].split(':')[1]) == 5 and parametros[i].split(':')[1][-1] == 'm':
                height = int(parametros[i].split(':')[1].split('cm')[0])
                if height >= 150 and height <= 193:
                    return True
                else:
                    return False
            elif len(parametros[i].split(':')[1]) == 4 and parametros[i].split(':')[1][-1] == 'n':
                height = int(parametros[i].split(':')[1].split('in')[0])
                if height >= 59 and height <= 76:
                    return True
                else:
                    return False
            else:
                return False
    return False

def validarEYR(parametros):
    for i in range(0,len(parametros)):
        if "eyr" == parametros[i].split(':')[0]:
            if int(parametros[i].split(':')[1]) >= 2020 and int(parametros[i].split(':')[1]) <= 2030:
                return True
    return False

def validarIYR(parametros):
    for i in range(0,len(parametros)):
        if "iyr" == parametros[i].split(':')[0]:
            if int(parametros[i].split(':')[1]) >= 2010 and int(parametros[i].split(':')[1]) <= 2020:
                return True
    return False

def validarBYR(parametros):
    for i in range(0,len(parametros)):
        if "byr" == parametros[i].split(':')[0]:
            if int(parametros[i].split(':')[1]) >= 1920 and int(parametros[i].split(':')[1]) <= 2002:
                return True
    return False

def buscarCID(parametros):
    if len(parametros) == 8:
        return False
    if len(parametros) == 7:
        for i in range(0,len(parametros)):
            if "cid" == parametros[i].split(':')[0]:
                return True
    if len(parametros) < 7:
        return True
    return False

def cuentaPassaportes():
    pasaportesValidos = 0
    parametros = []
    for i in range(0, len(passaportes)):
        parametros = passaportes[i].split()
        if buscarCID(parametros) == False and validarBYR(parametros)==True and validarIYR(parametros)==True and validarEYR(parametros)==True and validarHGT(parametros)==True and validarHCL(parametros)==True and validarECL(parametros)==True and validarPID(parametros)==True:
            print(str(passaportes[i]))
            pasaportesValidos = pasaportesValidos + 1
            print(str(pasaportesValidos))
        else:
            print("Passaporte Invalido")
    return pasaportesValidos
                
passaportes = []
info = ''
with open('problem.in', 'r') as file:
    contenido = [linea.splitlines() for linea in file]

for i in range(0, len(contenido)):
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
