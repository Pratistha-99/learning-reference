import numpy as np

# Creating Numpy or N-D Array
# arr1 = np.array([1,2,3,4,5])
# print(arr1)
# print(type(arr1))
# 2D data looks like vector


# arr2 = np.array([[1,2,3,4,5],[6,7,8,9,0]])
# print(arr2)
# 2D data looks like metric

# Zeros function is used to create nd array with all element as 0. Style of initializing. 
# arr3 = np.zeros((2,3))
# print(arr3)

# Creates array with initialized values as 1 (float value)
# arr4 = np.ones((4,3))
# print(type(arr4))

# Create identifty metrics, diagnoally 1 else 0 values.
# arr5 = np.identity(5)
# print(arr5)

# Create range in array form. Extension of range
# arr6 = np.arange(10)
# print(arr6)


#Linearly spaced distance
# arr7 = np.linspace(10,20,10)
# print(arr7)

# arr8 = arr7.copy()
# print(arr8)


# Creating Numpy Arrays
# a = np.array([1,2,3,4])
# print(a) # This is a 1D array - vector
# print(type(a))


# b = np.array([[1,2,3,4,5],[6,7,8,9,0]])
# print(b) # Metrics
# # 2D data looks like metric



# c = np.array([[1,2,3,4,5],[6,7,8,9,0],[1,1,1,1,1]])
# print(b) # Tensor


# print(np.array([1,2,3,4,5],dtype = int))
# print(np.arange(1,11).reshape(5,2))

# a=np.array([1,2,3,4])
# # b=np.array([[1,2,3,4,5],[6,7,8,9,0]])
# # c=np.array([[1,2,3,4,5],[6,7,8,9,0],[1,1,1,1,1]])
# # print(a,b,c)

# # Changing data type
# a = a.astype(np.int32)
# print(a.dtype)

#Array Operations
# a1 = np.arange(12).reshape(3,4)
# a2 = np.arange(12,24).reshape(3,4)
# print(a1,'\n',a2)
# print('\n')

#Scalar Operations
# print(a1)
# #Relational Operations
# print(a1 > 2)

#Array Function
# a1 = np.random.random((3,3))
# a1 = np.round(a1*100)
# print(a1)
# 0 refers to column and 1 refers to row
# print(np.max(a1,axis=1))

#Dot product
# a1 = np.arange(6).reshape(2,3)
# print(a1)
# a2 = np.arange(7,13).reshape(3,2)
# print(a2)
# print(np.dot(a1,a2))


# s1 = np.random.random((2,4))*100
# print(np.floor(s1))


#Slicing & Indexing
# a1 = np.arange(10)
# a2 = np.arange(12).reshape(3,4)
# a3 = np.arange(27).reshape(3,3,3)
# # # print(a3)
# # # print(a3 [1,1,0])

# # print(a2)
# # # print(a2[::2,1::2])
# # # print(a2[1,::3])
# # print(a2[0:2,1:])

# # print(a3[::2,0,::2])

# print(a2)
# # for i in np.nditer(a2):
# #     print(i)

# # print(a2.transpose())
# print(a2.ravel())


# #Stacking & Splitting
# ''' Join data from multiple data sources'''
# a4 = np.arange(12).reshape(3,4)
# a5 = np.arange(12,24).reshape(3,4)
# # Horizontal Stacking
# # print(a4,'\n\n',a5)
# # # Vertical Stacking
# # print(np.vstack((a4,a5)))


# # Splitting
# '''Create multiple data section from 1 main data source'''
# a6 = a4 + a5
# print(a6) 
# # print(np.hsplit(a6))
# print(np.vsplit(a6,1))




#Numpy array vs python list
'''Numpy uses c type array which is a static array and is not a referential array (store item directly in memory)
Python is a dynamic array, referential array and stores the address of item in var and not the item itself'''
# a = [i for i in range(10000000)]
# b = [i for i in range(10000000,20000000)]

# c = []
# import time # For time module
# start = time.time() # Gets current time in second

# for i in range(len(a)):
#     c.append(a[i]+b[i])
# print(time.time()-start)

# a = np.arange(10000000)
# b = np.arange(10000000,20000000)

# c = a + b
# start = time.time()
# c = a + b
# print(time.time()-start)

# Numpy vs python in terms of memory usage
# a = [i for i in range(10000000)]
# import sys # System module
# print(sys.getsizeof(a)) # Byte of mempory being occupied by python list

# a = np.arange(10000000,dtype=np.int8)
# print(sys.getsizeof(a)) # data type and memory size of each element in a NumPy array, directly affecting memory usage and performance.



#Advanced Indexing & Slicing

#Fancy Indexing - converting index position into list for filtering
# a = np.arange(0,24).reshape(6,4)
# print(a)
# print(a[[0,2,3]])
# print(a[:,[2,3]])

#Boolean Indexing - filtering based on condition
# a = np.random.randint(1,100,24).reshape(6,4)
# print(a)
# #Find numbers from array > 50
# print('\n')
# # print(a[a > 50])

# # Find given numbers from array
# # print(a % 2 == 0)
# # print('\n')
# # print(a[a % 2 == 0])

# # Find numbers greater than 50 & are even
# print((a>50) & (a%2==0))
# print(a[(a>50) & (a%2==0)])

# print(a[a % 7 != 0])


# Broadcasting
# a = np.arange(12).reshape(3,4)
# b = np.arange(3)
# print(a)
# print(b)
# print(a+b) # Not possible bc the matrix wont be of same size

# a = np.arange(3).reshape(1,3)
# b = np.arange(4).reshape(4,1)
# print(a)
# print(b)
# print(a+b)


#Sigmoid
# def sigmoid(array):
#     return 1/(1 + np.exp(-(array)))

# a = np.arange(10)
# print(sigmoid(a))


# Mean square error
# act = np.random.randint(1,50,25)
# pre = np.random.randint(1,50,25)

# def mse(actual,predicted):
#     return np.mean(sum((actual-predicted)**2))
# print(mse(act,pre))


# Missing Value
# a = np.array([1,2,3,4,5,np.nan,6])
# # print(a)
# print(np.isnan(a))


# Numpy Tips and Tricks
a = np.random.randint(1,100,15)
# print(np.append(a,100))

b = np.random.randint(1,100,24).reshape(6,4)
# print(np.sort(b)[::-1])
# print(np.append(b,np.ones((b.shape[0],1)),axis=1))


# c = np.arange(6).reshape(2,3)
# d = np.arange(6,12).reshape(2,3)
e = np.array([1,1,2,3,2,1,1,2,4,6,])
# print(np.unique(e))
# # print(np.concatenate((c,d),axis=1))

print(b)
# print(np.shape(a))
# # print(np.expand_dims(a,axis=1))
# print(b)
# # print(np.where(a%2==0,0,1))

# # print(np.argmax(b,axis=1))
# print(np.cumprod(b,axis=1))

# print(np.median(a))
# print(np.percentile(a,50))


# print(np.histogram(a,bins=[0,30,50,60]))
# salary = np.array([10000,20000,40000,50000])
# exp = np.array([10,2,40,3])
# print(np.corrcoef(salary,exp))


# print(a[np.isin(a,e)])

# print(np.flip(b,axis=1))
# np.put(e,[0,1,2],[30,30,10])
# print(e)
# print(np.delete(e,[3,4,5]))

#Set function
# m = np.array([1,2,3,4,5])
# n = np.array([3,4,5,6,7])
# print(m,n)
# print(np.union1d(m,n))
# print(np.setdiff1d(n,m))
# print(np.intersect1d(n,m))
# print(np.setxor1d(m,n))
# # print(np.isin(m,10))

# print(np.append(a,[20,50]))
# print(np.clip(a,a_min=20,a_max=50))


# t = np.arange(10)
# print(t)
# print(t[[1,3,5]])

u = np.arange(20).reshape(4,5)
# print(u)
''' Output 
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
''' 
print(u[u>5])
''' Output
[[ 0  3  4]
 [ 5  8  9]
 [10 13 14]
 [15 18 19]]'''

print(u>5)



l = np.array([1,2,3,np.nan,5])
print(l)
print(np.isnan(l))