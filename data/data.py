#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Used Jupyter notebooks on Anaconda
#used PANDAS, Seaborn , NUMPY, and MatPlotlib 
#Extras dones are Data visualization Bar Plot and Scatter Plot
#Extras done is Used multiple aspects of a single data source in your analysis


# In[19]:


import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt
import seaborn as sns 


# In[4]:


#read csv file 
df = pd.read_csv('airlines.csv')


# In[5]:


#mean/average of flights on time 
flight_avg = df['Statistics.Flights.On Time'].mean()
print(flight_avg)

#average amount of flights on time are about 9254 flights 


# In[ ]:


#average amount of flights on time are about 9254 flights 


# In[7]:


#finding the median of Statistics.# of Delays.Weather

weatherdelay = df['Statistics.# of Delays.Weather'].median()
print(weatherdelay)

#median of weather delays is 58 


# In[13]:


#Data visualization of boxplot using seaborn 

sns.set_theme(style = 'whitegrid')
ax = sns.barplot(x = 'Time.Month Name', y = 'Statistics.# of Delays.Weather', data = df)

ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.tight_layout()
plt.show()


# In[ ]:


#shows the most amount of delays due to weather was in June 


# In[24]:


#shows/finds correlation between columns in dataset 
df.corr()


# In[33]:


data = df
month = data['Time.Month']#sets physical health to the physical health column 
flightcancelled = data['Statistics.Flights.Cancelled'] #sets BMI to BMI column 
plt.scatter(month,flightcancelled, edgecolor = 'black', linewidth=1, alpha =.75)
plt.title('Month and Flights Cancelled')
plt.xlabel('Month')
plt.ylabel('FlightCancelled')
plt.tight_layout()


# In[ ]:


#Shows poor correlation between the month and the amount of flights cancelled 

