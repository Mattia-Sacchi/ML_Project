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

numEs = printEsercizio('Stampa gli indici uguali',numEs)

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

c= a==b
c= c.astype(bool)
a= np.arange(0,len(a))

print(a[c])

numEs = printEsercizio('Elementi tra 5 e 10',numEs)

a= np.array([2,6,1,9,10,3,27])
idx = a >= 5
idx1 = a <= 10
idx = idx == idx1
print(idx)
print(a[idx])

numEs = printEsercizio('Scambia la colonna 0 e 1',numEs)
arr = np.arange(9).reshape(3,3)
def Swap(arr, start_index, last_index):
    arr[:, [start_index, last_index]] = arr[:, [last_index, start_index]]
 
Swap(arr,0,1)
print(arr)

numEs = printEsercizio('Scambia le righe 1 e 2',numEs)

arr = np.arange(9).reshape(3,3)

temp = np.transpose(arr)
Swap(temp,0,1)
arr = temp.transpose()
print(arr)

numEs = printEsercizio('Triva gli elementi non NaN',numEs)

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

print(np.any(iris_2d ==  np.nan))

numEs = printEsercizio('Trasforma l\'array di array in uno unico in linea',numEs)

arr1 = np.arange(3)
arr2 = np.arange(3,7)
arr3 = np.arange(7,10)
array_of_arrays = np.array([arr1, arr2, arr3],dtype=object)

print(np.concatenate(array_of_arrays))

numEs = printEsercizio('Stampa l\'elemento maggiore',numEs)


np.random.seed(100)
a = np.random.randint(1,10, [5,3])

print(np.max(a))

#es 16

numEs = printEsercizio('Stampa soolo gli elementi non NaN',numEs)

a = np.array([1,2,3,np.nan,5,6,7,np.nan])
b = np.isnan(a) == False
print(a[b])

# es 17

numEs = printEsercizio('Sottrai all\'array 2d l\'array 1d',numEs)

a_2d = np.array([[3,3,3],[4,4,4],[5,5,5]])
b_1d = np.array([1,2,3])

print(a_2d - b_1d)

# es 18