
# coding: utf-8

# ## 1: Introducing US Gun Deaths Data

# In[1]:


import csv
data = list(csv.reader(open("guns.csv")))
data


# ## 2: Removing Headers From A List Of Lists

# In[2]:


headers = data[0]
headers


# In[11]:


data = data[1:]
data[:5]


# ## Counting Gun Deaths By Year

# In[4]:


years = [each[1] for each in data]
years


# In[5]:


year_counts = {}
for each in years :
    if each in year_counts :
        year_counts[each] += 1
    else :
        year_counts[each] = 1
year_counts


# ## 4: Exploring Gun Deaths By Month And Year

# In[12]:


import datetime
dates = [datetime.datetime(year=int(each[1]),month=int(each[2]),day=1) for each in data]
print(dates[:5])
date_counts = {}
for each in dates : 
    if each not in date_counts :
        date_counts[each] = 1
    else :
        date_counts[each] += 1
print(date_counts)


# ## 5: Exploring Gun Deaths By Race And Sex

# In[13]:


sex = [each[5] for each in data]
sex_counts = {}
for each in sex :
    if each in sex_counts :
        sex_counts[each] += 1
    else :
        sex_counts[each] = 1
sex_counts


# In[14]:


race = [each[7] for each in data]
race_counts = {}
for each in race :
    if each in race_counts :
        race_counts[each] += 1
    else :
        race_counts[each] = 1
race_counts


# ## 6. Reading In A Second Dataset

# In[16]:


census = list(csv.reader(open("census.csv")))
census


# ## 7. Computing Rates Of Gun Deaths Per Race

# In[18]:


mapping = {
    'Asian/Pacific Islander': 15159516 + 674625,
    'Black': 40250635,
    'Hispanic': 44618105,
    'Native American/Native Alaskan': 3739506,
    'White': 197318956
}
race_per_hundredk = {}
for key, value in race_counts.items() :
    race_per_hundredk[key] = value / mapping[key] * 100000
race_per_hundredk


# ## 8. Filtering By Intent

# In[23]:


intents = [each[3] for each in data]
#we already have a race column extracted before 
homicide_race_counts = {}
for idx, value in enumerate(race) :
    if intents[idx] == "Homicide" :
        if value not in homicide_race_counts :
            homicide_race_counts[value] = 1
        else :
            homicide_race_counts[value] += 1
homicide_race_counts


# In[24]:


homicide_per_hundredk = {}
for key, value in homicide_race_counts.items() :
    homicide_per_hundredk[key] = value / mapping[key] * 100000
homicide_per_hundredk

