#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import matplotlib.pyplot as plt


# In[14]:


# reads amount of files in a directory
files = [file for file in os.listdir('./Sales_Data')]

# make empty df
all_months_data = pd.DataFrame()

# for look iterates through directory and concats it on to empty dataframe
for file in files:
    df = pd.read_csv("./Sales_Data/" + file)
    all_months_data = pd.concat([all_months_data, df])

# save new file to new csv, index=false ignores savings the index column
all_months_data.to_csv("all_data.csv", index = False)


# In[15]:


all_data = pd.read_csv("all_data.csv")
all_data.head()


# In[19]:


# finding rows with NaN
nan_df = all_data[all_data.isna().any(axis=1)]
nan_df.head()


# In[24]:


# dropping NaN
all_data = all_data.dropna(how='all')


# In[25]:


# find rows containing 'Or', they didn't have a value and contained the same text as column names
all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']


# In[27]:


# adding a month column for readability
all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')
all_data.head()


# In[36]:


# converting columns to correct type
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered']) # int
all_data['Price Each'] = pd.to_numeric(all_data['Price Each']) # float


# In[40]:


# adding sales column
all_data["Sales"] = all_data['Quantity Ordered'] * all_data['Price Each']
all_data.head()


# In[43]:


# grouping sales column by month and sum
results = all_data.groupby('Month').sum()


# In[44]:


# plotting the sales by month
months = range(1, 13)  # month 1-12
plt.bar(months, results['Sales'])
plt.xticks(months)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month')
plt.show()


# In[45]:


# define a function to split the address line, gets first index after the comma
def get_city(address):
    return address.split(',')[1]

# gets the second index after the comma
def get_state(address):
    return address.split(',')[2].split(' ')[1]

all_data['City'] = all_data['Purchase Address'].apply(lambda x: get_city(x) + ", " + get_state(x))
city_sales = all_data.groupby('City').sum()
all_data.head()


# In[49]:


city_sales = all_data.groupby('City').sum()
city_sales


# In[51]:


# plotting sales by city
# uses the same order as city_sales results to match the groupby
cities = [city for city, df in all_data.groupby('City')]
# this below statement works, but is a different order than the city_sales results. use above statement
# city_sales = all_data['City'].unique()
plt.bar(cities, city_sales['Sales'])
plt.xticks(cities, rotation=90, size=8)
plt.ylabel('Sales in millions (USD)')
plt.xlabel('City Name')
plt.show()


# In[54]:


all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])
all_data['Hour'] = all_data['Order Date'].dt.hour
all_data['Minute'] = all_data['Order Date'].dt.minute
all_data['Count'] = 1
all_data.head()


# In[57]:


all_data.groupby(['Hour']).count()

# collects the ocurrence of an order placed on that hour
hours = [hour for hour, df in all_data.groupby('Hour')]

# display (x,y) hours by the count of occurrence on that hour
plt.plot(hours, all_data.groupby(['Hour']).count())
plt.xticks(hours)
plt.xlabel('Hour of Day')
plt.ylabel('Number of Orders')
plt.grid()
plt.show()


# In[61]:


# filtering all data by order id, finds duplicates
df = all_data[all_data['Order ID'].duplicated(keep=False)]
df.head(10)


# In[62]:


# new column consisting of the products ordered together, display on the same line
df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
df.head()


# In[63]:


# drop duplicates
df = df[['Order ID', 'Grouped']].drop_duplicates()
df.head()


# In[64]:


from itertools import combinations
from collections import Counter


# In[67]:


count = Counter()

# cycles through Grouped column and gets each item separated by a comma, updates counter
for row in df['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list, 2))) # the 2 annotates the 2 items found sold together, can do more

# displays top 10 most common
count.most_common(10)


# In[68]:


all_data.head()


# # What product sold the most?

# In[69]:


# grouping by product
product_group = all_data.groupby('Product')

# sum of quantity ordered column for each product
quantity_ordered = product_group.sum()['Quantity Ordered']

# iterates through product in product_group
products = [product for product, df in product_group]


# In[70]:


# plot bar graph
plt.bar(products, quantity_ordered)
plt.ylabel('Quantity Ordered')
plt.xlabel('Product Name')
plt.xticks(products, rotation=90, size=8)
plt.show()


# In[73]:


# gets all prices of diff products
prices = all_data.groupby('Product').mean()['Price Each']

# overlaying another set of data on previous chart
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.bar(products, quantity_ordered, color='g')
ax2.plot(products, prices, 'b-')

ax1.set_xlabel('Product Name')
ax1.set_ylabel('Quantity Ordered', color='g')
ax2.set_ylabel('Price ($)', color='b')
ax1.set_xticklabels(products, rotation=90, size=8)

plt.show()

