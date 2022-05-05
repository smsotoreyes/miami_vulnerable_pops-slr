#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 10:08:07 2022

@author: sofia
"""

#%% other columns commented out

## 'E_TOTPOP', 'M_TOTPOP', 'E_HU', 'M_HU', 'E_HH', 'M_HH', 'E_POV', 
##'M_POV', 'E_UNEMP', 'M_UNEMP', 'E_PCI', 'M_PCI', 'E_NOHSDP', 
##'M_NOHSDP', 'E_AGE65', 'M_AGE65', 'E_AGE17', 'M_AGE17', 
##'E_DISABL', 'M_DISABL', 'E_SNGPNT', 'M_SNGPNT', 
## 'E_MINRTY', 'M_MINRTY', 'E_LIMENG', 'M_LIMENG', 'E_MUNIT', 
##'M_MUNIT', 'E_MOBILE', 'M_MOBILE', 'E_CROWD', 'M_CROWD', 'E_NOVEH', 
## 'M_NOVEH', 'E_GROUPQ', 'M_GROUPQ', 'EP_POV', 'MP_POV', 'EP_UNEMP', 
##'MP_UNEMP', 'EP_PCI', 'MP_PCI', 'EP_NOHSDP', 'MP_NOHSDP', 'EP_AGE65', 
##'MP_AGE65', 'EP_AGE17', 'MP_AGE17', 'EP_DISABL', 'MP_DISABL', 
## 'EP_SNGPNT', 'MP_SNGPNT', 'EP_MINRTY', 'MP_MINRTY', 'EP_LIMENG',
## 'MP_LIMENG', 'EP_MUNIT', 'MP_MUNIT', 'EP_MOBILE', 'MP_MOBILE', 
## 'EP_CROWD', 'MP_CROWD', 'EP_NOVEH', 'MP_NOVEH', 'EP_GROUPQ', 
## 'MP_GROUPQ', 'EPL_POV', 'EPL_UNEMP', 'EPL_PCI', 'EPL_NOHSDP', 
## 'SPL_THEME1', 'RPL_THEME1', 'EPL_AGE65', 'EPL_AGE17', 'EPL_DISABL', 
## 'EPL_SNGPNT', 'SPL_THEME2', 'RPL_THEME2', 'EPL_MINRTY', 'EPL_LIMENG', 
## 'SPL_THEME3', 'RPL_THEME3', 'EPL_MUNIT', 'EPL_MOBILE', 'EPL_CROWD', 
## 'EPL_NOVEH', 'EPL_GROUPQ', 'SPL_THEME4', 'RPL_THEME4', 'SPL_THEMES', 
## 'RPL_THEMES',

#%% old slr join

# for s in slr_list:
#     if not s.startswith('FL_MFL2_'):
#         continue
#     scenarios = gpd.read_file(dist,layer=s)
#     print( len(scenarios) )
#     print( scenarios.columns )
#     print( scenarios.crs )
      
          
#     scenarios = scenarios.to_crs(epsg=32617)
    
#     tracts = gpd.read_file('Florida_TRACTS.zip')
#     md = tracts.query("STCNTY =='12086'")
#     md = md.to_crs(epsg=32617)
        
# fig,ax1 = plt.subplots(dpi=300)
# scenarios.plot(ax=ax1)
# fig.savefig(f"{s}.png")
# ax1.axis('off')

# scenarios.to_file("slr_scenarios.gpkg", layer = 'scenarios', index=False)

#%% centroids

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import os

tracts = gpd.read_file("joined.gpkg",layer="slr2")

centroids = tracts.copy()
centroids['geometry'] = tracts.centroid
centroids = centroids.dropna(subset=["flood"])
centroids.to_file("joined.gpkg",layer='centroids_slr2',index=False)


