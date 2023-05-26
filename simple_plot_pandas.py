#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
simple plot script

"""


import glob, sys


import numpy as np


import pandas as pd


import matplotlib.pyplot as plt

#from scipy.optimize import curve_fit

from pathlib import Path

import pdb

    
    
data_filepath = Path("/media/fabio/X-Bio_Data/X-Bio_documents/Geo_matrix_model/TEOS/CTAB/TEOS_CTAB_01_0W_500mbar_area_data.csv")



dataset = data_filepath.stem



df = pd.read_csv(data_filepath, sep='\t', encoding='utf-8')


xarray = np.array(df['timestamp'])

yarray = np.array(df['area'])

#yarray = np.array(df['pixels_num'])


fig, ax = plt.subplots()



plt.title(str(dataset))
ax.scatter(xarray/1000, yarray)#, label = "meas.") #, 

ax.set_xlabel("time (s)")

ax.set_ylabel(r"area ($mm^2$)")




#plt.legend()

plt.show()
