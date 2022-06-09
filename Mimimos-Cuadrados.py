#!/usr/bin/env python
# coding: utf-8

# 

# ## Estadística simple

# ###### Escriba una función que reciba una secuencia de datos y los almace en archivo que se llame data-aaaa-mm-dd-time-hh:mm:ss.txt 

# Una manera de introducir la fecha y la hora es con la siguiente biblioteca

# In[2]:


from datetime import datetime
now = datetime.now()


# In[3]:


print("The year is ", now.year)
print("The  month is ", now.month)
print("The  day is ",now.day)
print("The hour is ", now.hour)
print("The minute is ", now.minute)
print("The second is ", now.second)
print("The microsecond is ",now.microsecond)


# In[10]:


print(now.date( ) )
print (now.time( ) )


# In[5]:


print(type(str(now.date())))
print(now.time())


# In[111]:


file_name = "date-"+ str(now.date())+"-time-"+str(now.time())[:9]+"txt"


# In[112]:


file_name=file_name.replace(':', '.')


# In[113]:


print(file_name)


# In[114]:


file=open(file_name, "w")
file.close( )


# In[115]:


print("Ingrese los datos y para terminar pulse enter")

while True:
    
    datos = input()
    
    if len(datos) > 0:
        file = open(file_name, "a")
        file.write(datos + "\n")
        file.close()
        
    elif len(datos) == 0:
        break


# In[228]:


n = input("Ingrese los datos")
print(len(n))


# In[288]:


name = f'date-{now.date()}-{now.time()}'
name = name.replace(':', '.') + ".txt"
file = open(name, "w")
file.close()

stop = True

while stop:
    
    n = input("Ingrese los datos")
    
    if len(n) != 0:
        file = open(name, 'a')
        file.write(n+"\n")
    
        file.close()
    elif len(n) == 0:
        break
        
        


# ###### Escriba una función `average()` calcule la media de una serie de datos. 
# 
# Recordemos que la media se define como: $\overline{y} = \dfrac{ \sum_{i=0}^n y_i}{n}$

# In[289]:


import numpy as np


# In[290]:


datos = np.array([10, 10, 10, 9, 10, 9, 10, 10, 10, 10])


# In[312]:


def average(data):
    """esta función calcula la media de una serie de datos ya dada"""
    suma = 0  #es una variable que va a guardar todas la suma obtenida de la variable datos
    
    for i in data:
        suma = suma + i #se usa un ciclo for de i hasta data, donde se van sumando de uno en uno los datos que se tienen
    
    promedio = suma/len(data)  #a la variable promedio se le asigna la suma de los datos y se divide entre el número de datos que se tienen
    
    return promedio       


# In[292]:


average(datos)


# ###### Escriba una función `standard_deviation()` que calcule la desviación estándar de una serie de datos. 
# 
# La desviación estándar se define: $S_y = \sqrt{\dfrac{\sum_{i=0}^n(y_i - \overline{y})^2}{n-1}}$

# In[293]:


def standard_deviation(data):
    """esta función calcula la desviación estandar de una serie de datos a partir de la función average"""
    promedio = average(data)  #a la variable promedio le asignamos la llamada de la función average
    suma = 0  #a esta variable se le irán suamando los datos de i hasta n
    
    for i in data:
        suma = suma + (i - promedio)**2  #se aplica un ciclo for donde en suma se irá suamando el resultado que se tenga de suma, además se la suma el cuadrado de la resta de i por la variable promedio
    
    aux = (suma)/(len(data) - 1)  #a la variable auxiliar  se le realiza la división de la suma obtenida anteriormente entre el número de datos menos uno
    estandar = np.sqrt(aux) #a la variable estandar se le calcula la raíz cuadrada de la variable auxiliar
    
    return estandar
    


# In[294]:


datos


# In[295]:


standard_deviation(datos)


# ###### Defina una función que se llame `variance()` que calcule la varianza a parti de la de desviación estándar.
# 
# $\sigma = S_y^2$

# In[296]:


def variance (data):
    
    """esta función calcula la varianza a partir de la desviación estándar ya obtenida"""
    
    desviacion= standard_deviation(data) #se asigna una variable a la función standard_deviation
    varianza= desviacion **2 #a la variable varianza se le asigna el cuadrado de la variable desviacion
    
    return varianza


# In[297]:


datos


# In[298]:


variance (datos)


# ###### Escriba una función que se llame `coefficient_of_variation()`
# $c.v = \dfrac{S_y}{\overline{y}}100\%$

# In[299]:


def coefficient_of_variation(data):
    
    """esta función calcula el coeficiente de variación dividiendo la desviación estandar por el promedio y multiplicandolo por el 100%"""
    
    promedio= average(data)  #le se asigna a la variable promedio la llamada de la función average
    desviacion= standard_deviation(data) # a la variable desviacion se le asigna la llamada de la función standard_desviation
    variacion=(desviacion/promedio) * 100  #se realiza la división de las variables desviación entre promedio y a estas se les multiplica por el 100%
    
    return variacion


# In[300]:


datos


# In[301]:


coefficient_of_variation(datos)


# ###### Escriba una función que se llame `statistical_data()`, que abra un archivo  de datos.txt. En la segunda columna de poner el valor $y_i - \overline{y}$  para cada $i$ y al final del archivo debe estar el promedio y la desviación estándar.

# In[315]:


def statistical_data(data):
    
a=open (name, "r")
todo=a.read()
print(todo)


# ###### Usando las funciones anteriores y los siguientes datos los datos los siguientes datos: 
# 
# 8.8, 9.4, 10.0, 9.8, 10.1, 9.5, 9.8, 10.1, 9.2, 10.4, 7.9, 9.5, 8.9, 9.5, 9.6, 9.4, 10.0, 11.3, 9.4, 10.4, 9.8, 8.8, 10.6, 10.2, 8.9, 28.65, 26.55, 26.65, 27.65, 27.35, 28.35, 26.85, 28.65, 29.65, 27.85, 27.05, 28.25, 28.35, 26.75, 27.65, 28.45, 28.65, 28.45, 31.65, 26.35, 27.75, 29.25, 27.65, 28.65, 27.65, 28.55, 27.55, 27.25.
# 
# Determine:
# * La media. 
# * La desviación estándar. 
# * La varianza. 
# * El coeficiente de variación. 
# 
# 

# In[214]:


import numpy as np


# In[215]:


datitos= np.array([8.8, 9.4, 10.0, 9.8, 10.1, 9.5, 9.8, 10.1, 9.2, 10.4, 7.9, 9.5, 8.9, 9.5, 9.6, 9.4, 10.0, 11.3, 9.4, 10.4, 9.8, 8.8, 10.6, 10.2, 8.9, 28.65, 26.55, 26.65, 27.65, 27.35, 28.35, 26.85, 28.65, 29.65, 27.85, 27.05, 28.25, 28.35, 26.75, 27.65, 28.45, 28.65, 28.45, 31.65, 26.35, 27.75, 29.25, 27.65, 28.65, 27.65, 28.55, 27.55, 27.25])


# In[216]:


print(len(datitos))


# In[218]:


average(datitos)


# In[220]:


standard_deviation(datitos)


# In[224]:


variance(datitos)


# In[226]:


coefficient_of_variation(datitos)
    


# ## Regresión Lineal

# El ejemplo más simple de una aproximación por mínimos cuadrados es ajutar una línea recta a un conjunto de observaciones definidas por puntos: $(x_1, y_1), (x_2, y_2),\dots, (x_n, y_n)$. La expresión matemática para la línea recta es: $$y = a_0 + a_1x + e$$
# 
# Donde $a_0$ y $a_1$ son coeficientes que representan la intersección con el eje y y la pendiente, respectivamente, $e$ es el error, o diferencia, entre el modelo y las observaciones, el cual se representa al reordenar como: $$e = y - a_0 - a_1x$$
# 
# Así, el error o residuo es la discrepancia entre el valor verdadero de y y el valor aproximado, $a_0 + a_1x$, que predijo la ecuación lineal.
# 
# Se recomendienda al lector leer las notas *Regresión-lineal.pdf* ponga principal atención en el ejemplo 17.1, para tener una mejor idea del método.

# ###  Ajuste de una línea recta por mínimos cuadrados 

# Para determinar los valores de $a_0$ y $a_1$ se hace mediante las ecuaciones normales en forma simultanea:
# 
# 
# $$a_1 = \dfrac{n\sum x_i y_i - \sum x_i \sum y_i }{n\sum x_i^2 - \left(\sum x_i \right)^2}$$
# 
# $$a_0 = \overline{y} - a_1\overline{x}$$

# ###### Defina una función `coeffs()` que calcule los coeficientes $a_1$ y $a_0$.  

# In[263]:


import numpy as np


# In[264]:


data = np.array([[4, 1590], [8,1320], [12, 1000], [16,900], [20, 560], [24, 560]])


# In[180]:


len(data)


# In[181]:


data [0][0]


# In[182]:


data[:,1]


# In[265]:


def coeffs(datos):
    n=len(datos)
    
    suma_xy = 0 #es una variable para guardar la suma del producto de x e y
    for i in range (0, n):
        suma_xy = suma_xy + datos [i][0]* datos[i][1] #usamos un ciclo for para obtener la suma de la multiplicación de los datos asignados en x y en y
        
    suma_x = 0 #es una variable para guardar la suma de los valores x
    for i in range (0, n):
        suma_x = suma_x + datos [i][0] #usamos un ciclo for para obtener la suma de los valores de x
        
    suma_y = 0 #es una variable para guardar la suma de los valores y
    for i in range (0, n):
        suma_y = suma_y + datos [i][1] #usamos un ciclo for para obtener la suma de los valores de y
    
    suma_x2 = 0 #es una variable para guardar la suma de los valores x elevados al cuadrado
    for i in range (0, n):
        suma_x2 = suma_x2 + datos [i][0]**2 #usamos un ciclo for para obtener la suma de los valores de x elevados al cuadrado
        
    a1=(n*suma_xy-suma_x*suma_y)/(n*suma_x2-suma_x**2) #en esta variable se realiza en el numerador la multiplicacion de n por el producto de x e y, menos el producto de la suma de x y la suma de y. En el denominador se realiza el producto de n por la suma de x elevada al cuadrado, menos la suma de x al cuadrado
    a0=average(datos[:,1]-a1*average(datos[:,0])) #en esta variable se tiene el promedio de los datos obtenidos en y, menos el prodcuto de la variable a1 por el promedio de x
    
    return a0, a1
   


# In[184]:


a0, a1= coeffs(data)


# In[185]:


import matplotlib.pyplot as plt


# In[186]:


def lineal(a0, a1, x):
    return a0 + x*a1


# In[187]:


lineal(a0, a1, 32) #da la concentración en ese tiempo el número 32


# In[278]:


x=np.linspace(0, 25, 100)


# In[281]:


y=lineal (a0, a1, x)


# In[282]:


plt.scatter(data[:,0], data[:,1])
plt.plot(x, y, color="c")


# In[191]:


coeffs(data)


# A la siguiente expresión se le conoce como *cociente de correlación* En un ajuste perfecto, r = 1, significa que la línea explica el 100% de la variabilidad de los datos. Si r = 0,  el ajuste no representa alguna mejora:
# 
# $$r = \dfrac{n\sum x_i y_i - \sum x_i \sum y_i }{\sqrt{n\sum x_i^2 - \left(\sum x_i \right)^2}\sqrt{n\sum y_i^2 - \left(\sum y_i \right)^2}}$$
#  

# ###### Defina una función `correlation()` que calcule el coeficiente de correlación para un conjunto de datos. 

# In[196]:


import numpy as np


# In[197]:


data = np.array([[4, 1590], [8,1320], [12, 1000], [16,900], [20, 560], [24, 560]])


# In[198]:


def correlation(datos):
    n=len(datos)
    suma_xy = 0 #es una variable para guardar la suma del producto de x e y
    for i in range (0, n):
        suma_xy = suma_xy + datos [i][0]* datos[i][1] #usamos un ciclo for para obtener la suma de la multiplicación de los datos asignados en x y en y
        
    suma_x = 0 #es una variable para guardar la suma de los valores x
    for i in range (0, n):
        suma_x = suma_x + datos [i][0] #usamos un ciclo for para obtener la suma de los valores de x
        
    suma_y = 0 #es una variable para guardar la suma de los valores y
    for i in range (0, n):
        suma_y = suma_y + datos [i][1] #usamos un ciclo for para obtener la suma de los valores de y
    
    suma_x2 = 0 #es una variable para guardar la suma de los valores x elevados al cuadrado
    for i in range (0, n):
        suma_x2 = suma_x2 + datos [i][0]**2 #usamos un ciclo for para obtener la suma de los valores de x elevados al cuadrado                                                                                                                                                     c
        
    suma_y2=0 #es una variable para guardar la suma de los valores y elevados al cuadrado
    for i in range (0, n):
        suma_y2=suma_y2 + datos [i][1]**2 #usamos un ciclo for para obtener la suma de los valores de y elevados al cuadrado       
        
    raiz1=np.sqrt(n*suma_x2-suma_x**2) #se realiza la raíz cuadrad del producto de n por mas suma de la variable suma_x2, restandole la variable suma_x elevada al cuadrado
    raiz2=np.sqrt(n*suma_y2-suma_y**2) ##se realiza la raíz cuadrad del producto de n por mas suma de la variable suma_y2, restandole la variable suma_y elevada al cuadrado
        
    r=(n*suma_xy-suma_x*suma_y)/ (raiz1*raiz2)  #en esta variable se realiza en el numerador la multiplicacion de n por el producto de x e y, menos el producto de la suma de x y la suma de y. Dividiendola por el producto de las variables raíz 1 y raiz 2
    
    return r
   


# In[199]:


correlation(data)


# #### Escriba una función que se llame `least_square()`, que reciba el nombre de un archivo donde tomará los datos, calule la aproximación lineal, el coeficiente de correlación y grafique los datos y la aproximación.

# In[ ]:





# Después de una tormenta, se vigila la concentración de la bacteria E. coli en un área de natación:
# 
# |   t(hrs)   |  4 |  8 | 12 | 16 | 20 | 24 |
# |------------|----|----|----|----|----|----|
# |c(CFU/100mL)|1590|1320|1000| 900| 560| 560|
# 
# 
# El tiempo se mide en horas transcurridas después de finalizar la tormenta, y la unidad CFU es una “unidad de formación de colonia”. Use los datos y la regresión por minímos cuadrados para estimar
# 
# * La concentración al final de la tormenta (t = 0).
# * El tiempo en el que la concentración alcanzará 200 CFU / 100 mL. Observe que la elección del modelo debe ser consistente con el hecho de que las concentraciones negativas son imposibles y de que la concentración de bacterias siempre disminuye con el tiempo.

# In[266]:


coeffs(data)


# In[268]:


lineal(a0, a1, 0) #da la concentración final de la tormenta cuando t=0


# In[ ]:




