#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Códigos para obtener la raíz cuadrada de un número en Python
    Utilice math.sqrt() para calcular la raíz cuadrada de un número en Python
    Utilice la función pow() para calcular la raíz cuadrada de un número en Python
    Utilice el operador ** para calcular la raíz cuadrada de un número en Python
    Utilice cmath.sqrt() para calcular la raíz cuadrada de un número en Python
    Utilice numpy.sqrt() para calcular la raíz cuadrada de un número en Python


# In[1]:


#Usar math.sqrt() para calcular la raíz cuadrada de un número 
import math
print(math.sqrt(16))


# In[2]:


#Usar math.sqrt() para calcular la raíz cuadrada de una lista de números 
import math

a = [4,2,6]
b = []

for i in a:
    b.append(math.sqrt(i))
print(b)


# In[3]:


#Uzar la función pow() para calcular la raíz cuadrada de un número 
print(pow(9,0.5))


# In[4]:


#Usar el operador ** para calcular la raíz cuadrada de un número 
print(9 ** (0.5))


# In[5]:


#Usar cmath.sqrt() para calcular la raíz cuadrada de un número 
import cmath

x = -16
print(cmath.sqrt(x))


# In[6]:


#Usar numpy.sqrt() para calcular la raíz cuadrada de un número
import numpy as np

a = [4,2,6]
print(np.sqrt(a))

