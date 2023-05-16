#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
simple script for plotting loss functions from a PyTorch checkpoint dictionary
"""
import os

import numpy as np 

#import pandas as pd

import matplotlib.pyplot as plt

#import matplotlib.gridspec as gridspec

from pathlib import Path
import pdb

import torch



checkpt_path = Path("/home/fabio/Documents/X-Bio/lab/HED_UNet_benchmarking/python_code_HED_UNet/logs/2023-04-28_12-12-20/checkpoints/320.pt")


if torch.cuda.is_available():
    checkpt = torch.load(checkpt_path)

else:
    checkpt = torch.load(checkpt_path, map_location=torch.device('cpu'))

epc = checkpt['epoch']

loss = checkpt['loss']

val_loss = checkpt['val_loss']



loss_list = [x.item() for x in loss] 

#loss_list = [x.detach().numpy() for x in loss] #alternative

val_loss_list = [x.item() for x in val_loss]

#pdb.set_trace()




fig, ax = plt.subplots()

#nameplot = data_path.stem + " - right"

#plt.title(nameplot)
#plt.title("right angle")

plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

plt.xlabel('epoch', size = "20")
plt.ylabel('loss', size = "20")
ax.plot(loss_list, color="blue", label = 'train', linewidth=2)  #loss_list[1:]
ax.plot(val_loss_list, color="red", label = 'valid', linewidth=2) # val_loss_list[1:]

plt.xlim([0, 320])

#save_path = data_path.parent.absolute() / nameplot 
#plt.savefig(save_path)

plt.legend(fontsize=18)

plt.show()


