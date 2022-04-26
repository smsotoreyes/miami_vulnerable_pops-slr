#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 12:08:32 2022

@author: sofia
"""

#%% modules

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

#%% spatial join (slr onto tract)

## reading the files/creating layer
tract = gpd.read_file("miami.gpkg")
tract = tract.to_crs(epsg=32617)
r = 'FL_MFL2_slr_2ft'
water = gpd.read_file('flood_layers.gpkg',layer=r)
water['flood'] = 1
water = water[['flood','geometry']]
water = water.dissolve()

merged = tract.sjoin(water, how="left", predicate="intersects")

merged.to_file("joined.gpkg",layer="slr2",index=False)