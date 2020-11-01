#!/usr/bin/env python
# coding: utf-8

# In[1]:


from OCFit import OCFit, FitLinear
import numpy as np
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#Učitavanje podataka
OC_=pd.read_csv('./AD_And_OC.csv', header = None, names = ['d', 'c'])
oc = np.array((OC_['c']))
E = np.array(OC_['d'])
#plt.scatter(E,oc)
#plt.show()


# In[4]:


#Učitavanje podataka za sistem i greške
import numpy as np
P = 0.98
t0 = 51000
err = 0.002*np.ones(E.shape)


# In[5]:


#Računanje perioda
from astropy.timeseries import LombScargle
frequency, power = LombScargle(E, oc).autopower()
p=(1/frequency[np.argmax(power)]) 
p2=p+500
p1=p-500


# In[6]:


#Traženje predpostavljene vrednosti za t0
Emax=E[np.argmax(oc)]
t01 = Emax - 500
t02 = Emax + 500


# In[7]:


from OCFit import OCFit, FitLinear

#initialization of class OCFit and O-C calculated using FitLinear
fit=OCFit(E,oc,err = err)
fit.Epoch(t0,P)  #calculating epochs

#setting the model and parameters for fitting
fit.model='LiTE3'
fit.fit_params=['a_sin_i3', 'e3', 'w3', 't03', 'P3']
fit.limits={'a_sin_i3': [3, 3.5], 'e3': [0, 1], 'w3': [0,2*np.pi],
            't03': [t01, t02], 'P3': [p1, p2]}
fit.steps={'a_sin_i3': 1e-4, 'e3': 1e-3, 'w3': 1e-3, 't03': 10, 'P3': 10}

#fitting using GA without displaying fitting progress
fit.FitGA(100,100,visible=True)
#sumarry of results after GA
fit.Summary()

#fitting using MCMC without displaying fitting progress
fit.FitMCMC(1e3,visible=False)
#sumarry of results after MC
fit.Summary()

#plotting figure
#figure with original O-C with fit without transformation of x axis
#together with residue and 2nd axis in epochs
fit.Plot(trans = False,with_res=True,double_ax=True)

