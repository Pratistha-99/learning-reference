# Importing Pandas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# #Building series from lists
# Series is a class inside pandas. Series has index of item and its respective value.  
# country = ['Nepal','India','Pakistan','Bangladesh','Srilanka','Bhutan']
# print(pd.Series(country)) # Prints series object (string = object in pandas)

# # Creating an integer list
# runs = [13,23,56,33,1]
# print(pd.Series(runs)) 

# #Providing custom index
# marks = [67,89,100,56]
# subjects = ['maths','english','science','geography']
# # converting marks to values and subjects as index
# print(pd.Series(marks,index=subjects))

# marks = pd.Series(marks,index=subjects,name='Pratistha Thapa') #NAME attribute gives additional info
# print(marks)

# Series from dictionary
marks = {
    'maths':65,
    'english':89,
    'science':79,
    'geography':100
}
marks_series = pd.Series(marks,name='pt')
# # print(marks_series) # Same as creating marks with custom index


# # Series attributes
# print(marks_series.size) #Number of element in the series
# print(marks_series.dtype) #Datatype of series
# print(marks_series.name) #Name of the series
# print(marks_series.is_unique) #Is series items unique
# print(marks_series.index) #Index object of the series
# print(marks_series.values) #Value of the series


# Series using read_csv
subs = pd.read_csv('/Users/aayush/Desktop/Learning/Python Learning/CLV_Churn/Python Tutorial/Pandas/subs.csv')
# print(type(subs)) # Type of file imported, dataframe type when read_csv is used.
subs = subs.squeeze('columns') # Dataframe is converted to a Series type by using squeeze function
# print(type(subs)) 
# print(subs)

# with 2 columns
vk_match = pd.read_csv('/Users/aayush/Desktop/Learning/Python Learning/CLV_Churn/Python Tutorial/Pandas/kohli_ipl.csv',index_col='match_no')
# print(type(vk_match))
vk_match = vk_match.squeeze('columns')
# print(type(vk_match))

# third data set
bollywood = pd.read_csv('/Users/aayush/Desktop/Learning/Python Learning/CLV_Churn/Python Tutorial/Pandas/bollywood.csv',index_col='movie')
# print(bollywood)
bollywood = bollywood.squeeze('columns')
# print(bollywood)

# # head and tail methods
# # top 5 rows by default
# print(subs.head())
# print(subs.head(3)) # custom
# # bottom 5 rows by default
# print(subs.tail())
# print(subs.tail(10)) #custom

# Sample - gives a random row from the dataset
# used to remove biasness by random selection
# print(bollywood.sample())
# print(bollywood.sample(5))

# value_counts - gives frequency of each unique value from the dataset
# print(bollywood.value_counts())

# sort_values - sorts value in asc or desc order, changes are temporary (no changes in original value)
#method chaining - output of one becomes input for another
# ascending parameter for describing the order of sort
# print(vk_match.sort_values(ascending=False).head(1))
# #inplace parameter makes permanent changes in the original series object
# print(vk_match.sort_values(inplace=False))

#sort_index - sorts index in asc or desc order
# print(bollywood.sort_index(ascending=False))
# bollywood.sort_index(ascending=False,inplace=True) #inplace makes permanent changes
# print(bollywood)


# Series maths methods
#Count - gives # of items present inside a series - skips nan value
# Missing value is included in size but not in series
# print(vk_match.count())

# # sum - total sum function
# print(subs.sum())

# # product - total product function
# print(subs.product()) 

# # mean
# print(subs.mean())

# # median
# print(subs.median())

#mode
# print(bollywood.mode()) #gives index position and the most frequent value

# #std
# print(subs.std())

# #var
# print(subs.var())

# #Min
# print(subs.min())

# # Max
# print(subs.max())

# #describe - provides mathematical summary for the series
# print(vk_match.describe())
# print(subs.describe())

# # Filtering data with: indexing, slicing, fancy indexing and labels
# # Series Indexing - based on index position, negative index position works for string type index, in our case, bollywood custom index
# x = pd.Series([12,13,14,35,46,56,58,79,9])
# print(x)
# print(x[1]) #Series doent work for negative indexing
# print(bollywood['Zokkomon']) #Works with python default indexing and with custom indexing as well
# print(bollywood[-1]) #Negative indexing works string indexes


#  #Series Slicing - getting multiple items
# print(vk_match[5:16]) # 6 to 16 index
# print(vk_match[-5:]) # -5 or last 5 index
# print(bollywood[-7:])
# print(bollywood[::2])

# # Fancy Indexing - using index position directly
# # Finding 1,3,5,6th match
# print(vk_match[[1,3,4,5]]) 
# print(bollywood['2 States (2014 film)']) 


# #Editing Series - with index position or label
# print(marks_series['science'])
# marks_series['science'] = 70
# marks_series[1] = 100
# marks_series['sst'] = 90 # adding an item, if its not an index value, pandas will add an item (write over it)
# print(marks_series)

# #Slicing
# vk_match[2:4] = [100,100] #Range of position
# print(vk_match)

# # Fancy Indexing
# vk_match[[1,3,4]] = [10,0,0] # Specific position
# print(vk_match)

# Using Index Label
# bollywood['Tom & Jerry'] = 'Tom'
# print(bollywood)


# #Series with Python Functionalities
# print(len(subs)) #length
# print(type(subs)) #data type
# print(dir(subs)) #attributes and methods in series
# print(sorted(subs)) #sorted data but in a list form
# print(min(subs),max(subs)) # min & max of series

##Type concersion
# print(marks_series)
# print(list(marks_series)) #convert series of marks into a list
# print(dict(marks_series)) #convert series of marks into a dictionary

##Membership Operator
# # Membership operator works with index values
# print('Tom & Jerry' in bollywood) # is this movie in bollywood

##Looping
# for i in bollywood:
#     print(i) # Generate list of values from bollywood

## Loops works with values, if you want to work with index then you have to explicitly specify that you're using index
# for i in bollywood.index:
#     print(i)

##Arithmetic Operator
# print(100+marks_series) # Arithmetic result

# Relational Opearator
# print(vk_match >= 50) # Gives boolean series


# #Boolean Indexing on Series
# print(vk_match[vk_match>=50].size) # .size gives the number
# print(vk_match[vk_match == 0]) # Matches where there is a duck
# print(vk_match[vk_match == 0].size) # Give the size or total # of matches where there are ducks
# print(subs>=200) # More than 200 subs a day

# #Find actors who have done more than 20 movies
# num_movies = bollywood.value_counts() # Number of movies done by each actor
# print(num_movies[num_movies>20]) # Boolean series being places in num_movies to get the count
# # print(bollywood.value_counts()[bollywood.value_counts() > 20]) -- one liner solution for the above

# #Plotting Graphs on Series
# subs.plot() #Converts to a 2d plot
# plt.show()

bollywood.value_counts().head(20).plot(kind='bar')
plt.show()