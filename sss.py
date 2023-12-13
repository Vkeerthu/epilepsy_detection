#!/usr/bin/env python
# coding: utf-8

# # import packages

# In[33]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# In[5]:


get_ipython().system('pip3 install numpy')
get_ipython().system('pip3 install pandas')
get_ipython().system('pip3 install torch')
get_ipython().system('pip3 install -Uqq fastbook')
get_ipython().system('pip3 install --user graphviz')
print("Done")


# In[6]:


import numpy as np
import pandas as pd
import torch
from fastai.tabular.all import *


# # data preparation

# In[7]:


raw_data = pd.read_csv(r'C:\Users\nielit\Downloads\data.csv')


# In[8]:


raw_data.head()


# # Split the Dataset into Training Set & Test Set

# In[9]:


# Percentage to split by for training
perc = 90

# Set for training the model
data = raw_data.head(int(len(raw_data)*(perc/100))).copy()

# Set for testing the model later to get the real accuracy
test_set = raw_data.tail(int(len(raw_data)*((100-perc)/100))).copy()


# In[10]:


data


# # Format Data for Training

# In[11]:


cont_names_data = list(data.columns.values)
cont_names_data.remove("Unnamed: 0")
cont_names_data.remove('y')


# In[12]:


cat_names_data = []
for i in data["Unnamed: 0"]:
    cat_names_data.append(i)


# In[13]:


data['y'].replace(2, 0, inplace=True)
data['y'].replace(3, 0, inplace=True)
data['y'].replace(4, 0, inplace=True)
data['y'].replace(5, 0, inplace=True)


# In[14]:


data


# # Making and Training the Tabular Model

# In[15]:


splits = RandomSplitter(valid_pct=0.3, seed=None)(range_of(data))

to = TabularPandas(
    data,
    cont_names = cont_names_data,
    procs = [Normalize, FillMissing, Categorify],
    splits = splits,
    y_block = CategoryBlock,
    y_names= "y"
)

dls = to.dataloaders(bs=256)
dls.show_batch()


# In[20]:


import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="fastai.torch_core")


# # Training

# ## Find the best learning rate

# In[21]:


f1score = F1Score()

# Assuming you have already defined dls and cont_names_data
learn = tabular_learner(dls, metrics=[f1score, accuracy, error_rate])
lr_min = learn.lr_find()
print(lr_min)


# In[22]:


f1score = F1Score()

# learn = tabular_learner(dls, metrics=[accuracy, error_rate, f1score])
learn = tabular_learner(dls, metrics=[f1score, accuracy, error_rate])
lr_min, lr_steep = learn.lr_find()
print(lr_min)
print(lr_steep)


# # Train the Model

# In[23]:


learn.fit(n_epoch=100, lr=lr_min)


# # Save the Model

# In[24]:


name = "EEG_torch"
# save_format = int(input("Which format to save the model:\n\t1. .pt - PyTorch\n\t2. pkl - FastAi\n1 or 2:"))
save_format = 1
# Try both of them and let me know which one works
if save_format == 1:
    torch.save(learn, name + ".pt")
    print("Saved the model using torch")
elif save_format == 2:
    learn.export(name + ".pkl")
    print("Saved the model using FastAi")
else:
    print("Did not work")


# # Test the Model with Test Set

# In[25]:


if save_format == 1:
    model = torch.load(name + ".pt")
    print("Loaded the .pt model using torch")
elif save_format == 2:
    model = torch.load(name + ".pkl")
    print("Loaded the .pkl model using torch")
else:
    print("Did not work")


# In[26]:


def get_row(row_number):
    # print(test_set.iloc[row_number].iloc[1:])
    row = test_set.iloc[row_number].iloc[1:-1]
    return row


# In[27]:


row_num = 232
row, clas, probs = model.predict(get_row(row_num))


# In[28]:


row.show()


# In[34]:


print(clas.int())

#result = torch.round(torch.abs(clas))

if clas.int() == 1:
    print("Seizure Detected")
else:
    print("No Seizure Detected")


# In[29]:


test_set


# In[30]:


test_set['y'].replace(1, 1, inplace=True)
test_set['y'].replace(2, 0, inplace=True)
test_set['y'].replace(3, 0, inplace=True)
test_set['y'].replace(4, 0, inplace=True)
test_set['y'].replace(5, 0, inplace=True)


# In[31]:


test_set


# In[32]:


correct = 0
wrong = 0

for i in range(10350, 11500):
    row, clas, probs = model.predict(get_row(i-10350))
    if clas.int() == test_set['y'][i]:
        correct += 1
    else:
        print(i)
        print(str(clas.int()) + ", " + str(test_set['y'][i]))
        wrong += 1
print("Correct: ", correct)
print("Wrong: ", wrong)
print("Percent: " + str(correct / (correct + wrong)))


# In[ ]:




