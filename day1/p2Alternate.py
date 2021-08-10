#!/usr/bin/python3

def partition(low, high):
    pivote = Lista_de_numeros[low];
    i = low + 1;
    j = high;
    while i < j + 1:
        while i < j + 1 and Lista_de_numeros[i] <= pivote: i += 1
        while i < j + 1 and Lista_de_numeros[j] >= pivote: j -= 1
        if i < j + 1: Lista_de_numeros[i], Lista_de_numeros[j] = Lista_de_numeros[j], Lista_de_numeros[i]
    Lista_de_numeros[low], Lista_de_numeros[j] = Lista_de_numeros[j], Lista_de_numeros[low]
    return j
  
def quickSort(low, high):
    if low < high:
        pi = partition(low, high)
        quickSort(low, pi-1)
        quickSort(pi+1, high)

def busquedaDicotomica(x,minimo,maximo):
    print(str(x)+" - "+str(Lista_de_numeros[minimo])+" - "+str(Lista_de_numeros[maximo]))
    ans = 0
    if x < Lista_de_numeros[0] or x > Lista_de_numeros[-1]: return 0
    elif x == Lista_de_numeros[minimo]: return Lista_de_numeros[minimo]
    elif x == Lista_de_numeros[maximo]: return Lista_de_numeros[maximo]
    elif minimo==maximo: ans = 0
    else: 
        i = (minimo+((maximo-minimo)//2))        
        if x < Lista_de_numeros[i]: ans = busquedaDicotomica(x,minimo,i)
        elif x > Lista_de_numeros[i]: ans = busquedaDicotomica(x,i+1,maximo)  
        else: ans = Lista_de_numeros[i]
    return ans

def busca2020():
    for i in range(0,len(Lista_de_numeros)):
        if (Lista_de_numeros[i]) == 2020/3: return Lista_de_numeros[i] * 3
        else:
            for j in range(0,len(Lista_de_numeros)):
                num = busquedaDicotomica(2020 - (Lista_de_numeros[i] + Lista_de_numeros[j]), 0, len(Lista_de_numeros)-1)
                if (Lista_de_numeros[i] + Lista_de_numeros[j] + num) == 2020:
                    print(str(i)+" - "+str(j)+" - "+str(num))
                    return Lista_de_numeros[i] * Lista_de_numeros[j] * num

Lista_de_numeros = []
with open('problem.in', 'r') as file:
    Lista_de_numeros = [int(linea) for linea in file]

quickSort(0,len(Lista_de_numeros)-1)

print(str(busca2020()))
