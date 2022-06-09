#!/usr/bin/env python
# coding: utf-8

# # **Introducción a SymPy**

# ### ***Índice***
# * [1. ¿Qué es SymPy?](#¿Qué-es-SymPy?) 
# * [2. Creación de expresiones en SimPy](#Creación-de-expresiones-en-SimPy)
#     * [2.1. Símbolos](#Símbolos)
#     * [2.2. Funciones](#Funciones)
# * [3. Manipulación de expresiones](#Manipulación-de-expresiones)
#     * [3.1. Substitución](#Substitución)
#     * [3.2. Simplificación](#Simplificación)
#     * [3.3. Evaluación númerica](#Evaluación-númerica)
# * [4. Calcúlo con SymPy](#Calcúlo-con-SymPy)
#     * [4.1.Derivadas](#Derivadas)
#     * [4.2. Integrales](#Integrales)
#     * [4.3. Límites](#Límites)
#     * [4.4. Taylor series](#Taylor-series)
#     * [4.5. Resolver ecuaciones](#Resolver-ecuaciones)
# * [5.Algunas funciones creadas con SymPy](#Algunas-funciones-creadas-con-SymPy)
#     * [5.1. Graficas de función, derivada y función primitiva](#Graficas-de-función,-derivada-y-función-primitiva)
#     * [5.2. Calculo de área entre dos funciones](#Calculo-de-área-entre-dos-funciones)
# * [6. Bibliografía](#Bibliografía)

# ![][imagen] 
# 
# [imagen]:https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Sympy_logo.svg/1200px-Sympy_logo.svg.png

# ## ¿Qué es SymPy?
# 
# SymPy es un sistema de álgebra informática (CAS) escrito en el lenguaje de programación Python . SymPy es fácil de usar e instalar y funciona en todos los lugares donde está instalado Python 2.7 o posterior.
# 
# Simpy es una paquetería que nos permite hacer cálculo simbólico y numérico, contiene funciones y aplicaciones que son muy útiles para elaborar cálculo complejo 
# 
# Un sistema de álgebra de computadora (CAS) es un programa de computadora diseñado para manipular matemáticas
# , expresiones temáticas en forma simbólica en lugar de numérica, una tarea que se lleva a cabo
# por científicos teóricos. Hay una serie de programas especializados y algunos
# sistemas de propósito aplicables a una amplia gama de problemas, y es este último el que
# considerar aquí.
# 
# La característica más sorprendente de SymPy es que está escrito completamente en Python y, de hecho, es solo un módulo adicional. Es pequeño y funciona en cualquier sistema Python. Interfaces Bueno, a NumPy para números y a Matplotlib para gráficos. El modo terminal estándar
# tiene una salida poco sofisticada, pero, naturalmente, se puede utilizar dentro del portátil Jupyter, y
# allí ofrece quizás el mejor formato disponible actualmente de complicados simbólicos
# salida. 
# 
# 
# 
# 
# Simpy es una paquetería de Python que utiliza y recibe el lenguaje de python, en la paquetería podemos encontrar la creación e interpretación de símbolos y funciones e incluye funciones que nos permiten crear funciones matemáticas más complejas ya que simpy cuanta con funciones como derivar, integrar, simplificar expresiones e incluye el reconocimiento e interpretación de números enteros, racionales, flotantes y números complejos, entre otras características más, todo ello da como resultado que simpy sea una paquetería que nos brinda múltiples herramientas para realizar calculo y programas matemáticos de manera mucho más sencilla y eficaz.
# 
# 

# # Símbolos

# El verdadero poder de las matemáticas viene
# del uso de variables algebraicas. Para ello, debe utilizar los objetos Symbol. Para crearlos,
# debe especificar su nombre y, opcionalmente, puede especificar varios "supuestos" sobre el
# variable. Los supuestos disponibles incluyen "entero", "real", "positivo", etc. Si ninguno es
# especificado, el objeto Símbolo se trata como una variable compleja. Implicaciones entre propiedades
# se tienen en cuenta automáticamente y las combinaciones imposibles provocan un error. 
# 
# Hay varias formas de crear instancias de clases, y quizás la forma más común de manejar
# insertar la línea x, y = sy.symbols ("x y")
# 
# 
# La función de símbolos () facilita la creación de muchos símbolos a la vez. La palabra clave
# los argumentos que le da se pasan al constructor Symbol (). Para el primer argumento,
# acepta un mini-lenguaje inspirado en la notación de segmento de Python, que se describe mejor
# con el siguiente ejemplo:

# In[1]:


from sympy import *


# Podemos crear símbolos usando la función symbols()  y podemos crear varios símbolos a la vez  como se muestra a continuación 

# In[2]:


x = symbols('x')
t, y, z = symbols('t y z')


# In[3]:


z = Symbol('z') # variable compleja 
x = Symbol('x', real=True) #simbolo entre los reales
a = Symbol('a', positive=True) # simbolo en los positivos


# In[4]:


print(type(x))
print(type(t))


# También podemos crear una serie de símbolos usando literales indicando la letra de inicio y el límite.

# In[5]:


symbols('a:c, i:k')


# Al igual que con las literales se puede utilizar un símbolo con un subíndice colocando primero el símbolo y después numero de símbolos que se desea crear, se puede indicar desde que subíndice se desea empezar.

# In[6]:


symbols('x:5')


# In[7]:


symbols('x3:12')


# Lo importante de definir y trabajar con símbolos es porque SymPy utiliza la sintaxis de Python y si nosotros no definimos como símbolo a una variable Python lo va a reconocer como una variable que no está definida y nos va a saltar un error, al definir los símbolos Python los reconoce como una variable aunque aún no se le defina un valor en concreto. 
# 
# A continuación se muestra el ejemplo:
# 

# In[8]:


s**2


# In[9]:


s = symbols('S')


# In[10]:


s**2


# Al definir los símbolos también podemos trabajar operaciones aritméticas y SymPy va a simplificar los términos semejantes  

# In[11]:


3*x**2 + 7*y + 2*x**2 + (-5*y) - 4*x**2


# In[ ]:





# # Funciones

# En SymPy podemos usar y ejecutar funciones matemáticas y dado a que ya hemos creado símbolos antes podemos aplicarle funciones a nuestros símbolos de esta manera obtenemos una expresión resumida o resuelta pero de forma simbólica es decir que aún no evaluamos valores numéricos, prácticamente como si de cálculo teórico se tratase.
# 
# Dentro de la creación de funciones al utilizar el lenguaje de Python, podemos definir funciones como previamente ya conocemos y SymPy va a trabajar con ellas sin problemas, además también podemos definir funciones simbólicas esto quiere decir que se expresa que es una función pero no se tiene que definir.
# 
# 

# In[12]:


f = Function('f')


# In[13]:


print(type(f))
f(0)


# Aquí definimos una función utilizando el recurso de función anónima lambda que reciba de argumento a  ‘x’
# 

# In[14]:


g =lambda x: x**2 + 3*x - 21
g(x)


# También podemos introducir otros símbolos  o variables matemáticas que ya hayamos definido antes 

# In[15]:


g(x*y**2/3)


# In[16]:


g(x**2 + 3)


# In[17]:


g(3)


# SymPy tiene dentro de su paquetería funciones como sin, cos, tan, pi, exp entre otras por esto mismo es que Sympy nos puede simplificar bastante el cálculo.
# 
# 
# 
# 

# In[18]:


f = cos(exp(sin(x**pi)))
f


# Dentro de SymPy podemos crear expresiones matemáticas solo usando la sintaxis de Python y con ellas ya podremos realizar el cálculo en SymPy 

# # Manipulación de expresiones

# # Substitución

# Los objetos y expresiones de SymPy son inmutables. Transformarlos en realidad significa crear
# un nuevo objeto que difiere del inicial de alguna manera. La forma más directa de hacer esto es
# utilice el método .subs (). subs (antiguo, nuevo) devuelve una nueva expresión donde todos los
# las ocurrencias de lo antiguo en la expresión han sido reemplazadas por nuevas. Para reemplazar varias expresiones diferentes
# de una sola vez se debe pasar como un solo argumento a un diccionario de los pares {antiguo: nuevo},
# como se muestra en el siguiente ejemplo:

# In[19]:


x, y = symbols('x, y', real=True)
f = lambda x, y:(cos(x) * exp(y))
f(x, y)


# Si colocamos dentro de la función subs() un diccionario con los símbolos que deseamos sustituir podemos cambiar los varios valores a la vez

# In[20]:


f(x,y).subs({x: pi, y: 2})


# In[21]:


funcion = exp(x+1)/(x**2-2)
funcion


# A continuación tenemos un ejemplo de como sympy con el métodos .subs() puede cambiar de símbolos que son variables complejas a valores u otras variables 

# In[22]:


funcion.subs(x,2)


# # Simplificación 

# Simplificación
# Cuando tienes una expresión simbólica, una necesidad común es ponerla en una forma más corta o que
# es más fácil de entender. Casi siempre es más conveniente tratar con 1 que con $cos (x^2)
# + sin (x^2)$. Aquí es donde entra en uso la función simplify ().
# simplify () aplica una combinación heurística de algoritmos de simplificación. Puede usar
# relaciones trigonométricas, aplicar propiedades de logaritmos y exponenciales, simplificar fracciones
# y raíces cuadradas, etc. En todas estas operaciones, se tienen en cuenta las propiedades de
# los objetos, particularmente is_positive e is_real, como se muestra en el siguiente ejemplo:

# In[23]:


f = cos(x)**2 + sin(x)**2
f


# La función simplify() de sympy puede reconocer identidades trigonométricas y simplificarlas a la expresión más sencilla aquí unos ejemplos. 

# In[24]:


simplify(f)


# In[25]:


alpha = symbols('alpha')
alpha


# Fórmulas de doble ángulo 

# In[26]:


s = cos(alpha)**2 - sin(alpha)**2
s


# In[27]:


simplify(s)


# Identidades de productos 

# In[28]:


d = sin(alpha)*cos(alpha)
d


# In[29]:


simplify(d)


# Identidades fundamentales 

# In[30]:


t = sin(alpha)/cos(alpha)
t


# In[31]:


simplify(t)


# Logaritmos y exponeciales

# In[32]:


c = (cos(log(a**2))*tan(log(a**2)))
c


# In[33]:


simplify(c)


# Aquí hay una lista de los métodos más útiles (hay más en el módulo sympy.simplify):
# + radsimp (): esto simplifica expresiones con raíces cuadradas
# + trigsimp (): esto simplifica combinaciones de funciones trigonométricas
# + cancel (): Esto elimina los factores comunes entre el numerador y el denominador de una fracción
# + together (): Esto coloca las sumas de una fracción sobre el mismo denominador
# + apart (): esto aplica la descomposición de fracciones parciales
# 
# Aunque hay que aclarar que la función simplify() engloba todas estas, pero en caso de que solo se busque simplificar una en específico se pueden utilizar estas variantes que solo simplificaran la parte de la expresión que les corresponde. 

# Raíz cuadrada

# In[34]:


raiz = 1/(sqrt(5) - 2)
raiz


# In[35]:


radsimp(raiz)


# Identidades trigonometricas

# In[36]:


trigo = (sin(x)**2 + cos(x)**2)
trigo


# In[37]:


trigsimp(trigo)


# Factores comunes

# In[38]:


factor_comun =((x**2 - 1)/(x - 1))
factor_comun


# In[39]:


cancel(factor_comun)


# Suma de fracciones

# In[40]:


sum_frac = (1/(x-1) - 1/(x+1))
sum_frac


# In[41]:


together(sum_frac)


# fracciones parciales

# In[42]:


frac_parciales = (2/(x**2 - 1))
frac_parciales


# In[43]:


apart(frac_parciales)


# Si tenemos alguna expresión que sympy pueda simplificar y usamos el método simplify() va a simplificar todo o que encuentre.
# 
# 

# # Evaluación númerica

# 
# La evaluación numérica sirve para obtener resultados numéricos para las expresiones simbólicas o para las funciones que hemos creado, el método de evaluación numérica nos va a definir la expresión en valores reales numéricos eso quiere decir que deja de ser simbólico el cálculo y la función para evaluar numéricamente es N() que recibe la expresión o función como primer argumento y como segundo recibe las el número de cifras de precisión 
# 
# 

# In[44]:


pi


# In[45]:


N(pi, 100)


# Aquí tenemos una expresión compleja que al correr la celda nos entrega la expresión pero de manera simbólica 

# In[46]:


(exp(pi*sqrt(163)))


# 
# Aquí podemos ver una expresión que como resultado va a dar un numero flotante y para ello podemos agregar a la función N() un segundo argumento que nos de el número de digitos de precisión del resultado 

# In[47]:


N(exp(pi*sqrt(163)), 50)


# In[48]:


len('262537412640768743.99999999999925007259719818568888')


# Aquí comprobamos la longitud de la cifra y nos da 51 pero phyton cuenta el punto como elemento por ello da 51 – 1 = 50 cifras de precisión  

# # Calcúlo con SymPy

# La principal aplicación de SymPy es que puede realizar calculo computacional, anterior mente ya definimos que es el cálculo simbólico, creamos símbolos y funciones además vimos cómo se manipulan y ejecutan. 
# 
# Ahora toca ver como son las funciones que SymPy nos ofrece en el apartado del cálculo matemático y como es que se ejecutan 
# 

# # Derivadas

# Para realizar el cálculo de una derivada de una función tenemos el método diff()  este método recibe de argumento a la función o expresión como primer argumento, el símbolo o variable con respecto a al cual se quiere derivar y como último argumento al número u orden al cual se quiere derivar en caso de no poner este ultimo la función va a entregar la primer derivada. 

# In[49]:


f = Function('f')


# In[50]:


diff(f(x))


# In[51]:


f = x**3 + 3*x**2 + 2*x + 11
f


# In[52]:


diff(f, x)


# Aquí obtenermos la tercera derivada de la función con respecto a 'x'

# In[53]:


diff(f,x,3)


# Cuando se tienen más de una variable en la función solo hay que especificar con respecto a que se quiere derivar, si lo que queremos es derivar con respecto a más de una variable solo introducimos en la función diff() la función seguido de la variable y después el número de veces que se quiere derivar con respecto a esta variable para después introducir la siguiente variable seguido del numero.
# 
# A contiuacion un ejemplo:

# In[54]:


f = x**2 * y**2
f


# In[55]:


diff(f, x, 2, y, 2)


# In[56]:


f = x**4 + sin(y) - x**3*y**2
f


# In[57]:


diff(f, x, 3, y, 1)


# In[58]:


f = exp(x*y*z)
f


# En caso de que solo queramos expresar la derivada sin evaluar tenemos el método Derivative()
# 
# 

# In[59]:


deriv = Derivative(f, x, y, x, z, 4)
deriv


# 
# Para evaluar una derivada no evaluada, use el método .doit()
# 
# 

# In[60]:


deriv.doit()


# # Integrales 

# SymPy tiene potentes algoritmos de integración y, en particular, puede encontrar la mayoría de integrales
# de funciones logarítmicas y exponenciales expresables con funciones especiales, y muchas más
# 
# Para calcular una integral, use la función de integrate(). Hay dos tipos de integrales, definidas e indefinidas. Para calcular una integral indefinida, es decir, una antiderivada o función primitiva, simplemente pase la variable después de la expresión.
# 
# 
# Tenga en cuenta que SymPy no incluye la constante de integración.

# In[61]:


f = cos(x) + (x)
f


# In[62]:


integrate(f)


# En el caso de que la integral sea definida solo tenemos que agregar los límites de integración. Para calcular una integral definida, pase el argumento (variable_integración, límite_inferior, límite_superior). 
# 
# Ejemplo:
# 

# In[63]:


f = 2*sqrt(x -1)
f


# In[64]:


integrate(f,(x, 1, 3))


# In[65]:


f = exp(-x)
f


# In[66]:


integrate(f,(x, 0, oo))


# Las integrales simbólicas y las antiderivadas no evaluadas están representadas por la clase Integral.
# 
# El método Integral() puede devolver estos objetos si no puede calcular la integral, nos devuelve la integral simbólica o no evaluada 

# In[67]:


intg = Integral(sin(x), (x, 0, pi))
intg


# De igual manera que la derivada no evaluada tenemos que para evaluar una integral podemos utilizar el método .doit()
# 
# 

# In[68]:


intg.doit()


# # Límites 

# Los límites de una función en SymPy se obtienen con el método limit() que recibe como argumentos a la función a evaluar, la variable y el valor hacia el cual va a la tendencia del limite
# 
# ejemplo:
# 

# In[69]:


f = (3-x)/(x**2 - 2*x - 8)
f


# In[70]:


limit(f, x, 4)


# In[71]:


f = (x - 9)/(sqrt(x) - 3)
f


# In[72]:


limit(f, x, 6)


# In[73]:


simplify(limit(f, x, 6))


# In[74]:


N(simplify(limit(f, x, 6)),10)


# limites cuanado x tiende a infinito, para definir limites a infinito solo tenemos que colocar a infinito en el tercer argumento que recibe la función y en SymPy el infinito se representa como una doble ‘o’ (oo) y en el caso en donde el valor tienda a menos infinito solo se agrega un – antes (-oo).
# 
#  
# 

# In[75]:


f = (3*x + 1)/(2*x - 3)
f


# In[76]:


limit(f , x , oo)


# In[77]:


f = (1 - exp(x))/(1 + exp(x))
f


# In[78]:


limit(f, x, -oo)


# También hay un cuarto parámetro opcional, para especificar la dirección de aproximación al objetivo límite.
# "+" (el valor predeterminado) da el límite desde arriba y "-" es desde abajo.
# 
# Ejemplo:

# In[79]:


f = 1/x
f


# In[80]:


limit(f, x, 0, "-")


# Al igual que las funciones de cálculo anteriores tenemos para expresar a los limites sin evaluar el método Limit() y para evaluarlo la función .doit().

# In[81]:


f = log(2/x**2)
f


# In[82]:


Limit(f, x, -oo)


# In[83]:


Limit(f, x, -oo).doit()


# # Taylor series 

# Una aproximación de la serie de Taylor es una aproximación de una función obtenida a partir de su serie Taylor. Para calcularlo, use series (expr, x, x0, n), donde x es la variable relevante, x0 es
# el punto donde se realiza la expansión (por defecto es 0), y n es el orden de expansión (por defecto
# a 6)
# 

# In[84]:


series(cos(x), x)


# In[85]:


f = ln(x)
f


# In[86]:


series(f, x, 1, 6)


# El término O al final representa el término de orden de Landau en x = 0,Significa que se omiten todos los términos x con potencia mayor o igual que que se señala(la potencia posterior a O). Los términos del pedido se pueden crear y manipular fuera de la serie. Absorben automáticamente los términos de orden superior.

# In[87]:


f = sqrt(x)
f


# In[88]:


diff(f, x, 5)


# In[89]:


series(f, x, 4, 6)


# # Resolver ecuaciones 

# La función principal que se utiliza para resolver ecuaciones es solve (). Su interfaz es algo
# complicado ya que acepta muchos tipos de entradas diferentes y puede generar resultados en varias formas
# dependiendo de la entrada.
# Para ecuaciones simples en donde igualamos a 0 tenemos la siguiente sintaxis  solve(expresión, variable).
# Esto puede resolver ecuaciones algebraicas
# y ecuaciones trascendentales que involucran fracciones racionales, raíces cuadradas, valores absolutos,
# exponenciales, logaritmos, funciones trigonométricas, etc. El resultado es entonces una lista de
# los valores de las variables que satisfacen la ecuación.
# En es caso de tener una igualdad de expresiones colocar así solve(expr A – expr B, x)
# 
# A continuacion se muestra como

# In[90]:


solve(x**2 - 1, x)


# In[91]:


expr_a = 2*x**2
expr_a


# In[92]:


expr_b = 3*x
expr_b


# In[93]:


solve(expr_a - expr_b, x)


# In[ ]:





# # Algunas funciones creadas con SymPy

# A continuación crearemos un par de funciones implementando los conocimientos que hemos adquirido en el nootebook utilizando el módulo de cálculo de SymPy con el objetivo de  ejemplificar las oportunidades que  SymPy nos ofrece, en donde yo quiero destacar que esto solo es una parte muy resumida y breve de todas la funciones y aplicaciones  que SymPy tiene y que nos permite realizar, ya que con esta paquetería la cantidad de herramientas aplicaciones, funciones,  métodos y uso se extiende más a de algunas funciones y aplicaciones para el cálculo.
# 
# 

# # Graficas de función, derivada y función primitiva

# A continuación se vamos a realizar una función que va a graficar a las funciones y utilizaremos el módulo de graficas que SymPy tiene si quieres saber cómo graficar de manera rápida y sencilla ["Como graficar de manera simple y facíl en SymPy"](https://colab.research.google.com/github/HaydeePeruyero/Geometria-Analitica-1/blob/master/3_1_Graficar_con_Sympy.ipynb).
# Si quieres conocer más acerca del módulo de graficas de SymPy entra al sitio web oficial de ["SymPy plotting"](https://docs.sympy.org/latest/modules/plotting.html)

# In[94]:


def visual_grafic(function, a=-10, b=10):
    '''Esta función recibe a una función matemática y a un intervalo en donde se desea graficar, la función regresa las gráficas de la función, la derivada de la función y la función primitiva o anti-derivada de la función. \n \n visual_grafic(funcion, limite de graficación a, limite de graficación b) '''
    print((function))
    
    dx = diff(function, x) 
    print(dx)
    dx
    integ = (integrate(function, x))
    print(integ)
    
    plot(function, (x, a, b),line_color='cyan', title='Función' )
    plot(dx, (x, a, b), line_color='purple', title='Derivada de la función')
    plot(integ, (x, a, b), line_color='pink', title='Función primitiva')
    


# In[95]:


get_ipython().run_line_magic('pinfo', 'visual_grafic')


# In[96]:


f = x*sin(1/x)
f


# In[105]:


visual_grafic(f, -0.4, 0.4)


# # Calculo de área entre dos funciones

# En esta función vamos a calcular el área que se limita por la curva de dos funciones en donde la función va a recibir 2 argumentos la función o expresión matemática inferior y la función o expresión matemática superior.
# 
# 
# Esta función recibe dos expresiones o funciones creadas en sympy y nos regresa los puntos en donde se intersectan las funciones y el área entre las dos funciones.

# In[98]:


def area_entre_funciones(fi, fs):
    '''Esta función recibe dos expresiones o funciones creadas en sympy y nos regresa los puntos en donde se intersectan las funciones y el área entre las dos funciones '''
    #fis = fi - fs
    #print(fis)
    puntos = solve(fi - fs, x)
    print('Los puntos donde se intersectan las funciones son:', puntos)
    a = puntos[0]
    b = puntos[1]
    
    A = integrate(fi - fs, (x, a, b))
    #print(A)
    #f = A.subs(x, a)
    at = N(simplify(A), 10)
    abs(at)
    #print(at)
    if at > 0:
        print(at)
        #print('el valor llega aqui')
        plot(fi, fs, (x, a-1, b+1), line_color='cyan', title='Área entre funciones')
        
    elif at < 0:
        nat = at*(-1)
        print('El valor de el área señalada es igual a', nat)
        #print('el valor llega aqui')
        plot(fi, fs, (x, a-1, b+1), line_color='cyan', title='Área entre funciones')
        
   
    #at = positive=true 
    #print(at)
    #print(f)
    #g = A.subs(x, b)
    #print(g)
    #plot(fi, fs, (x, a-1, b+1), line_color='cyan', title='Área entre funciones')


# In[99]:


fi = x**2 - 2*x
fs = 12 - x**2


# In[100]:


get_ipython().run_line_magic('pinfo', 'area_entre_funciones')


# In[101]:


area_entre_funciones(fi, fs)


# In[102]:


fi = x**2 - 2*x 
fs = x


# In[103]:


area_entre_funciones(fi, fs)


# Si quieres conocer más acerca de SymPy entra en su página web y ahí podrás encontrar toda la información sobre SymPy y también dentro de su página se encuentra toda la documentación y está dividida y estructurada por temas y subtemas así como sus funciones y aplicaciones.  
# 
# [Pagína web SymPy](https://www.sympy.org/)

# # Bibliografía

# * Ronan Lamy, R. L. (2013). Instant SymPy Starter (1.a ed., Vol. 1). http://www.packtpub.com/. https://www.packtpub.com/big-data-and-business-intelligence/instant-sympy-starter-instant
# 
# 
# * Stewart, J. M. (2014). Python for Scientists (Segunda Edición, Vol. 1). Department of Applied Mathematics & Theoretical Physics University of Cambridge. https://doi.org/10.1017/9781108120241
# 
# 
# * Welcome to SymPy’s documentation! — SymPy 1.7.1 documentation. (s. f.). SymPy. Recuperado 16 de enero de 2021, de https://docs.sympy.org/latest/index.html

# [Volver al inicio](#Introducción-a-SymPy)
