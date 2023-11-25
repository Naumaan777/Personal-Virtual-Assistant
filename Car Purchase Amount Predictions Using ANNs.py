#!/usr/bin/env python
# coding: utf-8

# 
# # CODE TO PREDICT CAR PURCHASING DOLLAR AMOUNT USING ANNs (REGRESSION TASK)

# # PROBLEM STATEMENT

# You are working as a car salesman and you would like to develop a model to predict the total dollar amount that customers are willing to pay given the following attributes: 
# - Customer Name
# - Customer e-mail
# - Country
# - Gender
# - Age
# - Annual Salary 
# - Credit Card Debt 
# - Net Worth 
# 
# The model should predict: 
# - Car Purchase Amount 

# # STEP #0: LIBRARIES IMPORT
# 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # STEP #1: IMPORT DATASET

# In[2]:


car_df = pd.read_csv('Car_Purchasing_Data.csv', encoding='ISO-8859-1') 
#Encoding is to take care of special characters


# In[3]:


car_df


# # STEP #2: VISUALIZE DATASET

# In[4]:


sns.pairplot(car_df)


# # STEP #3: CREATE TESTING AND TRAINING DATASET/DATA CLEANING

# In[5]:


X = car_df.drop(['Customer Name', 'Customer e-mail', 'Country', 'Car Purchase Amount'], axis = 1)
#axis = 1 is column axis=0 is row

# In[ ]:





# In[6]:


X


# In[7]:


y = car_df['Car Purchase Amount']
y.shape


# In[8]:


from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)


# In[9]

X_scaled

scaler.data_max_


# In[10]:


scaler.data_min_


# In[11]:


print(X_scaled[:,0])


# In[12]:


y.shape


# In[13]:


y = y.values.reshape(-1,1)
# This is required otherwise scaling below for y output will fail

# In[14]:


y.shape


# In[15]:


y_scaled = scaler.fit_transform(y)


# In[16]:


y_scaled


# # STEP#4: TRAINING THE MODEL

# In[17]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size = 0.25)

#default value of test_size is 25%.
# In[18]:


import tensorflow.keras
from keras.models import Sequential
from keras.layers import Dense  # fully connected artificial network, multiple hidden layers 
from sklearn.preprocessing import MinMaxScaler

model = Sequential()
model.add(Dense(25, input_dim=5, activation='relu'))
# 25 neurons, 5 features - first hidden layer
model.add(Dense(25, activation='relu'))
# 25 neurons, 5 features - second  hidden layer
model.add(Dense(1, activation='linear'))  # 1 output layer.
model.summary()
#Parameteres include bias  5 features mean five weights per neuron

# In[19]:


model.compile(optimizer='adam', loss='mean_squared_error') 
#adam is like the gradient descent to minimise the cost function

# In[20]:


epochs_hist = model.fit(X_train, y_train, epochs=20, batch_size=25,  verbose=1, validation_split=0.2)
# epochs = 20, - iterations as part of backward propagation
#validation split - validation data is subset of training data to avoid overfitting
# # STEP#5: EVALUATING THE MODEL 
# try epochs 100 and check the mean square error
# In[21]:
# if we have to change epochs or batch size need to restart the kernel and execute the full script

print(epochs_hist.history.keys())  # 


# In[22]:


plt.plot(epochs_hist.history['loss'])
plt.plot(epochs_hist.history['val_loss'])

plt.title('Model Loss Progression During Training/Validation')
plt.ylabel('Training and Validation Losses')
plt.xlabel('Epoch Number')
plt.legend(['Training Loss', 'Validation Loss'])


# In[23]:


# Gender, Age, Annual Salary, Credit Card Debt, Net Worth

X_Testing = np.array([[1, 50, 50000, 10985, 629312]])


# In[24]:


y_predict = model.predict(X_Testing)
y_predict.shape


# In[25]:


print('Expected Purchase Amount=', y_predict[:,0])


# # EXCELLENT JOB! NOW YOU'VE MASTERED THE USE OF ANNs FOR REGRESSION TASKS! 
