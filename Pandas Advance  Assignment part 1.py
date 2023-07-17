#!/usr/bin/env python
# coding: utf-8

# Q1. List any five functions of the pandas library with execution.

# In[1]:


import pandas as pd


# In[2]:


f = pd.read_csv("E:\Book1.csv" )


# In[4]:


f.head()


# In[5]:


f.describe()


# In[6]:


f.info()


# In[8]:


f.count()


# In[9]:


f.tail()


# In[11]:


f.shape


# In[12]:


f.columns


# In[19]:


f[['SNo','ObservationDate']]


# Q2. Given a Pandas DataFrame df with columns 'A', 'B', and 'C', write a Python function to re-index the
# DataFrame with a new index that starts from 1 and increments by 2 for each row.

# In[20]:


d = {"A":[1,2,3],
    "B":['A','B','C'],
    "C":['a','b','c']}


# In[21]:


d


# In[22]:


df = pd.DataFrame(d)


# In[23]:


df


# In[39]:


df.reindex([1,3,5],)


# Q3. You have a Pandas DataFrame df with a column named 'Values'. Write a Python function that
# iterates over the DataFrame and calculates the sum of the first three values in the 'Values' column. The
# function should print the sum to the console.
# For example, if the 'Values' column of df contains the values [10, 20, 30, 40, 50], your function should
# calculate and print the sum of the first three values, which is 60.

# In[132]:


v={"a":[10],
   "b":[20],
   "c":[30],
   "d":[40],
   "e":[50]}
  


# In[133]:


df= pd.DataFrame(v)


# In[134]:


df


# In[146]:


df['Sum']=df.iloc[:,[1,3]].sum(axis=1)
print(df)


# Q4. Given a Pandas DataFrame df with a column 'Text', write a Python function to create a new column
# 'Word_Count' that contains the number of words in each row of the 'Text' column.

# Q5. How are DataFrame.size() and DataFrame.shape() different?

# Pandas DataFrame size()
# The size property is used to get an int representing the number of elements in this object and Return the number of rows if Series. Otherwise, return the number of rows times the number of columns if DataFrame.
# 
# 
# Pandas DataFrame shape()
# The shape property is used to get a tuple representing the dimensionality of the Pandas DataFrame.
# 
# 

# Q6. Which function of pandas do we use to read an excel file?

# import pandas as pd
# file = pd.read_excel('file')

# Q7. You have a Pandas DataFrame df that contains a column named 'Email' that contains email
# addresses in the format 'username@domain.com'. Write a Python function that creates a new column
# 'Username' in df that contains only the username part of each email address.
# The username is the part of the email address that appears before the '@' symbol. For example, if the
# email address is 'john.doe@example.com', the 'Username' column should contain 'john.doe'. Your
# function should extract the username from each email address and store it in the new 'Username'
# column.

# In[148]:


import pandas as pd


# In[153]:


df = pd.DataFrame({'email':['username@domain.com', 'john.doe@example.com']})

df['Name'] = df['email'].str.split('@').str[0]


# In[154]:


df


# Q8. You have a Pandas DataFrame df with columns 'A', 'B', and 'C'. Write a Python function that selects
# all rows where the value in column 'A' is greater than 5 and the value in column 'B' is less than 10. The
# function should return a new DataFrame that contains only the selected rows.
# For example, if df contains the following values:
# A B C
# 0 3 5 1
# 1 8 2 7
# 2 6 9 4
# 3 2 3 5
# 4 9 1 2
# Your function should select the following rows: A B C
# 1 8 2 7
# 4 9 1 2
# The function should return a new DataFrame that contains only the selected rows.

# Q9. Given a Pandas DataFrame df with a column 'Values', write a Python function to calculate the mean,
# median, and standard deviation of the values in the 'Values' column.

# In[155]:


f.head()


# In[158]:


f.mean()


# In[159]:


f.std()


# In[160]:


f.describe()


# In[ ]:




