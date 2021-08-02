#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[5]:


import matplotlib as plot


# In[4]:


import os


# In[3]:


import pandas as pd


# In[6]:


df=pd.read_csv(r"D:\projects\Weather Data.csv")


# In[16]:


df


# In[18]:


df.head(10)


# In[20]:


df.shape # shows number of Rows and columns


# In[22]:


df.index #gives Index start and end index  and increment by steps


# In[24]:


df.columns # Display the COlumne name


# In[36]:


df.dtypes #Data Type of columns


# In[37]:


df['Weather'].unique() #provide you with unique values


# In[39]:


df.nunique() #number of Unique value


# In[43]:


df.count() #gives total counts in every colum


# In[44]:


df['Weather'].value_counts() #it can only apply on single Column , It show all the value with their total count


# In[47]:


df.info() #Basic Info for Data


# # Questions Part 
# 

# Q1) Find all the unique "Wind speed " values in the data 

# In[48]:


df.head(2)


# In[52]:


df['Wind Speed_km/h'].nunique()


# In[50]:


df.nunique()


# In[54]:


df['Wind Speed_km/h'].unique() #Answer


# Find Number of time Weather is exactly clear?

# In[55]:


df.head(2)


# In[56]:


#value count
df.Weather.value_counts()


# In[58]:


#Filter Weather to Clear
df[df.Weather == 'Clear']


# In[60]:


#groupby function
df.groupby('Weather').get_group('Clear')


# Q3 Find no: of time speed of wind exactly 4km/h?

# In[61]:


data.head(2)


# In[65]:


df[df['Wind Speed_km/h']==4] # Q3 Answer 


# Q4) Find Out all the Null Values in Data Set
# 

# In[8]:


df.isnull().sum() #Answer


# In[9]:


df.notnull().sum() 


# Q5) Rename Column 'Weather' to weather condition
# 

# In[10]:


df.head(2)


# In[14]:


df.rename(columns ={'Weather' : 'Weather Condition'},inplace =True) #rename Column Name inplace is used for permanent replacement 


# In[15]:


df.head()


# Q6) What is mean of Visibility ?
# 

# In[17]:


df.head(2)


# In[18]:


df.Visibility_km.mean() #Calculate Mean for a column


# Q7) What is STD Dev pf 'Pressure ' in This Data ?
# 

# In[20]:


df.Press_kPa.std() #calculate Std dev for column


# Q8) What is variance of ' relative Humidity ' in this data ?

# In[21]:


df.head(2)


# In[22]:


df['Rel Hum_%'].var() #calculate Variance 


# Q9)find all instance when snow was recorded

# In[23]:


df.head(2)


# In[24]:


df['Weather Condition'].value_counts()


# In[29]:


df[df['Weather Condition']=='Snow']


# In[31]:


#str contains
df[df['Weather Condition'].str.contains('Snow')]  #will show all match that have snow value in it


# In[32]:


#583 rows have snow as value in column name weather Condition for Q10 


# Q11) Find all instance where speed above 24 and visibility above 25?
# 

# In[33]:


df.head(2)


# In[37]:


df[(df['Wind Speed_km/h']>24) & (df.Visibility_km == 25)]


# Q12) Mean value of all column against Weather condition ?

# In[38]:


df.head(2)


# In[42]:


df.groupby('Weather Condition').mean()


# Q12 What is the Minimum and maximum value of each column against each 'Weather condition' ?

# In[44]:


df.head()
df.groupby('Weather Condition').min()


# In[45]:


df.groupby('Weather Condition').max()


# Q13 ) Show all the records where Weather Condition is Fog ?

# In[47]:


df[df['Weather Condition']=='Fog']


# In[50]:


df[df['Weather Condition'].str.contains('Fog')]


# Q14) Find all the instances where Wheather is clear or visibility is above 40

# In[55]:


df[(df['Weather Condition']=='Clear') | (df['Visibility_km'] > 40)]


# Q15) Find all Instances where Weather is clear and Relative humidity is greater than 50 or Visibility > 40

# In[57]:


df[((df['Weather Condition']=='Clear')&(df['Rel Hum_%'] > 50)) | (df['Visibility_km'] > 40)]


# In[ ]:




