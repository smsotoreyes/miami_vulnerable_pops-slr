#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 18:42:48 2022

@author: sofia
"""

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

#%% gpkg tracts
raw = gpd.read_file("Florida_TRACTS.zip")
miami = raw.query("STCNTY =='12086'")
miami.to_file("miami.gpkg", layer = 'tracts', index=False)
print("\nColumns:", list(miami.columns))

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



#%% 


limeng = miami[['E_LIMENG','M_LIMENG']]
limeng['est']=limeng['E_LIMENG']
limeng['low']=limeng['est']-limeng['M_LIMENG']
limeng['high']=limeng['est']+limeng['M_LIMENG']
limeng = limeng.sort_values('est')
limeng = limeng.reset_index()
limeng[['est','low','high']].plot.line()

#%%

for v in var_list:
    if not v.startswith("F_"):
        continue
    flags = miami

