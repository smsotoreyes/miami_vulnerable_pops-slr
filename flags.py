#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 18:42:48 2022

@author: sofia
Build a customized vulnerability index layer 
"""

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import os

#%% gpkg tracts
## understanding columns in SVI index

raw = gpd.read_file("Florida_TRACTS.zip")
miami = raw.query("STCNTY =='12086'")
print("\nColumns:", list(miami.columns))

out_file = "miami.gpkg"

#%% SVI layers

## selecting flag layers for further analysis determined by relevance for MDC


var_list = ['F_POV', 'F_UNEMP', 'F_PCI', 'F_NOHSDP', 'F_THEME1', 
            'F_AGE65', 'F_AGE17', 'F_DISABL', 'F_SNGPNT', 'F_THEME2', 'F_MINRTY', 
            'F_LIMENG', 'F_THEME3', 'F_MUNIT', 'F_MOBILE', 'F_CROWD', 'F_NOVEH', 
            'F_GROUPQ', 'F_THEME4', 'F_TOTAL', 'E_UNINSUR', 'M_UNINSUR', 
            'EP_UNINSUR', 'MP_UNINSUR', 'E_DAYPOP',]
miami = miami.replace(-999, None)

for v in var_list:
    if not v.startswith("F_"):
        continue
    fig, ax1 = plt.subplots(dpi=300)
    miami.plot(v, 
               legend = True,
               legend_kwds = {"loc":3},
               cmap="RdYlBu_r",
               ax = ax1)
    ax1.axis("off")
    fig.suptitle(v)
    fig.tight_layout()
    fig.savefig(f"{v}.png")
    
#%% flag prefs

## creating geopackage layer of chosen vulnerability indicators (eliminated high occupancy buildings (multiunit)
## and limited english (limeng)

if os.path.exists(out_file):
    os.remove(out_file)

flag_list = ['F_THEME1',
             'F_THEME2',
             'F_MINRTY',
             'F_MOBILE','F_CROWD','F_NOVEH','F_GROUPQ']

miami['flag_pref'] = miami[flag_list].sum(axis='columns')
miami.to_file("miami.gpkg", layer = 'tracts', index=False)







