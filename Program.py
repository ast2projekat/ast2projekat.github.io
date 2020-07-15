# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 00:09:13 2020

@author: milos
"""
##################
import pandas as pd             
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
##################

##################
Podaci1 = pd.read_csv("C:\\Users\\milos\\Desktop\\Podaci\\VW_Cep_2.csv", header = None, names = ['a', 'b'])

x = Podaci1['a']
y = Podaci1['b']
##################

#interpolacija podataka 
n=400
m=2458125.54645
l=2458125.44031
xvals=np.linspace(m,l,n)

#Linearna interpolacija
f1 = interpolate.interp1d(x, y,kind='linear',fill_value='extrapolate')
yinterp = f1(xvals) 

#Kvadratna interpolacija 
#f2 = interpolate.interp1d(x, y,kind='quadratic',fill_value='extrapolate')
#yinterp = f2(xvals)   

#Gledamo koji je element u nizu je ymin i tražimo njegovu x koordinatu
ymin=max(yinterp)
ymin=np.where(yinterp == ymin)
xmin1=(xvals[ymin])
print('Pretpostavljeni minimum je: ', xmin1)
print('ymin je', ymin)

#Zadajemo početne vrednosti za for petlju
ymin1 = 186
 #Broj člana u nizu gde se nalazi ymin
S1 = 0    
S2 = 0
S3 = 0
t = 1
Tv = 2  #Delta T (pomeramo se za 20 članova niza levo i desno)

for i in range(1,5):
    S1=((yinterp[ymin1 + t*i]) + (yinterp[ymin1 - t*i]) + S1)
    S2=((yinterp[ymin1 + Tv + t*i]) + (yinterp[ymin1 - Tv - t*i]) + S2)
    S3=((yinterp[ymin1 - Tv + t*i]) + (yinterp[ymin1 + Tv - t*i]) + S3)
print('S1=',S1,'S2=',S2,'S3=',S3) 

Td=(l-m)/n*Tv 
#Računamo minimum
xmin = xmin1 + (1/2*(S3-S2)/(S3-2*S1+S2)*Td)
print('Trenutak minimuma je: ', xmin)

##############
ymiin=min(yinterp)
ymaax=max(yinterp)
xmin111=[xmin,xmin]
ymin111=[ymiin,ymaax]
##############

plt.plot(x,y,'o')
plt.plot(xvals,f1(xvals))
plt.legend(['podaci', 'linearna interpolacija'], loc='best')
#plt.plot(xvals,f2(xvals))
#plt.legend(['podaci', 'kvadratna interpolacija'], loc='best')
plt.gca().invert_yaxis()
plt.plot(xmin111,ymin111,'r')
plt.show()
