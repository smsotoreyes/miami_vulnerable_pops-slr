#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 21:18:12 2022

@author: sofia
"""
#%% modules

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import fiona


#%% dade


dist = 'FL_MFL_slr_data_dist/FL_MFL_slr_final_dist.gdb'

d_layers = fiona.listlayers(dist)
print( sorted(d_layers) )

slr_list = ['FL_MFL1_low_0ft', 'FL_MFL1_low_10ft', 'FL_MFL1_low_1ft',
             'FL_MFL1_low_2ft', 'FL_MFL1_low_3ft', 'FL_MFL1_low_4ft', 
             'FL_MFL1_low_5ft', 'FL_MFL1_low_6ft', 'FL_MFL1_low_7ft', 
             'FL_MFL1_low_8ft', 'FL_MFL1_low_9ft', 'FL_MFL1_slr_0ft', 
             'FL_MFL1_slr_10ft', 'FL_MFL1_slr_1ft', 'FL_MFL1_slr_2ft', 
             'FL_MFL1_slr_3ft', 'FL_MFL1_slr_4ft', 'FL_MFL1_slr_5ft', 
             'FL_MFL1_slr_6ft', 'FL_MFL1_slr_7ft', 'FL_MFL1_slr_8ft', 
             'FL_MFL1_slr_9ft', 'FL_MFL2_low_0ft', 'FL_MFL2_low_10ft', 
             'FL_MFL2_low_1ft', 'FL_MFL2_low_2ft', 'FL_MFL2_low_3ft', 
             'FL_MFL2_low_4ft', 'FL_MFL2_low_5ft', 'FL_MFL2_low_6ft', 
             'FL_MFL2_low_7ft', 'FL_MFL2_low_8ft', 'FL_MFL2_low_9ft', 
             'FL_MFL2_slr_0ft', 'FL_MFL2_slr_10ft', 'FL_MFL2_slr_1ft', 
             'FL_MFL2_slr_2ft', 'FL_MFL2_slr_3ft', 'FL_MFL2_slr_4ft', 
             'FL_MFL2_slr_5ft', 'FL_MFL2_slr_6ft', 'FL_MFL2_slr_7ft', 
             'FL_MFL2_slr_8ft', 'FL_MFL2_slr_9ft']

#%% flood layers >> pull out layers

runs = ['FL_MFL2_low_2ft', 'FL_MFL2_slr_2ft',
        'FL_MFL2_low_4ft', 'FL_MFL2_slr_4ft',
        'FL_MFL2_low_6ft', 'FL_MFL2_slr_6ft']

for r in runs:
    scenario = gpd.read_file(dist, layer=r)
    scenario = scenario.to_crs(epsg=32617)
    scenario.to_file('flood_layers.gpkg', layer=r, index=False)
    

