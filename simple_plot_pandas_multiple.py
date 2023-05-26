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


path_folder = Path("/home/fabio/Documents/X-Bio/lab/Geo_matrix_model/report_may_2023/area_data_files")

files_list = path_folder.glob("*.csv")
    
plot_folder_path = Path("/home/fabio/Documents/X-Bio/lab/Geo_matrix_model/report_may_2023/area_time_plots")


for data_filepath in files_list:

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

    #plt.show()
    
    figurepath = plot_folder_path / Path(dataset + ".png")
    
    plt.savefig(figurepath, bbox_inches='tight')
    
    plt.close()
