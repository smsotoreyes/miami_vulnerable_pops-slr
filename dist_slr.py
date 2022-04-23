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

#%% layers
##uwhats in these geodatabases

dist = 'FL_MFL_slr_data_dist/FL_MFL_slr_final_dist.gdb'

d_layers = fiona.listlayers(dist)
print( sorted(d_layers) )

#%%
dist_3 = 'FL_MFL2_slr_3ft'
dist_h = gpd.read_file(dist,layer=dist_3)

print( len(dist_h) )
print( dist_h.columns )
print( dist_h.crs )


dist_h = dist_h.to_crs(epsg=32617)

dade = gpd.read_file('Florida_TRACTS.zip')
md = dade.query("STCNTY =='12086'")
md = md.to_crs(epsg=32617)
           
#%%          
fig,ax1 = plt.subplots(dpi=300)
md.boundary.plot(color='black',linewidth=0.5,ax=ax1)
dist_h.plot(ax=ax1)
fig.savefig(dist_3+'.png')
ax1.axis('off')







