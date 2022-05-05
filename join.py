#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 12:08:32 2022

@author: sofia
"""

## this script takes 10 minutes to run

#%% modules

import geopandas as gpd
import os
import fiona

out_file = "joined.gpkg"

#%% spatial join (slr onto tract)

## reading the files/creating layer

tract = gpd.read_file("miami.gpkg")
tract = tract.to_crs(epsg=32617)

#%%
if os.path.exists(out_file):
    os.remove(out_file)

layers = fiona.listlayers('flood_layers.gpkg')
for r in layers:
    print(r,flush=True)
    water = gpd.read_file('flood_layers.gpkg',layer=r)
    water[r] = 1
    water = water[[r,'geometry']]
    merged = tract.sjoin(water, how="inner", predicate="intersects")
    merged = merged.drop(columns="index_right")
    merged = merged.drop_duplicates()
    merged['geometry'] = merged['geometry'].centroid
    merged.to_file(out_file, layer=r, index=False)
    
    
    


