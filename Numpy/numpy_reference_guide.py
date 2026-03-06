"""
=====================================================================
NUMPY COMPLETE REFERENCE & PRACTICE GUIDE
=====================================================================

Author: Pratistha Thapa
Purpose: This script serves as a structured documentation and practice guide 
for learning NumPy. It reflects my learning journey while studying 
NumPy concepts and experimenting with them through code.

I created this file as a personal reference so I can revisit and 
review important concepts whenever needed, and to share my learning 
process with others who may also be starting their NumPy journey. 

Each concept in this guide includes:

• Definition – What the concept means
• Explanation – A simple explanation of how it works
• Code Example – Practical implementation using NumPy
• Expected Output – Example result of running the code

Topics Covered:
• Introduction to NumPy
• NumPy arrays vs Python lists
• Creating NumPy arrays
• Array attributes and data types
• Array operations and vector operations
• Mathematical and statistical functions
• Indexing and slicing (vector, matrix, tensor)
• Broadcasting
• Reshaping and stacking arrays
• Boolean indexing
• Handling missing values
• Useful NumPy utility functions
• Set operations with NumPy arrays

This file is intended to be both:
1. A learning notebook
2. A quick reference guide

=====================================================================


=====================================================================
1. WHAT IS NUMPY?
=====================================================================

NumPy (Numerical Python) is a Python library built on top of C used for efficient
numerical computation. It introduces the ndarray (N-dimensional array),
which allows fast mathematical operations on large datasets.

NumPy is widely used in:
• Data Science
• Machine Learning
• Scientific Computing
• Artificial Intelligence
• Image Processing

Many libraries are built on top of NumPy:
• Pandas
• Scikit-Learn
• TensorFlow
• PyTorch

=====================================================================
2. FEATURES OF NUMPY
=====================================================================

1. N-Dimensional Arrays (ndarray)
2. Vectorized Operations (no loops required)
3. Broadcasting (operations on different sized arrays)
4. Mathematical & Statistical Functions
5. Efficient Memory Usage
6. Faster Execution (written in C)

=====================================================================
3. NUMPY VS PYTHON LIST
=====================================================================

Python Lists:
• Dynamic size
• Stores references to objects
• Slower for numerical computations

NumPy Arrays:
• Fixed size
• Stores data directly in contiguous memory
• Faster for numerical operations
"""

# Importing the Numpy Library
import numpy as np


# ==============================================================
# 4. SPEED COMPARISON
# ==============================================================

"""
Python List Example
"""

a = [1,2,3,4]
b = [5,6,7,8]

c = []
for i in range(len(a)):
    c.append(a[i] + b[i])

print(c)

# Output
# [6, 8, 10, 12]


"""
NumPy Vectorized Operation
"""

a_np = np.array([1,2,3,4])
b_np = np.array([5,6,7,8])

c_np = a_np + b_np

print(c_np)

# Output
# [ 6  8 10 12]


# ==============================================================
# 5. CREATING NUMPY ARRAYS
# ==============================================================

"""
np.array()

Creates a NumPy array from Python lists or tuples
"""

arr = np.array([1,2,3,4])
print(arr)

# Output
# [1 2 3 4]


"""
np.zeros()

Creates array filled with zeros
"""

zeros = np.zeros((2,3))
print(zeros)

# Output
# [[0. 0. 0.]
#  [0. 0. 0.]]


"""
np.ones()

Creates array filled with ones
"""

ones = np.ones((2,2))
print(ones)

# Output
# [[1. 1.]
#  [1. 1.]]


"""
np.identity()

Creates identity matrix (diagonal = 1)
"""

identity = np.identity(3)
print(identity)

# Output
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]


"""
np.arange()

Creates array with evenly spaced values
"""

a = np.arange(0,10)
print(a)

# Output
# [0 1 2 3 4 5 6 7 8 9]


"""
np.linspace()

Creates evenly spaced numbers between two values
"""

b = np.linspace(0,10,5)
print(b)

# Output
# [ 0.   2.5  5.   7.5 10. ]


"""
np.reshape()

Changes the shape of array
"""

c = np.arange(6).reshape(2,3)
print(c)

# Output
# [[0 1 2]
#  [3 4 5]]


"""
np.random.random()

Generates random numbers between 0 and 1
"""

r = np.random.random((2,2))
print(r)

# Example Output (values change every run)
# [[0.23 0.88]
#  [0.45 0.12]]


# ==============================================================
# 6. ARRAY ATTRIBUTES
# ==============================================================

"""
Array attributes describe the structure of arrays
"""

a = np.array([[1,2,3],[4,5,6]])

print(a.ndim)

# Output
# 2

print(a.shape)

# Output
# (2,3)

print(a.size)

# Output
# 6

print(a.itemsize)

# Output
# 8   (bytes)

print(a.dtype)

# Output
# int64


# ==============================================================
# 7. CHANGING DATA TYPE
# ==============================================================

"""
astype()

Changes data type of array
"""

a = np.array([1,2,3])
a = a.astype(np.float32)

print(a)

# Output
# [1. 2. 3.]


''' ==============================================================
# 8. ARRAY OPERATIONS
Array operations refer to mathematical operations performed
directly on NumPy arrays.

Unlike Python lists, NumPy performs operations in a
vectorized manner, meaning operations are applied
element-wise without the need for explicit loops.

Types of operations:
1. Scalar Operations -  Operations between array and scalar
2. Vector Operations
3. Relational Operations

# ============================================================== '''

a = np.array([1,2,3,4])

print(a + 2)

# Output
# [3 4 5 6]

print(a * 2)

# Output
# [2 4 6 8]


"""
Relational Operations
"""

print(a > 2)

# Output
# [False False True True]


# ==============================================================
# 9. VECTOR OPERATIONS 
# Vector operations perform element-wise computation between arrays.
# ==============================================================

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)

# Output
# [5 7 9]

print(a * b)

# Output
# [ 4 10 18]


# ==============================================================
# 10. STATISTICAL FUNCTIONS
# ==============================================================

a = np.array([10,20,30,40,50])

print(np.min(a))      # 10
print(np.max(a))      # 50
print(np.mean(a))     # 30.0
print(np.median(a))   # 30.0
print(np.std(a))      # standard deviation
print(np.var(a))      # variance
print(np.sum(a))      # 150
print(np.percentile(a,50))  # 30.0


# ==============================================================
# 11. MATRIX OPERATIONS
# ==============================================================

a = np.arange(6).reshape(2,3)
b = np.arange(6,12).reshape(3,2)

print(np.dot(a,b))

# Output
# [[ 28  31]
#  [100 112]]


# ==============================================================
# 12. MATHEMATICAL FUNCTIONS
# ==============================================================

a = np.array([1,2,3])

print(np.log(a))

# Output
# [0.         0.69314718 1.09861229]

print(np.exp(a))

# Output
# [ 2.71828183  7.3890561  20.08553692]


# ==============================================================
# 13. ROUNDING FUNCTIONS
# ==============================================================

a = np.array([1.2,3.7,4.3])

print(np.round(a))
# [1. 4. 4.]

print(np.floor(a))
# [1. 3. 4.]

print(np.ceil(a))
# [2. 4. 5.]


# ==============================================================
# 14. SLICING AND INDEXING
# ==============================================================

"""
Vector = 1D array (1 row - multiple items, item check moves from left to right)
Matrix = 2D array (2D - row check first (down), then move to column level(right) check)
Tensor = 3D or higher dimensional array (3D - matrix check(# of matrix), row check(# of rows), column check(# of columns))
"""

v = np.arange(10)
# Index position -1 leads to the end of the list
print(v[2:6])

# Output
# [2 3 4 5]


m = np.arange(12).reshape(3,4)

print(m[0:2,1:3])

# Output
# [[1 2]
#  [5 6]]


t = np.arange(27).reshape(3,3,3)

print(t[1,1,1])

# Output
# 13


"""
Fancy Indexing
"""
# Indexing based on position of item in the list
a = np.arange(10)
# print(a)
# Output: [0 1 2 3 4 5 6 7 8 9]

print(a[[1,3,5]]) # select 1st, 3rd and 5th position from a
# Output
# [1 3 5]


u = np.arange(20).reshape(4,5)
print(u)
''' Output 
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
''' 
print(u[:,[0,3,4]]) # Select all row but the 0th, 3rd and 4th columns
''' Output
[[ 0  3  4]
 [ 5  8  9]
 [10 13 14]
 [15 18 19]]'''



# ==============================================================
# 15. STACKING
# ==============================================================

a = np.arange(6).reshape(2,3)
b = np.arange(6,12).reshape(2,3)

print(np.hstack((a,b)))

# Output
# [[ 0 1 2 6 7 8]
#  [ 3 4 5 9 10 11]]

print(np.vstack((a,b)))

# Output
# [[ 0 1 2]
#  [ 3 4 5]
#  [ 6 7 8]
#  [ 9 10 11]]


# ==============================================================
# 16. SPLITTING
# ==============================================================

a = np.arange(12).reshape(3,4)

print(np.hsplit(a,2))

# Output
# [array([[0,1],
#         [4,5],
#         [8,9]]),
#
#  array([[2,3],
#         [6,7],
#         [10,11]])]


print(np.vsplit(a,3))

# Output
# [[0 1 2 3],
#  [4 5 6 7],
#  [8 9 10 11]]


# ==============================================================
# 17. BOOLEAN ARRAY - Used for filtering data based on specific condition
# ==============================================================

a = np.arange(10)

print(a[a > 5])
# Output
# [6 7 8 9]

u = np.arange(20).reshape(4,5)
# print(u)
''' Output 
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
''' 
print(u>5) # Converts the result in a boolean form
'''
[[False False False False False]
 [False  True  True  True  True]
 [ True  True  True  True  True]
 [ True  True  True  True  True]]
'''

print(u[u>5]) # Converts the result in a list showing all condition that is TRUE
# Output: [ 6  7  8  9 10 11 12 13 14 15 16 17 18 19]


"""
============================================================
16. RANDOM LIBRARY (PYTHON vs NUMPY)
============================================================

Python random module:
Used for general random values.


NumPy random:
Used for generating random arrays efficiently.
"""

import random # Python module

print(random.random())
print(np.random.random()) # Numpy random



# ==============================================================
# 18. BROADCASTING
# ==============================================================

"""
Broadcasting is a mechanism that allows NumPy to perform
arithmetic operations on arrays of different shapes.

Instead of copying data, NumPy automatically expands the
smaller array to match the larger one.

Rules:

1. If dimensions differ, NumPy adds a dimension of size 1
2. Dimensions are compatible if equal or one of them is 1
"""

a = np.arange(3).reshape(1,3)
b = np.arange(4).reshape(4,1)

print(a + b)

# Output
# [[0 1 2]
#  [1 2 3]
#  [2 3 4]
#  [3 4 5]]


# ==============================================================
# 19. USER DEFINED MACHINE LEARNING FUNCTIONS
# ==============================================================

"""
Sigmoid Function
"""

def sigmoid(x):
    return 1/(1 + np.exp(-x))

a = np.array([-2,-1,0,1,2])

print(sigmoid(a))

# Output
# [0.119 0.268 0.5 0.731 0.881]


"""
Mean Squared Error
"""

def mse(actual, predicted):
    return np.mean((actual - predicted)**2)

a = np.array([20])
p = np.array([10])

print(mse(a,p))


'''==============================================================
# 20. MISSING VALUES
ndarray (N-dimensional array) is the core data structure of NumPy.

It represents a grid of values where:

• All elements have the same data type
• Elements are stored in contiguous memory
• Operations are optimized for speed

# ============================================================== '''

a = np.array([1,2,3,np.nan,5])
print(a)
# [ 1.  2.  3. nan  5.]

print(np.isnan(a))
# Output
# [False False False True False]


# ==============================================================
# 21. NUMPY FUNCTIONS
# ==============================================================

a = np.array([5,3,8,1,9])

 # Sort
print(np.sort(a))
# [1 3 5 8 9]

# Append
print(np.append(a,10))
# [5 3 8 1 9 10]

# Concatenate
b = np.arange(5)
print(np.concatenate((a,b)))

# Unique values
print(np.unique(a))
# [1 3 5 8 9]

# Expand dimensions
print(np.expand_dims(a, axis=0))

# Conditional selection
print(np.where(a > 50, 1, 0))

# Index of maximum value
print(np.argmax(a))
# 4

# Index of minimum value
print(np.argmin(a))
# 3

# Cumulative sum
print(np.cumsum(a))
# [ 5 8 16 17 26]

# Cumulative multiplication
print(np.cumprod(a))

# Percentile
print(np.percentile(a,50))

# Histogram
print(np.histogram(a,bins=5))

# Correlation coefficient
x = np.array([1,2,3,4])
y = np.array([2,4,6,8])

print(np.corrcoef(x,y))

# Check membership
print(np.isin(a,[10,20,30]))

# Flip array
print(np.flip(a))

# Replace values
np.put(a,[0,1],[100,200])

# Delete values
print(np.delete(a,[2,3]))

# Clip values within range
print(np.clip(a,3,8))
# [5 3 8 3 8]


# ==============================================================
# 22. SET FUNCTIONS
# ==============================================================

m = np.array([1,2,3,4])
n = np.array([3,4,5,6])

# Union
print(np.union1d(m,n))
# [1 2 3 4 5 6]

# Difference
print(np.setdiff1d(n,m))
# [5 6]

# Intersection
print(np.intersect1d(m,n))
# [3 4]

# Symmetric difference
print(np.setxor1d(m,n))
# [1 2 5 6]


"""
=====================================================================
END OF NUMPY REFERENCE GUIDE
=====================================================================
"""