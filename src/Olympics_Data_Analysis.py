#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[2]:


df1 = pd.read_csv('athlete_events.csv')
df2 = pd.read_csv('noc_regions.csv')


# In[3]:


df1.head()


# In[4]:


df1.tail()


# In[5]:


df2.head()


# In[6]:


df2.tail()


# In[7]:


df1.shape


# In[8]:


df2.shape


# In[9]:


df = df1.merge(df2, on = 'NOC', how = 'left')
df.head()


# In[10]:


df.info()


# In[11]:


df.describe()


# In[12]:


df.isnull().sum()


# In[13]:


df.duplicated().sum()


# In[14]:


df.drop_duplicates(inplace = True)
df.duplicated().sum()


# In[15]:


df['Medal'].value_counts()


# In[16]:


df = pd.concat([df,pd.get_dummies(df['Medal'])],axis = 1)
df.head()


# In[17]:


df.groupby('NOC').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending = False).reset_index()


# In[18]:


df_New = df.drop_duplicates(subset = ['Team','NOC','Games','Year','Season','City','Sport','Event','Medal'])
df_New = df_New.groupby('NOC').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending = False).reset_index()


# In[19]:


df_New[df_New['NOC']== 'IND']


# In[20]:


df_New['Total'] = df_New['Gold'] + df_New['Silver'] + df_New['Bronze']
df_New.head()


# In[21]:


df['region'].value_counts().head()


# In[22]:


year = df['Year'].unique().tolist()
year.sort()
year.insert(0,'Overall')
year


# In[23]:


country = np.unique(df['region'].dropna().values).tolist()
country.sort()
country.insert(0,'Overall')
country


# In[24]:


df_medal = df.drop_duplicates(subset = ['Team','NOC','Games','Year','Season','City','Sport','Event','Medal'])
df_medal.head(3)


# In[25]:


def medal_tally(year , country):
    df_medal = df.drop_duplicates(subset = ['Team','NOC','Games','Year','Season','City','Sport','Event','Medal'])
    flag = 0
    if year == 'Overall' and country == 'Overall':
        temp_df = df_medal
    if year == 'Overall' and country != 'Overall':
        flag == 1
        temp_df = df_medal[df_medal['NOC']== country]
    if year != 'Overall' and country == 'Overall':
        temp_df = df_medal[df_medal['Year']== int(year)]
    if year != 'Overall' and country != 'Overall':
        temp_df = df_medal[(df_medal['Year'] == int(year)) & (df_medal['NOC'] == country)]
    if flag == 1:    
        Y = temp_df.groupby('NOC').sum()[['Gold','Silver','Bronze']].sort_values('Year').reset_index()
    else:
        Y = temp_df.groupby('NOC').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending = False).reset_index()

    Y['Total'] = Y['Gold'] + Y['Silver'] + Y['Bronze']
    
    print(Y)   


# In[26]:


medal_tally(year = '2016' , country = 'Overall')


# # OVERALL ANALYSIS
#  - Number of Editions
#  - Number of Cities
#  - Number of Events&sports
#  - Number of Athletes
#  - Participation Nation

# In[27]:


df.head(2)


# In[28]:


df['Year'].unique().shape[0]-1


# In[29]:


df['City'].unique().shape[0]


# In[30]:


df['Sport'].unique().shape[0]


# In[31]:


df['Event'].unique().shape[0]


# In[32]:


df['Name'].unique().shape[0]


# In[33]:


df['region'].unique().shape[0]


# In[34]:


df.head()


# In[35]:


df_nat = df.drop_duplicates(['Year','region'])['Year'].value_counts().reset_index().sort_values('index')
df_nat.rename(columns={'index':'Edition','Year':'Countries' },inplace = True)
df_nat


# In[36]:


fig = px.line(df_nat , x = 'Edition' , y = 'Countries')
fig.show()


# In[37]:


fig = px.scatter(df, x='Year', y='Age',title='Olympic Data Visualization', color='Sport'
                     ,hover_data=['Name', 'Team', 'Medal'])
fig.show()


# In[38]:


df_x = df.drop_duplicates(['Year','Sport','Event'])
plt.figure(figsize=(25,25))
sns.heatmap(df_x.pivot_table(index ='Sport',columns='Year',values='Event',aggfunc ='count').fillna(0).astype('int'),annot=True)


# In[39]:


df.dropna(subset=['Medal'])['Name'].value_counts().reset_index().merge(df,left_on = 'index',
                                                            right_on = 'Name', how = 'left')[['index','Name_x','Sport','NOC']].drop_duplicates('index').head(20)


# In[40]:


def successful (df,sport):
    temp_df = df.dropna(subset = ['Medal'])
    
    if sport != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == sport]
    df_x1 = temp_df['Name'].value_counts().reset_index().head(20).merge(df,left_on = 'index',right_on = 'Name', how = 'left')[['index','Name_x','Sport','region']].drop_duplicates('index').head(20)
    df_x1.rename(columns={'index':'Name_x','Name_x':'Medal'},inplace =True) 
    return df_x1


# In[41]:


successful(df,'Overall').head(20)


# In[ ]:





# In[ ]:





# In[42]:


# Medal distribution over time
sns.countplot(data=df, x='Year', hue='Medal')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Medal Distribution Over Time')
plt.xticks(rotation=90)
plt.show()


# In[43]:


# Distribution of athlete heights by sex
sns.boxplot(data=df, x='Sex', y='Height')
plt.xlabel('Sex')
plt.ylabel('Height')
plt.title('Distribution of Athlete Heights by Sex')
plt.show()


# In[44]:


# Top countries with the most medals
top_countries = df[df['Medal'].notnull()]['Team'].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.xlabel('Medal Count')
plt.ylabel('Country')
plt.title('Top Countries with the Most Medals')
plt.show()


# In[45]:


# Medal distribution by sport
sport_medals = df[df['Medal'].notnull()]['Sport'].value_counts().head(10)
sns.barplot(x=sport_medals.values, y=sport_medals.index)
plt.xlabel('Medal Count')
plt.ylabel('Sport')
plt.title('Medal Distribution by Sport')
plt.show()


# In[46]:


# Number of athletes in Summer vs. Winter Olympics
sns.countplot(data=df, x='Season')
plt.xlabel('Season')
plt.ylabel('Count')
plt.title('Number of Athletes in Summer vs. Winter Olympics')
plt.show()


# In[47]:


# Correlation matrix
import matplotlib.pyplot as plt
import seaborn as sns
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


# In[48]:


# Histogram of athletes' ages
plt.figure(figsize=(8, 6))
sns.histplot(df['Age'], bins=20, kde=True, color='skyblue')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Athletes\' Ages')
plt.show()


# In[49]:


# Bar plot for the count of medals by medal type
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Medal', palette='muted')
plt.xlabel('Medal')
plt.ylabel('Count')
plt.title('Count of Medals by Medal')
plt.show()


# In[50]:


# Box plot for athletes' BMI by sex
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Sex', y='Height', palette='pastel')
plt.xlabel('Sex')
plt.ylabel('BMI')
plt.title('Distribution of BMI by Sex')
plt.show()


# In[51]:


# Scatter plot of athletes' height and weight colored by sex
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Height', y='Weight', hue='Sex', palette='Set1', alpha=0.7)
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Scatter plot of Height vs. Weight')
plt.show()


# In[52]:


# Bar plot for the count of athletes by age group
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Age', palette='pastel')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.title('Count of Athletes by Age Group')
plt.show()


# In[ ]:




