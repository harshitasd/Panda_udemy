#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd;
d =pd.read_csv(r'C:\Users\PF48H\OneDrive\Desktop\panda/amazon_reviews.csv')


# In[5]:


d['Id']


# In[6]:


type(d['Id'])


# In[7]:


type(d)


# In[8]:


type(d[['ProductId','UserId']])


# In[9]:


d[['ProductId','UserId']]


# In[10]:


d.columns


# In[11]:


d.dtypes


# In[12]:


d['ProductId']


# In[13]:


d['ProductId'].values


# In[14]:


d.head()


# In[15]:


d.tail(3)


# In[16]:


type(d['ProfileName'])


# In[17]:


d['ProfileName'].value_counts()


# In[18]:


d.describe()


# In[19]:


d.isnull()


# In[20]:


type(d.isna())


# In[21]:


d.shape


# In[ ]:





# In[22]:


d.isna().sum(axis=0)


# In[23]:


type(d.isna())


# In[24]:


d.dropna(subset=['HelpfulnessNumerator']).shape


# In[25]:


d.head(30)


# In[26]:


d['Score'].fillna(0).head(20)


# In[27]:


df=d.copy()


# In[28]:


df.fillna(0,inplace=True)


# In[29]:


df.isnull().sum()


# In[30]:


df.dtypes


# In[31]:


df.head()


# In[32]:


df['Score'].unique()


# In[33]:


df['Score'].astype(int)


# In[34]:


df['Score_updated']=df['Score'].astype(int)


# In[35]:


df.columns


# In[36]:


df.head(2)


# In[37]:


df.drop('Score',axis=1,inplace=True)


# In[38]:


df.head(2)


# In[39]:


df.dtypes


# In[40]:


df['Score_updated'].unique()


# In[41]:


Filter1=df['Score_updated']==5


# In[42]:


df[Filter1]


# In[43]:


df.sort_values(by='Score_updated', ascending=False).head(7)    # becoz of False  


# In[44]:


df['Text'][0]


# In[45]:


len(df['Text'][0])


# In[46]:


def count_length(Text):
    return len(Text)


# In[47]:


df['Text'].apply(count_length)


# for experienced people

# In[48]:


df["Text"].apply(lambda x :len(x))  # here x signifies each index, i guess


# ##Group by

# In[50]:


df.groupby(['UserId'])['Score_updated'].max()  #min(),sum() also same here


# In[51]:


df.groupby(['UserId'])['Score_updated'].count() 


# In[52]:


type(df.groupby(['UserId'])['Score_updated'].count() )


# In[53]:


df.groupby(['UserId'])['Score_updated'].count().reset_index()


# In[54]:


type(df.groupby(['UserId'])['Score_updated'].count().reset_index())


# # panda plots(basic)

# In[55]:


df['Score_updated'].value_counts().plot()


# In[56]:


df['Score_updated'].value_counts().plot(kind='bar')


# In[ ]:




