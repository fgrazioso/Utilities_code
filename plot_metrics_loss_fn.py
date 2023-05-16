#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
simple script for plotting loss functions from a pytorch metrics log file
"""

import numpy as np

from pathlib import Path

import matplotlib.pyplot as plt



data_path = Path("/home/fabio/Documents/X-Bio/lab/HED_UNet_benchmarking/python_code_HED_UNet/logs/2023-04-28_12-12-20/metrics.txt")

ep_array1 = []   # epoch train

ep_array2 = []         # epoch validation

loss = []           #  train loss
val = []     # validation loss


with open(data_path) as datafile:
    for line in datafile:
        """
        line structure:
        Epoch 01 - Train: Loss: 0.090, SegAcc: 0.997, EdgeAcc: 0.900
        Epoch 01 - Val: Loss: 0.003, SegAcc: 1.000, EdgeAcc: 0.890
        """
        
        
        epstr, rest = line.split("-")
        
        epstr = epstr.strip()
        rest = rest.strip(' \n')
        
        
        dummy, epoch = epstr.split(" ")
        
        epoch = int(epoch)
        
        
        payload, dummy, dummy = rest.split(",")
        
        tag, dummy, value = payload.split(":")
        
        tag = tag.strip()
        value = float(value.strip())
        
        
        
        if tag == "Train":
            
            ep_array1.append(epoch)
            loss.append(value)
            
        elif tag == "Val":
            
            ep_array2.append(epoch)
            val.append(value)
            
        else: print("error!")
            
            
            
            
fig, ax = plt.subplots()

plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

plt.xlabel('epoch', size = "20")
plt.ylabel('loss', size = "20")

ax.plot(ep_array1, loss, label = "train")
ax.plot(ep_array2, val, label = "valid")
    

plt.legend(fontsize=18)

plt.show()
