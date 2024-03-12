import numpy as np
import matplotlib.pyplot as plt
global numEs
numEs = 2

def printEsercizio(text,numEs):
    numEs = numEs +1
    print('Esercizion numero '+str( numEs))
    print(text)
    return numEs

tuttiTrue = np.ones((3,3),dtype=bool)
print(tuttiTrue)
numEs = printEsercizio('tutti true',numEs)

arr = np.array([0,1,2,3,4,5,6,7,8,9])
arrBool = (arr % 2 == 1)
arrBool = arrBool.astype(bool)

numEs = printEsercizio('Dispari',numEs)
print(arrBool)


print(arr[arrBool])

numEs = printEsercizio('Sostituisci i dispari con -1',numEs)
#arr[arrBool] = -1


#  (Commento il precedente)

vettCopia = arr.copy()
vettCopia[arrBool] = -1
numEs = printEsercizio('Fallo senza modificare l\'originale',numEs)
print(vettCopia)
print(arr)

numEs = printEsercizio('Converti un array 1D in un array 2D con 2 righe',numEs)
arrayPatenza = np.arange(10)
arrayPatenza = arrayPatenza.reshape((2,-1))
print(arrayPatenza)

a = np.arange(10).reshape(2,-1)
b = np.repeat(1,10).reshape(2,-1)
concatenati = np.concatenate([a,b])
numEs = printEsercizio('impila array a b',numEs)
print(concatenati)
numEs = printEsercizio('impila verticalmente array a b',numEs)
concatenati = np.concatenate([a,b],axis=1)
print(concatenati)

numEs = printEsercizio('Ricava tutte le posizioni in cui a e b coincidono',numEs)
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

idx = a==b
print(a[idx])

a= np.array([2,6,1,9,10,3,27])
idx = a >= 5
idx1 = a <= 10
idx = idx == idx1
print(idx)
print(a[idx])