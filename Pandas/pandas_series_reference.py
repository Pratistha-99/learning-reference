"""
=====================================================================
PANDAS SERIES COMPLETE REFERENCE & PRACTICE GUIDE
=====================================================================

Author: Pratistha Thapa

Purpose:
This script serves as a structured documentation and practice guide
for learning Pandas Series. It reflects my learning journey while
studying Pandas concepts and experimenting with them through code.

I created this file as a personal reference so I can revisit and
review important concepts whenever needed, and to share my learning
process with others who may also be starting their Pandas journey.

Each concept in this guide includes:

• Definition – What the concept means
• Explanation – A simple explanation of how it works
• Code Example – Practical implementation using Pandas
• Expected Output – Example result of running the code

Topics Covered:
• What is a Pandas Series
• Creating Series from list and dictionary
• Custom index and Series name
• Series attributes
• Reading Series from CSV
• Head, tail and sample
• value_counts, sorting
• Mathematical methods
• Indexing, slicing, fancy indexing
• Editing Series
• Python functions on Series
• Boolean indexing
• Plotting with Pandas and Matplotlib

This file is intended to be both:
1. A learning notebook
2. A quick reference guide

=====================================================================
"""

# ==============================================================
# IMPORTING LIBRARIES
# ==============================================================

# NumPy is often used together with Pandas for numerical operations.
import numpy as np

# Pandas is the main library used here.
import pandas as pd

# Matplotlib is used for plotting graphs.
# Important:
# importing matplotlib does NOT automatically import pyplot.
# We explicitly import the pyplot submodule because it contains
# plotting functions like plt.show(), plt.plot(), etc.
import matplotlib.pyplot as plt


# ==============================================================
# 1. WHAT IS A PANDAS SERIES?
# ==============================================================

"""
Definition:
A Pandas Series is a one-dimensional labeled array capable of
holding data of any type such as integers, strings, floats, or objects.

A Series contains:
• Index -> label/position of each value
• Value -> actual data stored

You can think of Series as:
- a single column of a table
- an improved version of a Python list
- a mixture of dictionary + array behavior

Why it is useful:
• supports indexing and slicing
• supports vectorized operations
• includes many built-in methods
• forms the foundation of Pandas DataFrame columns
"""


# ==============================================================
# 2. BUILDING SERIES FROM PYTHON LIST
# ==============================================================

"""
When we pass a Python list into pd.Series(),
Pandas automatically creates a default integer index starting from 0.
"""

country = ['Nepal', 'India', 'Pakistan', 'Bangladesh', 'Srilanka', 'Bhutan']
print(pd.Series(country))

# Expected Output:
# 0         Nepal
# 1         India
# 2      Pakistan
# 3    Bangladesh
# 4      Srilanka
# 5        Bhutan
# dtype: object

# Note:
# dtype: object means the Series contains string-like Python objects.


# Another example using integer values
runs = [13, 23, 56, 33, 1]
print(pd.Series(runs))

# Expected Output:
# 0    13
# 1    23
# 2    56
# 3    33
# 4     1
# dtype: int64


# ==============================================================
# 3. CREATING SERIES WITH CUSTOM INDEX
# ==============================================================

"""
By default, Pandas creates numeric indexes.
But we can provide our own custom index labels.

Syntax:
pd.Series(data, index=custom_labels)

This is useful when labels are meaningful,
for example: subject names, dates, product names, user ids, etc.
"""

marks = [67, 89, 100, 56]
subjects = ['maths', 'english', 'science', 'geography']

print(pd.Series(marks, index=subjects))

# Expected Output:
# maths         67
# english       89
# science      100
# geography     56
# dtype: int64


# ==============================================================
# 4. ADDING NAME TO A SERIES
# ==============================================================

"""
A Series can also have a name.
The name acts like metadata and gives extra meaning to the data.

Syntax:
pd.Series(data, index=index_labels, name='name_here')
"""

marks = pd.Series(marks, index=subjects, name='Pratistha Thapa')
print(marks)

# Expected Output:
# maths         67
# english       89
# science      100
# geography     56
# Name: Pratistha Thapa, dtype: int64

# Note:
# The name appears at the bottom of the printed Series.


# ==============================================================
# 5. BUILDING SERIES FROM DICTIONARY
# ==============================================================

"""
When a dictionary is passed to pd.Series():
• dictionary keys become the index
• dictionary values become the Series values

This is very convenient because dictionaries already have labels.
"""

marks_dict = {
    'maths': 65,
    'english': 89,
    'science': 79,
    'geography': 100
}

marks_series = pd.Series(marks_dict, name='pt')
print(marks_series)

# Expected Output:
# maths         65
# english       89
# science       79
# geography    100
# Name: pt, dtype: int64


# ==============================================================
# 6. SERIES ATTRIBUTES
# ==============================================================

"""
Attributes describe the properties of a Series.

Commonly used attributes:
• size      -> total number of elements
• dtype     -> data type of values
• name      -> name of Series
• is_unique -> checks whether all values are unique
• index     -> index labels of Series
• values    -> NumPy array of underlying values
"""

print(marks_series.size)
# Expected Output:
# 4

print(marks_series.dtype)
# Expected Output:
# int64

print(marks_series.name)
# Expected Output:
# pt

print(marks_series.is_unique)
# Expected Output:
# True

print(marks_series.index)
# Expected Output:
# Index(['maths', 'english', 'science', 'geography'], dtype='object')

print(marks_series.values)
# Expected Output:
# array([ 65,  89,  79, 100])


# ==============================================================
# 7. READING DATA FROM CSV
# ==============================================================

"""
pd.read_csv() reads CSV files.

Important:
pd.read_csv() returns a DataFrame by default, even if the CSV has only one column.

If a CSV contains only one useful column and we want it as a Series,
we can convert the one-column DataFrame into Series using:

.squeeze('columns')
"""

subs = pd.read_csv('Python Tutorial/Pandas/datasets/subs.csv')
print(type(subs))

# Expected Output:
# <class 'pandas.core.frame.DataFrame'>

subs = subs.squeeze('columns')
print(type(subs))

# Expected Output:
# <class 'pandas.core.series.Series'>

print(subs)

# Expected Output:
# depends on your subs.csv file
# example:
# 0    48
# 1    57
# 2    62
# ...
# Name: subscribers, dtype: int64
#
# Note:
# exact values depend on the file content.


# CSV with custom index column
vk_match = pd.read_csv(
    'Python Tutorial/Pandas/datasets/kohli_ipl.csv',
    index_col='match_no'
)
print(type(vk_match))

# Expected Output:
# <class 'pandas.core.frame.DataFrame'>

vk_match = vk_match.squeeze('columns')
print(type(vk_match))

# Expected Output:
# <class 'pandas.core.series.Series'>


# Another dataset
bollywood = pd.read_csv(
    'Python Tutorial/Pandas/datasets/bollywood.csv',
    index_col='movie'
)

print(bollywood)

# Expected Output:
# One-column DataFrame with movie names as index and lead actor as values

bollywood = bollywood.squeeze('columns')
print(bollywood)

# Expected Output:
# movie
# 3 Idiots                         Aamir Khan
# Zokkomon                         Darsheel Safary
# ...
# Name: lead, dtype: object


# ==============================================================
# 8. HEAD() AND TAIL()
# ==============================================================

"""
head(n) -> returns first n rows (default = 5)
tail(n) -> returns last n rows (default = 5)

Useful for quickly inspecting a dataset.
"""

print(subs.head())

# Expected Output:
# first 5 rows of subs

print(subs.head(3))

# Expected Output:
# first 3 rows of subs

print(subs.tail())

# Expected Output:
# last 5 rows of subs

print(subs.tail(10))

# Expected Output:
# last 10 rows of subs


# ==============================================================
# 9. SAMPLE()
# ==============================================================

"""
sample() returns random rows from the Series.

Useful when:
• quickly inspecting data
• avoiding bias from only looking at top rows
• random testing
"""

print(bollywood.sample())

# Expected Output:
# one random movie and its lead actor

print(bollywood.sample(5))

# Expected Output:
# 5 random movie-actor rows


# ==============================================================
# 10. value_counts()
# ==============================================================

"""
value_counts() counts how many times each unique value appears.

For bollywood Series:
• index  -> actor names
• values -> number of movies done by each actor

Very useful for:
• frequency analysis
• finding most common categories
• identifying repeated values
"""

print(bollywood.value_counts())

# Expected Output:
# actor names with counts in descending order
# example:
# Akshay Kumar      48
# Amitabh Bachchan  35
# Ajay Devgn        30
# ...
#
# exact result depends on your dataset


# ==============================================================
# 11. SORTING
# ==============================================================

"""
sort_values() -> sorts data by values
sort_index()  -> sorts data by index labels

Important:
Most Pandas methods return a new object by default.
So changes are temporary unless:
• reassigned
• or inplace=True is used
"""

print(vk_match.sort_values(ascending=False).head(1))

# Expected Output:
# highest score in the Series
# example:
# match_no
# 34    113
# Name: runs, dtype: int64

print(vk_match.sort_values(inplace=False))

# Expected Output:
# all match scores sorted in ascending order

print(bollywood.sort_index(ascending=False))

# Expected Output:
# Series sorted by movie names in reverse alphabetical order

bollywood.sort_index(ascending=False, inplace=True)
print(bollywood)

# Expected Output:
# permanently sorted bollywood Series by index descending


# ==============================================================
# 12. SERIES MATHEMATICAL METHODS
# ==============================================================

"""
Pandas Series supports many mathematical/statistical methods.

count()  -> counts non-missing values
sum()    -> total sum
product()-> multiplication of all values
mean()   -> arithmetic average
median() -> middle value
mode()   -> most frequent value
std()    -> standard deviation
var()    -> variance
min()    -> minimum value
max()    -> maximum value
"""

print(vk_match.count())
# Expected Output:
# total number of non-null scores

print(subs.sum())
# Expected Output:
# sum of all subscriber values

print(subs.product())
# Expected Output:
# product of all values
# Note: can become extremely large

print(subs.mean())
# Expected Output:
# average of all subscriber values

print(subs.median())
# Expected Output:
# middle value of sorted subscriber data

print(bollywood.mode())
# Expected Output:
# actor name(s) appearing most often
# example:
# 0    Akshay Kumar
# dtype: object

print(subs.std())
# Expected Output:
# standard deviation of subscribers

print(subs.var())
# Expected Output:
# variance of subscribers

print(subs.min())
# Expected Output:
# minimum subscriber value

print(subs.max())
# Expected Output:
# maximum subscriber value


# ==============================================================
# 13. DESCRIBE()
# ==============================================================

"""
describe() gives a quick summary of the data.

For numeric Series, it includes:
• count
• mean
• std
• min
• 25%
• 50%
• 75%
• max

For object/string Series, it includes:
• count
• unique
• top
• freq
"""

print(vk_match.describe())

# Expected Output:
# count     ...
# mean      ...
# std       ...
# min       ...
# 25%       ...
# 50%       ...
# 75%       ...
# max       ...

print(subs.describe())

# Expected Output:
# summary statistics for subscriber data


# ==============================================================
# 14. INDEXING
# ==============================================================

"""
Indexing means retrieving a single value from a Series.

Two common ways:
• by numeric position
• by index label

Important note:
Series indexing can sometimes behave differently depending on whether
the index is numeric or custom string labels.
"""

x = pd.Series([12, 13, 14, 35, 46, 56, 58, 79, 9])
print(x)

# Expected Output:
# 0    12
# 1    13
# 2    14
# 3    35
# 4    46
# 5    56
# 6    58
# 7    79
# 8     9
# dtype: int64

print(x[1])

# Expected Output:
# 13

print(bollywood['Zokkomon'])

# Expected Output:
# lead actor of movie "Zokkomon"
# example:
# Darsheel Safary

print(bollywood[-1])

# Expected Output:
# last value in bollywood Series
# Note:
# this works here because index is string-based, not integer-based


# ==============================================================
# 15. SLICING
# ==============================================================

"""
Slicing means retrieving multiple consecutive values.

Syntax:
series[start:end]

Important:
• start is included
• end is excluded in position-based slicing
"""

print(vk_match[5:16])

# Expected Output:
# values from position 5 to 15

print(vk_match[-5:])

# Expected Output:
# last 5 values from vk_match

print(bollywood[-7:])

# Expected Output:
# last 7 movie-actor pairs

print(bollywood[::2])

# Expected Output:
# every second value from bollywood


# ==============================================================
# 16. FANCY INDEXING
# ==============================================================

"""
Fancy indexing means selecting multiple specific positions or labels.

Useful when you want:
• non-consecutive positions
• specific selected values
"""

print(vk_match[[1, 3, 4, 5]])

# Expected Output:
# values from positions 1, 3, 4, and 5

print(bollywood['2 States (2014 film)'])

# Expected Output:
# lead actor of "2 States (2014 film)"


# ==============================================================
# 17. EDITING SERIES
# ==============================================================

"""
Series values can be changed using:
• label
• position
• slicing
• fancy indexing

You can also add new values using a new label.
"""

print(marks_series['science'])
# Expected Output:
# 79

marks_series['science'] = 70
marks_series[1] = 100
marks_series['sst'] = 90

print(marks_series)

# Expected Output:
# maths         65
# english      100
# science       70
# geography    100
# sst           90
# Name: pt, dtype: int64

# Note:
# Since 'sst' did not exist earlier, Pandas added it as a new entry.


# Slicing-based editing
vk_match[2:4] = [100, 100]
print(vk_match)

# Expected Output:
# positions 2 and 3 updated to 100

# Fancy indexing-based editing
vk_match[[1, 3, 4]] = [10, 0, 0]
print(vk_match)

# Expected Output:
# positions 1, 3, and 4 changed to 10, 0, 0 respectively

# Editing with label
bollywood['Tom & Jerry'] = 'Tom'
print(bollywood)

# Expected Output:
# new movie label "Tom & Jerry" added with lead actor "Tom"


# ==============================================================
# 18. SERIES WITH PYTHON FUNCTIONALITIES
# ==============================================================

"""
Pandas Series works with many Python built-in functions.

Examples:
len()     -> number of elements
type()    -> data type of object
dir()     -> all available methods and attributes
sorted()  -> sorted values in list form
min(),max()-> minimum and maximum values
"""

print(len(subs))
# Expected Output:
# total number of elements in subs

print(type(subs))
# Expected Output:
# <class 'pandas.core.series.Series'>

print(dir(subs))
# Expected Output:
# long list of available methods and attributes

print(sorted(subs))
# Expected Output:
# Python list of sorted values from subs

print(min(subs), max(subs))
# Expected Output:
# minimum and maximum values


# ==============================================================
# 19. TYPE CONVERSION
# ==============================================================

"""
A Series can be converted into other Python data structures.

list(series) -> converts values to list
dict(series) -> converts index-value pairs to dictionary
"""

print(marks_series)
# Expected Output:
# current Series values

print(list(marks_series))
# Expected Output:
# [65, 100, 70, 100, 90]

print(dict(marks_series))
# Expected Output:
# {'maths': 65, 'english': 100, 'science': 70, 'geography': 100, 'sst': 90}


# ==============================================================
# 20. MEMBERSHIP OPERATOR
# ==============================================================

"""
Important:
'in' checks membership in the INDEX, not in the VALUES.

So:
'Tom & Jerry' in bollywood
checks whether this label exists as an index.
"""

print('Tom & Jerry' in bollywood)

# Expected Output:
# True


# ==============================================================
# 21. LOOPING THROUGH SERIES
# ==============================================================

"""
Looping directly over a Series gives VALUES.
If you want indexes, use series.index.
"""

for i in bollywood:
    print(i)

# Expected Output:
# prints all actor names one by one

for i in bollywood.index:
    print(i)

# Expected Output:
# prints all movie names one by one


# ==============================================================
# 22. ARITHMETIC OPERATIONS
# ==============================================================

"""
Arithmetic operations in Pandas are vectorized.
That means the operation is applied to every element automatically.

Example:
100 + marks_series
adds 100 to each mark.
"""

print(100 + marks_series)

# Expected Output:
# maths        165
# english      200
# science      170
# geography    200
# sst          190
# Name: pt, dtype: int64


# ==============================================================
# 23. RELATIONAL OPERATIONS
# ==============================================================

"""
Relational operators compare each value element-wise and return
a Boolean Series.

Examples:
>=, <=, >, <, ==, !=
"""

print(vk_match >= 50)

# Expected Output:
# Boolean Series with True where value >= 50, else False


# ==============================================================
# 24. BOOLEAN INDEXING
# ==============================================================

"""
Boolean indexing filters a Series using a condition.

This is one of the most powerful Pandas features.

Pattern:
series[condition]
"""

print(vk_match[vk_match >= 50].size)

# Expected Output:
# number of matches where runs >= 50

print(vk_match[vk_match == 0])

# Expected Output:
# all matches where score is 0 (ducks)

print(vk_match[vk_match == 0].size)

# Expected Output:
# total number of ducks

print(subs >= 200)

# Expected Output:
# Boolean Series showing which subscriber counts are >= 200


# ==============================================================
# 25. FREQUENCY-BASED FILTERING
# ==============================================================

"""
Problem:
Find actors who have done more than 20 movies.

Step 1:
value_counts() gives number of movies per actor

Step 2:
filter those counts > 20
"""

num_movies = bollywood.value_counts()
print(num_movies[num_movies > 20])

# Expected Output:
# actors whose movie count is greater than 20
# example:
# Akshay Kumar        48
# Amitabh Bachchan    35
# Ajay Devgn          29
# ...
#
# exact values depend on the dataset

# One-line version:
# print(bollywood.value_counts()[bollywood.value_counts() > 20])


# ==============================================================
# 26. PLOTTING WITH PANDAS
# ==============================================================

"""
Pandas Series has built-in plotting support using Matplotlib.

subs.plot()
creates a line chart by default.

Important:
plt.show() is required in normal Python scripts
to display the graph window.
"""

subs.plot()
plt.show()

# Expected Output:
# A line graph where:
# x-axis -> index position
# y-axis -> subscriber values


# ==============================================================
# 27. BAR CHART EXAMPLE
# ==============================================================

"""
We can also plot a bar chart using kind='bar'.

This example shows top 20 actors with the highest number of movies.
"""

bollywood.value_counts().head(20).plot(kind='bar')
plt.show()

# Expected Output:
# A bar chart with:
# x-axis -> actor names
# y-axis -> number of movies


# ==============================================================
# 28. IMPORTANT LEARNING NOTES
# ==============================================================

"""
Key points to remember:

1. pd.Series() creates a one-dimensional labeled array.

2. read_csv() returns a DataFrame by default.
   Use .squeeze('columns') to convert one-column DataFrame to Series.

3. value_counts() is one of the most useful methods for categorical data.

4. 'in' checks index membership, not values.

5. Boolean indexing is a core Pandas skill:
   series[series > value]

6. sort_values() sorts by values, sort_index() sorts by labels.

7. Pandas plotting internally uses Matplotlib.

8. Looping over Series gives values by default.
   Use series.index if you want labels.

9. Arithmetic and relational operations are vectorized.

10. Series is the foundation of DataFrame columns.
"""


"""
=====================================================================
END OF PANDAS SERIES REFERENCE GUIDE
=====================================================================
"""