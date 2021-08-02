#!/usr/bin/python3

def validadorContrasenas():
    passValid = 0
    cantidad, carac, password = [], [], []
    for i in range(0, len(Lista_de_contrasenas)):
        cantidad, carac, password = Lista_de_contrasenas[i].split()
        minimo, maximo = cantidad.split('-')
        if (password[int(minimo)-1] == carac[0]) ^ (password[int(maximo)-1] == carac[0]):
            passValid = passValid + 1
    return passValid
                
Lista_de_contrasenas = []
with open('problem.in', 'r') as file:
    Lista_de_contrasenas = [linea.rstrip('\n') for linea in file]

print(str(validadorContrasenas()))
