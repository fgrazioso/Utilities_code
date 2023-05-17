#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
simple plot script

"""


import glob, sys


import numpy as np


import pandas as pd


import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

from pathlib import Path

import pdb

    
    
data_filepath1 = Path("/media/fabio/X-Bio_Data/X-Bio_documents/Geo_matrix_model/TEOS/2023-03-15_18-17-08_frames/2023-03-15_18-17-08_frames_area_data.csv")


data_filepath2 = Path("/media/fabio/X-Bio_Data/X-Bio_documents/Geo_matrix_model/TEOS/2023-03-15_18-57-49_frames/2023-03-15_18-57-49_frames_area_data.csv")

data_filepath2_1 = Path("/media/fabio/X-Bio_Data/X-Bio_documents/Geo_matrix_model/TEOS/2023-03-15_18-57-49_frames_1_sec/2023-03-15_18-57-49_frames_area_data.csv")


data_filepath3 = Path("/media/fabio/X-Bio_Data/X-Bio_documents/Geo_matrix_model/TEOS/2023-03-16_17-56-25_frames/2023-03-16_17-56-25_frames_area_data.csv")


data_filepath4 = Path("/media/fabio/X-Bio_Data/X-Bio_documents/Geo_matrix_model/TEOS/2023-03-16_18-25-09_frames/2023-03-16_18-25-09_frames_area_data.csv")

data_filepath5 = Path("/media/fabio/X-Bio_Data/X-Bio_documents/Geo_matrix_model/TEOS/2023-03-17_17-22-41_frames/2023-03-17_17-22-41_frames_area_data.csv")


data_filepath6 = Path("/media/fabio/X-Bio_Data/X-Bio_documents/Geo_matrix_model/TEOS/2023-03-17_18-08-18_frames/2023-03-17_18-08-18_frames_area_data.csv")

data_filepath = data_filepath2


dataset = data_filepath.stem



df = pd.read_csv(data_filepath, sep='\t', encoding='utf-8')


xarray = np.array(df['timestamp'])

yarray = np.array(df['area'])

#yarray = np.array(df['pixels_num'])


fig, ax = plt.subplots()



plt.title(dataset  )
ax.scatter(xarray, yarray)#, label = "meas.") #, 

ax.set_xlabel("time (ms)")

ax.set_ylabel(r"area ($mm^2$)")




#plt.legend()

plt.show()
