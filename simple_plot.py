#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
simple plot script

"""


import os, glob, sys


import numpy as np

import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

import pdb




def gauss_fn(x, *param):
    """
    y =    1/(sig √2 )   e^[ 1/2  ( x - mu )/ sig ]^2 
    """
    mu, sig = param
    return   ( 1 /(sig * np.sqrt(2 * np.pi ))) *\
                            np.exp(-0.5 * ((x - mu) / sig)**2  )  
    
    # 


data_filepath = "/media/fabio/X-Bio_Data/X-Bio_documents/Leaves_wetting/Листья Огурец Растекание/9-10 молодые листья/test_out/meas_data.csv"


dataset, dummy = os.path.splitext(os.path.basename(data_filepath))

time, area = np.loadtxt(data_filepath, skiprows=1, delimiter="\t", unpack=True)#, usecols = [0, 1, 2] , delimiter="\t")


numero_dati_up = len(time)
numero_dati_down = len(area)


#fig, ax = plt.subplots()
#ax.plot(up_angle, color = "red")
#ax.plot(down_angle, color = "blue")


#print("up_angle = ", up_angle)
#print("down_angle = ", down_angle)
#pdb.set_trace()


#guessparamup = [35, 2]

#guessparamdwn = [35, 3]

#histo_up, edg_histo_up = np.histogram(up_angle, bins = 8, density = True)

#histo_down, edg_histo_down = np.histogram(down_angle, bins = 8, density = True)



#print("histo_up = ", histo_up)
#print("histo_down = ", histo_down)



#fit_param, dummy = curve_fit(gauss_fn, edg_histo_up[:-1], histo_up, 
                             #p0 = guessparamup)


# pdb.set_trace()

fig, ax = plt.subplots()


#plt.title(dataset + " top" )
ax.scatter(time, area)#, label = "meas.") #, 

ax.set_xlabel("time (ms)")

ax.set_ylabel(r"area ($cm^2$)")


#xarray = np.linspace(edg_histo_up[0], edg_histo_up[-1], 1000)

#ax.plot(xarray, gauss_fn(xarray, *guessparamup), 
#                            label = "guess", color = "green")



#ax.plot(xarray, gauss_fn(xarray, *fit_param), 
#                            label = "gauss", color = "red")

#annotation_str = "$\mu$ = {0:.2f}\n$\sigma$ = {1:.2f}\ntot. data = {2}"\
    #.format(fit_param[0], fit_param[1], numero_dati_up)

#plt.annotate(annotation_str, xy=(0.03, 0.8),
#                                                xycoords='axes fraction')

#plt.legend()


#fig, ax = plt.subplots()

#plt.title(dataset + ' bottom')


#ax.scatter(edg_histo_down[:-1], histo_down, label = "meas.")

#xarray = np.linspace(edg_histo_down[0], edg_histo_down[-1], 1000)
#ax.plot(xarray, gauss_fn(xarray, *guessparamdwn), 
                           #label = "guess", color = "green")

#fit_param, dummy = curve_fit(gauss_fn, edg_histo_down[:-1], histo_down, 
                             #p0 = guessparamdwn)

#ax.plot(xarray, gauss_fn(xarray, *fit_param), 
                            #label = "gauss", color = "red")


#annotation_str = "$\mu$ = {0:.2f}\n$\sigma$ = {1:.2f}\ntot. data = {2}"\
    #.format(fit_param[0], fit_param[1], numero_dati_down)

#plt.annotate(annotation_str, xy=(0.03, 0.8),
                                                #xycoords='axes fraction')

#plt.legend()

plt.show()
