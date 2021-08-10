#!/usr/bin/python3

def busca2020():
    for i in range(0,len(Lista_de_numeros)):
        for j in range(0,len(Lista_de_numeros)):
            for k in range(0,len(Lista_de_numeros)):
                if (Lista_de_numeros[i] + Lista_de_numeros[j] + Lista_de_numeros[k]) == 2020:
                    print(str(Lista_de_numeros[i])+" - "+str(Lista_de_numeros[j])+" - "+str(Lista_de_numeros[k]))
                    return Lista_de_numeros[i] * Lista_de_numeros[j] * Lista_de_numeros[k]

Lista_de_numeros = []
with open('problem.in', 'r') as file:
    Lista_de_numeros = [int(linea) for linea in file]

print(str(busca2020()))
