
# %%
## WİTHOUT İTERATİON
from numpy import *

n = int(input("Order: "))

def Legendre(n,x):
    x=array(x)
    if (n==0):
        return x*0+1.0
    elif (n==1):
        return x
    else:
        return ((2.0*n-1.0)*x*Legendre(n-1,x)-(n-1)*Legendre(n-2,x))/n
 
def DLegendre(n,x):
    x=array(x)
    if (n==0):
        return x*0
    elif (n==1):
        return x*0+1.0
    else:
        return (n/(x**2-1.0))*(x*Legendre(n,x)-Legendre(n-1,x))

roots=[]
weight=[]

for i in range(1,(n+1)):
    x=cos(pi*(i-0.25)/(n+0.5))
    #print(x)
    roots.append(x)
    
    w = ((2)/((1-x*x)*(DLegendre(n,x)**2)))
    weight.append(w)

print("Xi: ",roots)
print("Weights: ",weight)

##############################################################################################

# %%
# WİTH İTERATİON
from numpy import *

n = int(input("Order: "))

def Legendre(n,x):
    x=array(x)
    if (n==0):
        return x*0+1.0
    elif (n==1):
        return x
    else:
        return ((2.0*n-1.0)*x*Legendre(n-1,x)-(n-1)*Legendre(n-2,x))/n
 

def DLegendre(n,x):
    x=array(x)
    if (n==0):
        return x*0
    elif (n==1):
        return x*0+1.0
    else:
        return (n/(x**2-1.0))*(x*Legendre(n,x)-Legendre(n-1,x))

roots1=[]
weights1 = []

for i in range(1,(n+1)):
    x=cos(pi*(i-0.25)/(n+0.5))
    #print(x)
    tollerans = 1e-20
    #hata = 10*tollerans
    iterasyon = 0
    while iterasyon<4:
        x=x -Legendre(n,x)/DLegendre(n,x)
        iterasyon=iterasyon+1
        #hata=abs(-Legendre(n,x)/DLegendre(n,x))
        #print(x)
    
    roots1.append(x)

    w = ((2)/((1-x*x)*(DLegendre(n,x)**2)))
    weights1.append(w)



print("Xi: ",roots1)
print("Weights: ",weights1)
#########################################################################################

# %%
# WİTH İTERATİON
from numpy import *

n = int(input("Order: "))

def Legendre(n,x):
    x=array(x)
    if (n==0):
        return x*0+1.0
    elif (n==1):
        return x
    else:
        return ((2.0*n-1.0)*x*Legendre(n-1,x)-(n-1)*Legendre(n-2,x))/n
 

def DLegendre(n,x):
    x=array(x)
    if (n==0):
        return x*0
    elif (n==1):
        return x*0+1.0
    else:
        return (n/(x**2-1.0))*(x*Legendre(n,x)-Legendre(n-1,x))

roots2=[]
weights2 = []

for i in range(1,(n+1)):
    x=cos(pi*(i-0.25)/(n+0.5))
    iterasyon = 0
    while iterasyon<4:
        x=x -Legendre(n,x)/DLegendre(n,x)
        iterasyon=iterasyon+1
    roots2.append(x)
    w = ((2)/((1-x*x)*(DLegendre(n,x)**2)))
    weights2.append(w)

print("Xi: ",roots2)
print("Weights: ",weights2)

# %%
