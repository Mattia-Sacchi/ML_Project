# 1. Importa numpy come np e stampa il numero di versione
import numpy as np

print(np.__version__)

# 2. Crea un array 1D di numeri da 0 a 99
arr = np.arange(100)

# 3. Crea un array numpy 3x3 di tutti i True
opt_1 = np.full((3, 3), True, dtype=bool)

# 4. Estrai i numeri dispari da arr
# Input:
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Output:
# array([1, 3, 5, 7, 9])
arr[arr % 2 == 1]

# 5. Sostituisci tutti i numeri dispari in arr con -1
# Input:
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Output:
# array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])
arr[arr% 2 == 1] = -1

# 6. Sostituisci tutti i numeri dispari in arr con -1 senza modificare arr
# Input:
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Output:
# out
#  array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])
# arr
#  array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr2 = np.where(arr % 2 == 1, -1, arr)
print('arr:', arr)
print('out:', arr2)

# 7. Converti un array 1D in un array 2D con 2 righe
# Input:
arr = np.arange(10)
# Output:
# array([[0, 1, 2, 3, 4],
#        [5, 6, 7, 8, 9]])
arr.reshape(2,-1)

# 8. Impila gli array a e b verticalmente
# Input
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
# Output:
# array([[0, 1, 2, 3, 4],
#        [5, 6, 7, 8, 9],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1]])
opt_1 = np.concatenate([a, b], axis=0)
opt_2 = np.vstack([a, b])
opt_3 = np.r_[a, b]

# 9. Impila gli array a e b orizzontalmente
# Input
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
# Output:
# array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
#        [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
opt_1 = np.concatenate([a, b], axis=1)
opt_2 = np.hstack([a, b])
opt_3 = np.c_[a, b]

# 10. Ricava le posizioni in cui gli elementi di a e b coincidono
# Input:
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
# Output:
# (array([1, 3, 5, 7]),)
np.where(a == b)

# 11. Estrai gli elementi tra 5 e 10 da a
# Input:
a = np.array([2, 6, 1, 9, 10, 3, 27])
# Output:
# (array([6, 9, 10]),)
opt_1 = a[(a >= 5) & (a <= 10)]
opt_2 = a[np.where((a >= 5) & (a <= 10))]
opt_3 = a[np.where(np.logical_and(a >= 5, a <= 10))]

# 12. Scambia le colonne 1 e 2 in arr
# Input:
arr = np.arange(9).reshape(3, 3)
# Output:
# array([[1, 0, 2],
#        [4, 3, 5],
#        [7, 6, 8]])
arr = arr[:, [0, 2, 1]]

# 13. Scambia le righe 1 e 2 in arr
# Input:
arr = np.arange(9).reshape(3, 3)
# Output:
# array([[3, 4, 5],
#        [0, 1, 2],
#        [6, 7, 8]])
arr = arr[[0, 2, 1], :]

# 14. Scopri se iris_2d ha valori mancanti (nan)
# Input
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0, 1, 2, 3])
#
np.isnan(iris_2d).any()

# 15. Converti array_of_arrays in un array 1D flat linear
# Input:
arr1 = np.arange(3)
arr2 = np.arange(3, 7)
arr3 = np.arange(7, 10)
array_of_arrays = np.array([arr1, arr2, arr3])
# Output:
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr_2d_opt_1 = np.array([a for arr in array_of_arrays for a in arr])
arr_2d_opt_2 = np.concatenate(array_of_arrays)

# 16. Calcola il massimo di ciascuna riga di un array a
# Input:
np.random.seed(100)  # A cosa serve questa istruzione?
a = np.random.randint(1, 10, [5, 3])
#
opt_1 = np.amax(a, axis=1)
opt_2 = np.apply_along_axis(np.max, arr=a, axis=1)

# 17. Rimuovi tutti i valori nan da un array 1D
# Input:
a = np.array([1, 2, 3, np.nan, 5, 6, 7, np.nan])
# Output:
# array([ 1.,  2.,  3.,  5.,  6.,  7.])
a = a[~np.isnan(a)]

# 18. Sottrai l'array 1D b_1d dall'array 2D a_2d, in modo che b_1d sia sottratto da ciascuna riga di a_2d
# Input:
a_2d = np.array([[3, 3, 3], [4, 4, 4], [5, 5, 5]])
b_1d = np.array([1, 2, 3])
# Output:
# array([[2, 1, 0],
#        [3, 2, 1],
#        [4, 3, 2]])
a_2d - b_1d