#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


heart = pd.read_csv('heart.csv')
heart.head()


# In[3]:


index=['HeartDisease', 
       'Smoking', 
       'AlcoholDrinking', 
       'Stroke', 
       'DiffWalking', 
       'Diabetic',
       'PhysicalActivity',
       'Asthma', 
       'KidneyDisease', 
       'SkinCancer']

def to_bin(sers):
    if sers == "Yes":
        return 1
    if sers == "No":
        return 0

for col in index:
    heart[col] = heart[col].apply(to_bin)


# In[4]:


heart.head()


# In[5]:


heart['PhysicalHealth'].unique() # range from 0 to 30
heart['MentalHealth'].unique() # range from 0 to 30


# In[6]:


def sex(sers):
    if sers == "Male":
        return 1
    if sers == "Female":
        return 0
heart['Sex'] = heart['Sex'].apply(sex)


# In[7]:


heart["GenHealth"].unique()


# In[8]:


heart[:].shape


# In[9]:


gen_dict = {"Poor": 1, "Fair": 2, "Good": 3, "Very good": 4, "Excellent": 5}

def gen(sers):
    return gen_dict[sers]

heart["GenHealth"] = heart["GenHealth"].apply(gen)


# In[10]:


heart


# In[11]:


heart["AgeCategory"].unique()


# In[12]:


age_dict = {'18-24': 1, '25-29': 2, 
            '30-34': 3, '35-39': 4, 
            '40-44': 5, '45-49': 6, 
            '50-54': 7, '55-59': 8, 
            '60-64': 9, '65-69': 10, 
            '70-74': 11, '75-79': 12,
            '80 or older': 13}
def age(sers):
    return age_dict[sers]

heart["AgeCategory"] = heart["AgeCategory"].apply(age)


# In[13]:


heart.head()


# In[14]:


heart["Race"].unique()


# In[15]:


race_dict = {'American Indian/Alaskan Native': 1,
             "Asian": 2,
             "Black": 3,
             "Hispanic": 4,
             "White": 5,
             "Other": 6}

def race(sers):
    return race_dict[sers]


# In[16]:


heart["Race"] = heart["Race"].apply(race)


# In[17]:


heart.columns


# In[18]:


h = heart[heart['HeartDisease'] == 1]
h["AlcoholDrinking"].sum()/h["AlcoholDrinking"].count() # 4% not too high

heart

def var(hrt):
    final = []
    
    for elem in hrt.columns:
        if hrt[elem].nunique() == 2: # binary
            print(elem)
            final.append(((hrt[elem].sum()/hrt[elem].count()), elem))
#         else:
#             print(elem)
#         elif elem != 'HeartDisease':
#             final.append((hrt[elem]))
    return sorted(final)

var(h)


# In[19]:


heart.dtypes


# In[ ]:





# In[20]:


h['AgeCategory'].mean(), h['AgeCategory'].median(), h['AgeCategory'].mode() 
# 65-69 avg
# most common in dataset is 80 or older!


# In[21]:


h['BMI'].mean(), h['BMI'].median(), h['BMI'].mode()
# avg is around 29
# most common is around 26 so -- overweight is more likely


# In[22]:


heart = heart.dropna()


# In[23]:


heart.to_csv('clean_heart.csv', index=False)


# In[ ]:





# In[25]:


from sklearn import preprocessing
import matplotlib.pyplot as plt 
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)


# In[28]:


X = heart.loc[:, heart.columns != 'HeartDisease']
y = heart.loc[:, heart.columns == 'HeartDisease']
from imblearn.over_sampling import SMOTE
os = SMOTE(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
columns = X_train.columns
os_data_X,os_data_y=os.fit_resample(X_train, y_train)
os_data_X = pd.DataFrame(data=os_data_X,columns=columns )
os_data_y= pd.DataFrame(data=os_data_y,columns=['HeartDisease'])
# we can Check the numbers of our data
print("length of oversampled data is ",len(os_data_X))
print("Number of people without heart disease in oversampled data",len(os_data_y[os_data_y['HeartDisease']==0]))
print("Number of people with heart disease",len(os_data_y[os_data_y['HeartDisease']==1]))
print("Proportion of no heart disease data in oversampled data is ",len(os_data_y[os_data_y['HeartDisease']==0])/len(os_data_X))
print("Proportion of heart disease data in oversampled data is ",len(os_data_y[os_data_y['HeartDisease']==1])/len(os_data_X))


# In[31]:


data_final_vars=heart.columns.values.tolist()
y=['HeartDisease']
X=[i for i in data_final_vars if i not in y]
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(max_iter=1000)
rfe = RFE(logreg, n_features_to_select=19)
rfe = rfe.fit(os_data_X, os_data_y.values.ravel())
print(rfe.support_)
print(rfe.ranking_)


# In[32]:


cols = ['BMI', 'Smoking', 'AlcoholDrinking', 'Stroke', 'PhysicalHealth',
       'MentalHealth', 'DiffWalking', 'Sex', 'AgeCategory', 'Race', 'Diabetic',
       'PhysicalActivity', 'GenHealth', 'SleepTime', 'Asthma', 'KidneyDisease',
       'SkinCancer']


# In[33]:


X=os_data_X[cols]
y=os_data_y['HeartDisease']


import statsmodels.api as sm
logit_model=sm.Logit(y,X)
result=logit_model.fit()
print(result.summary2())


# In[34]:


cols = ['BMI', 'Smoking', 'AlcoholDrinking', 'MentalHealth', 'DiffWalking', 
        'Sex', 'AgeCategory', 'Race', 'Diabetic', 'PhysicalActivity', 
        'GenHealth', 'SleepTime', 'Asthma', 'KidneyDisease', 'SkinCancer']
X=os_data_X[cols]
y=os_data_y['HeartDisease']


import statsmodels.api as sm
logit_model=sm.Logit(y,X)
result=logit_model.fit()
print(result.summary2())


# In[41]:


from sklearn.linear_model import LogisticRegression
from sklearn import metrics
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
logreg = LogisticRegression(max_iter=10000)
logreg.fit(X_train, y_train)


# In[42]:


y_pred = logreg.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))


# In[43]:


from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)


# In[44]:


from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))


# In[45]:


from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
logit_roc_auc = roc_auc_score(y_test, logreg.predict(X_test))
fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(X_test)[:,1])
plt.figure()
plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.savefig('Log_ROC')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




