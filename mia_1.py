#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 12:25:34 2022

@author: sofia
"""
#%% modules

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
#%% gpkg tracts
raw = gpd.read_file("Florida_TRACTS.zip")
miami = raw.query("STCNTY =='12086'")
miami.to_file("miami.gpkg", layer = 'tracts', index=False)
print("\nColumns:", list(miami.columns))
#%%
var_list = ['E_TOTPOP', 'M_TOTPOP', 'E_HU', 'M_HU', 'E_HH', 'M_HH', 'E_POV', 
            'M_POV', 'E_UNEMP', 'M_UNEMP', 'E_PCI', 'M_PCI', 'E_NOHSDP', 
            'M_NOHSDP', 'E_AGE65', 'M_AGE65', 'E_AGE17', 'M_AGE17', 
            'E_DISABL', 'M_DISABL', 'E_SNGPNT', 'M_SNGPNT', 
            'E_MINRTY', 'M_MINRTY', 'E_LIMENG', 'M_LIMENG', 'E_MUNIT', 
            'M_MUNIT', 'E_MOBILE', 'M_MOBILE', 'E_CROWD', 'M_CROWD', 'E_NOVEH', 
            'M_NOVEH', 'E_GROUPQ', 'M_GROUPQ', 'EP_POV', 'MP_POV', 'EP_UNEMP', 
            'MP_UNEMP', 'EP_PCI', 'MP_PCI', 'EP_NOHSDP', 'MP_NOHSDP', 'EP_AGE65', 
            'MP_AGE65', 'EP_AGE17', 'MP_AGE17', 'EP_DISABL', 'MP_DISABL', 
            'EP_SNGPNT', 'MP_SNGPNT', 'EP_MINRTY', 'MP_MINRTY', 'EP_LIMENG',
            'MP_LIMENG', 'EP_MUNIT', 'MP_MUNIT', 'EP_MOBILE', 'MP_MOBILE', 
            'EP_CROWD', 'MP_CROWD', 'EP_NOVEH', 'MP_NOVEH', 'EP_GROUPQ', 
            'MP_GROUPQ', 'EPL_POV', 'EPL_UNEMP', 'EPL_PCI', 'EPL_NOHSDP', 
            'SPL_THEME1', 'RPL_THEME1', 'EPL_AGE65', 'EPL_AGE17', 'EPL_DISABL', 
            'EPL_SNGPNT', 'SPL_THEME2', 'RPL_THEME2', 'EPL_MINRTY', 'EPL_LIMENG', 
            'SPL_THEME3', 'RPL_THEME3', 'EPL_MUNIT', 'EPL_MOBILE', 'EPL_CROWD', 
            'EPL_NOVEH', 'EPL_GROUPQ', 'SPL_THEME4', 'RPL_THEME4', 'SPL_THEMES', 
            'RPL_THEMES', 'F_POV', 'F_UNEMP', 'F_PCI', 'F_NOHSDP', 'F_THEME1', 
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
    

#%% cool graph

limeng = miami[['E_LIMENG','M_LIMENG']]
limeng['est']=limeng['E_LIMENG']
limeng['low']=limeng['est']-limeng['M_LIMENG']
limeng['high']=limeng['est']+limeng['M_LIMENG']
limeng = limeng.sort_values('est')
limeng = limeng.reset_index()
limeng[['est','low','high']].plot.line()



