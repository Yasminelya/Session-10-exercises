#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 00:32:24 2018

@author: yasminelyagoubi
"""

#%% Exercise 1

def calculate_volume_cilinder(r,h):
    import math
    return math.pi*(float(r)**2)*float(h)
    
def calculate_volume_sphere(rad):
    import math
    return(float(rad)**3)*math.pi * 4/3
    
#%% Exercise 2
    
import matplotlib.pyplot as plt
import numpy as np

level=["pass","proficiency","excellence","honors"]

plt.bar(level,[15,35,35,15])

print ("the distribution of the class is:")


    