#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
datos=pd.read_csv('"Nombre del archivo".csv')
df=pd.DataFrame(datos)
df.reset_index().to_csv('DatosExportados"Nombre del archivo"_csv',header=True, Index=False)

