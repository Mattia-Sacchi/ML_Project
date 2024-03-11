import numpy as np 

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

c= a==b
c= c.astype(bool)
a= np.arange(0,len(a))

print(a[c])

# es 9

arr = np.arange(9).reshape(3,3)
def Swap(arr, start_index, last_index):
    arr[:, [start_index, last_index]] = arr[:, [last_index, start_index]]
 
Swap(arr,0,1)
print(arr)

# es 12

arr = np.arange(9).reshape(3,3)

temp = np.transpose(arr)
Swap(temp,0,1)
arr = temp.transpose()
print(arr)

# es 13

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

print(np.any(iris_2d ==  np.nan))

# es 14

arr1 = np.arange(3)
arr2 = np.arange(3,7)
arr3 = np.arange(7,10)
array_of_arrays = np.array([arr1, arr2, arr3],dtype=object)

print(np.concatenate(array_of_arrays))

# es 15


np.random.seed(100)
a = np.random.randint(1,10, [5,3])

print(np.max(a))

#es 16

a = np.array([1,2,3,np.nan,5,6,7,np.nan])
b = np.isnan(a) == False
print(a[b])

# es 17
a_2d = np.array([[3,3,3],[4,4,4],[5,5,5]])
b_1d = np.array([1,2,3])

print(a_2d - b_1d)

# es 18