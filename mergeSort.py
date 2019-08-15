from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
 
def geraLista(size):
    vector = []
    while size > 0:
        vector.append(size)
        size-=1
    return vector
  
def geraInversa(size):
  lista=list(range(size,1,-1))
  return lista

def geraOrdenado(size):
	return list(range(size))


def desenhaGrafico(x,y,xl = "Entradas", yl = "Saídas", name='fig'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo Aleatório")
    #ax.plot(x,y2, label = "Melhor Tempo Decrescente")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name+'.png')

operacoes=[]

def mergeSort(vector):

    if len(vector) > 1:
        i = 0
        j = 0
        k = 0
        mid = len(vector) // 2
        r = vector[mid:]
        l = vector[:mid]
        mergeSort(l)
        mergeSort(r)


        while i < len(l) and j < len(r):

            if l[i] < r[j]:
                vector[k] = l[i]
                i=i+1

            if(l[i] > r[j]):
                vector[k] = r[j]
                j=j+1
            k=k+1

        while i < len(l):
            vector[k] = l[i]
            i=i+1
            k=k+1

        while j < len(r):
            vector[k] = r[j]
            k=k+1
            j=j+1
            

listas=[]
listaInversa=[]
listaOrdenada=[]
x2 = [100000, 200000, 400000, 500000, 1000000, 2000000]
y = []
y2=[]
y3=[]

for i in range(len(x2)):
  listas.append(geraLista(x2[i]))
  listaInversa.append(geraInversa(x2[i]))


for i in range(len(x2)):
  y.append(timeit.timeit("mergeSort({})".format(listas[i]),setup="from __main__ import mergeSort",number=1))
  print("Terminou de ordenar um vetor de tamanho " + str(x2[i]) + "...")


print(operacoes[:])

desenhaGrafico(x2,y,'Quantidade','Tempo', 'mergeSort')
