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

#%% cool graph

limeng = miami[['E_LIMENG','M_LIMENG']]
limeng['est']=limeng['E_LIMENG']
limeng['low']=limeng['est']-limeng['M_LIMENG']
limeng['high']=limeng['est']+limeng['M_LIMENG']
limeng = limeng.sort_values('est')
limeng = limeng.reset_index()
limeng[['est','low','high']].plot.line()



