#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 17:52:30 2022

@author: sofia
"""
#%% modules

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import fiona

#%% conf

conf = 'FL_MFL_conf_data/FL_MFL_conf_final.gdb'
c_layers = fiona.listlayers(conf)
print( sorted(c_layers))

conf_3 = 'FL_MFL2_conf_3ft'
conf_h = gpd.read_file(conf,layer=conf_3)

print( len(conf_h) )
print( conf_h.columns )
print( conf_h.crs )


conf_h = conf_h.to_crs(epsg=32617)

dade = gpd.read_file('Florida_TRACTS.zip')
md = dade.query("STCNTY =='12086'")
md = md.to_crs(epsg=32617)
           
#%%          
fig,ax1 = plt.subplots(dpi=300)
md.boundary.plot(color='black',linewidth=0.5,ax=ax1)
conf_h.plot(ax=ax1)
fig.savefig(conf_h+'.png')
ax1.axis('off')