# NumPy Learning Reference Guide

![Python](https://img.shields.io/badge/Python-3.x-blue)
![NumPy](https://img.shields.io/badge/NumPy-Library-green)
![Status](https://img.shields.io/badge/Status-Learning%20Project-orange)

A structured **NumPy documentation and practice guide** created while learning and experimenting with NumPy concepts.

This repository reflects my **learning journey while studying NumPy** and practicing important NumPy operations.

The goal of this project is to create a **clear reference guide** that can be used for both **learning and interview preparation**.

---

# Author

**Pratistha Thapa**

---

# Table of Contents

- Introduction
- What is NumPy
- Features of NumPy
- NumPy vs Python Lists
- Creating NumPy Arrays
- Array Attributes
- Data Type Conversion
- Array Operations
- Vectorization
- Mathematical and Statistical Functions
- Rounding Functions
- Indexing and Slicing
- Fancy and Boolean Indexing
- Array Manipulation
- Stacking and Splitting
- Broadcasting
- Random Number Generation
- Machine Learning Utility Functions
- Handling Missing Values
- Useful NumPy Utility Functions
- Set Operations

---

# What is NumPy

**NumPy (Numerical Python)** is a Python library used for **efficient numerical computation**.

It provides a powerful data structure called **ndarray (N-dimensional array)** that allows fast mathematical operations on large datasets.

NumPy is widely used in:

- Data Science
- Machine Learning
- Scientific Computing
- Artificial Intelligence
- Image Processing

Many Python libraries depend on NumPy such as:

- Pandas
- Scikit-learn
- TensorFlow
- PyTorch
- SciPy

---

# Features of NumPy

NumPy provides several important features:

- N-dimensional arrays (`ndarray`)
- Vectorized operations
- Broadcasting support
- Mathematical and statistical functions
- Efficient memory usage
- Faster execution due to implementation in C

---

# NumPy vs Python Lists

| Feature | Python List | NumPy Array |
|------|------|------|
| Memory Storage | Stores references to objects | Stores elements in contiguous memory |
| Speed | Slower for numerical computation | Faster due to vectorization |
| Data Types | Mixed data types allowed | Same data type required |
| Operations | Requires loops | Supports element-wise operations |

---

# Creating NumPy Arrays

NumPy provides several functions to create arrays.

| Function | Description | Syntax |
|------|------|------|
| `np.array()` | Create array from list or tuple | `np.array([1,2,3])` |
| `np.zeros()` | Create array filled with zeros | `np.zeros((rows,cols))` |
| `np.ones()` | Create array filled with ones | `np.ones((rows,cols))` |
| `np.identity()` | Create identity matrix | `np.identity(n)` |
| `np.arange()` | Create evenly spaced values | `np.arange(start,stop,step)` |
| `np.linspace()` | Create evenly spaced values within interval | `np.linspace(start,stop,num)` |
| `np.reshape()` | Change array shape | `array.reshape(rows,cols)` |
| `np.random.random()` | Generate random values | `np.random.random(shape)` |

---

# Array Attributes

Array attributes describe the **structure of an ndarray**.

| Attribute | Description | Syntax |
|------|------|------|
| `ndim` | Number of dimensions | `array.ndim` |
| `shape` | Dimensions of array | `array.shape` |
| `size` | Total number of elements | `array.size` |
| `itemsize` | Memory size of each element | `array.itemsize` |
| `dtype` | Data type of elements | `array.dtype` |

---

# Data Type Conversion

NumPy arrays can change data types using:


array.astype(datatype)


Example syntax:


array.astype(np.float32)


---

# Array Operations

NumPy supports element-wise operations.

### Scalar Operations

Operations between array and scalar value.

Syntax:


array + scalar
array * scalar
array / scalar
array ** scalar


### Relational Operations

Used to compare array elements.

Syntax:


array > value
array < value
array == value
array != value


---

# Vectorization

**Vectorization** refers to performing operations on **entire arrays at once** instead of using loops.

Benefits:

- Faster computation
- Cleaner code
- Efficient memory usage

Example syntax:


array1 + array2
array ** 2


---

# Mathematical and Statistical Functions

NumPy provides built-in functions for numerical calculations.

| Function | Description | Syntax |
|------|------|------|
| `min()` | Minimum value | `np.min(array)` |
| `max()` | Maximum value | `np.max(array)` |
| `mean()` | Average value | `np.mean(array)` |
| `median()` | Middle value | `np.median(array)` |
| `std()` | Standard deviation | `np.std(array)` |
| `var()` | Variance | `np.var(array)` |
| `sum()` | Sum of elements | `np.sum(array)` |
| `percentile()` | Percentile value | `np.percentile(array,value)` |
| `dot()` | Dot product of matrices | `np.dot(a,b)` |
| `log()` | Natural logarithm | `np.log(array)` |
| `exp()` | Exponential function | `np.exp(array)` |

---

# Rounding Functions

NumPy provides functions to adjust decimal values.

| Function | Description | Syntax |
|------|------|------|
| `round()` | Round to nearest value | `np.round(array)` |
| `floor()` | Round down | `np.floor(array)` |
| `ceil()` | Round up | `np.ceil(array)` |

---

# Indexing and Slicing

Indexing allows accessing specific elements of arrays.

### Vector (1D Array)

Syntax:


array[index]
array[start:stop]


### Matrix (2D Array)

Syntax:


array[row,column]
array[row_start:row_end , col_start:col_end]


### Tensor (3D Array)

Syntax:


array[matrix,row,column]


---

# Fancy and Boolean Indexing

### Fancy Indexing

Used to select elements using index arrays.

Syntax:


array[[index1,index2,index3]]


### Boolean Indexing

Used to filter elements based on conditions.

Syntax:


array[array > value]


---

# Array Manipulation

Common functions for modifying array structure.

| Function | Description | Syntax |
|------|------|------|
| `reshape()` | Change array shape | `array.reshape(rows,cols)` |
| `transpose()` | Swap rows and columns | `array.transpose()` |
| `ravel()` | Flatten array | `array.ravel()` |

---

# Stacking and Splitting

Used to combine or divide arrays.

### Stacking

| Function | Syntax |
|------|------|
| Horizontal Stack | `np.hstack((a,b))` |
| Vertical Stack | `np.vstack((a,b))` |

### Splitting

| Function | Syntax |
|------|------|
| Horizontal Split | `np.hsplit(array,sections)` |
| Vertical Split | `np.vsplit(array,sections)` |

---

# Broadcasting

**Broadcasting** allows NumPy to perform operations on arrays with different shapes.

Broadcasting Rules:

1. NumPy compares dimensions from right to left.
2. Dimensions are compatible if they are equal or one of them is `1`.
3. The smaller array is automatically expanded.

Example syntax:


array1 + array2


---

# Random Number Generation

Two ways to generate random values in Python.

### Python Random Module

Used for generating individual random values.


random.random()


### NumPy Random Module

Used for generating random arrays efficiently.


np.random.random(shape)


---

# Machine Learning Utility Functions

### Sigmoid Function

Used in logistic regression and neural networks.

Formula:


1 / (1 + e^-x)


Example syntax:


1/(1 + np.exp(-x))


### Mean Squared Error (MSE)

Used to measure prediction error.

Formula:


mean((actual - predicted)^2)


Example syntax:


np.mean((actual - predicted)**2)


---

# Handling Missing Values

NumPy represents missing values using:


np.nan


To detect missing values:


np.isnan(array)


---

# Useful NumPy Utility Functions

| Function | Syntax |
|------|------|
| Sort array | `np.sort(array)` |
| Append value | `np.append(array,value)` |
| Concatenate arrays | `np.concatenate((a,b))` |
| Unique elements | `np.unique(array)` |
| Expand dimensions | `np.expand_dims(array,axis)` |
| Conditional selection | `np.where(condition,x,y)` |
| Index of max value | `np.argmax(array)` |
| Index of min value | `np.argmin(array)` |
| Cumulative sum | `np.cumsum(array)` |
| Cumulative product | `np.cumprod(array)` |
| Histogram | `np.histogram(array,bins)` |
| Correlation coefficient | `np.corrcoef(x,y)` |
| Membership test | `np.isin(array,values)` |
| Reverse array | `np.flip(array)` |
| Replace values | `np.put(array,index,value)` |
| Delete elements | `np.delete(array,index)` |
| Clip values | `np.clip(array,min,max)` |

---

# Set Operations

NumPy supports set operations on arrays.

| Function | Syntax |
|------|------|
| Union | `np.union1d(a,b)` |
| Difference | `np.setdiff1d(a,b)` |
| Intersection | `np.intersect1d(a,b)` |
| Symmetric Difference | `np.setxor1d(a,b)` |

---

# Purpose of This Repository

This repository serves as:

- A **learning notebook**
- A **NumPy reference guide**
- A **revision sheet for interviews**

---

# License

This project is shared for **learning and educational purposes**.
