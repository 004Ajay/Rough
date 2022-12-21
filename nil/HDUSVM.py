

# In[1]:


import pandas as pd
import numpy as np

#heart = pd.read_csv("heart.csv")
heart = pd.read_csv('heart_disease.csv')
heart.head()


# In[2]:


labels= np.array(heart.iloc[:,-1:])


# In[4]:


features= np.array(heart.iloc[:,:13])


# In[9]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=0)


# In[10]:


from sklearn.preprocessing import StandardScaler
# define min max scaler
scaler = StandardScaler()
# transform data
X_train_scaled = scaler.fit_transform(X_train)


# In[11]:


X_train_scaled


# In[12]:


X_test_scaled = scaler.fit_transform(X_test)
X_test_scaled


# ### Linear Kernel

# In[13]:


from sklearn.svm import SVC
svm_linear = SVC(kernel='linear', C=0.01)
svm_linear.fit(X_train_scaled, y_train)
print("Accuracy:", svm_linear.score(X_train_scaled, y_train))


# In[14]:


print("Accuracy:", svm_linear.score(X_test_scaled, y_test))


# In[15]:


from sklearn.svm import SVC
svm_linear = SVC(kernel='linear', C=100)
svm_linear.fit(X_train_scaled, y_train)
print("Accuracy:", svm_linear.score(X_train_scaled, y_train))


# In[16]:


print("Accuracy:", svm_linear.score(X_test_scaled, y_test))


# ### Polynomial Kernel

# In[17]:


# Degree = 2
svm_degree_2 = SVC(kernel='poly', degree=2)
svm_degree_2.fit(X_train_scaled, y_train)
print("Polynomial kernel of degree = 2")
print("Accuracy:", svm_degree_2.score(X_train_scaled, y_train))


# In[18]:


print("Accuracy:", svm_degree_2.score(X_test_scaled, y_test))


# In[19]:


# Degree = 4
svm_degree_4 = SVC(kernel='poly', degree=4)
svm_degree_4.fit(X_train_scaled, y_train)
print("Polynomial kernel of degree = 4")
print("Accuracy:", svm_degree_4.score(X_train_scaled, y_train))


# In[20]:


print("Accuracy:", svm_degree_4.score(X_test_scaled, y_test))


# ### RBF Kernel

# In[21]:


# gamma = 0.1
svm_gamma_01 = SVC(kernel='rbf', gamma=0.1)
svm_gamma_01.fit(X_train_scaled, y_train)
print("Gamma = 0.1")
print("Accuracy:", svm_gamma_01.score(X_train_scaled, y_train))


# In[22]:


print("Accuracy:", svm_gamma_01.score(X_test_scaled, y_test))


# In[23]:


# gamma = 1
svm_gamma_1 = SVC(kernel='rbf', gamma=1)
svm_gamma_1.fit(X_train_scaled, y_train)
print("Gamma = 1")
print("Accuracy:", svm_gamma_1.score(X_train_scaled, y_train))


# In[24]:


print("Accuracy:", svm_gamma_1.score(X_test_scaled, y_test))

