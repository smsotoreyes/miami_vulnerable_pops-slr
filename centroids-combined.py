"""
centroids-combined.py
May 2022 PJW
Build a combined file with flooded centroids from different scenarios.
"""

import geopandas as gpd
import os
import fiona
import matplotlib.pyplot as plt

in_file = 'joined.gpkg'
out_file = 'centroids-combined.gpkg'

if os.path.exists(out_file):
    os.remove(out_file)

#%%
#
#  Read each layer and build a combined set of information
#

layers = fiona.listlayers(in_file)

first = True
for r in layers:
    print(r,flush=True)
    this_layer = gpd.read_file(in_file,layer=r)
    print('\n'+r+', centroids=',len(this_layer))
    this_layer = this_layer[[r,'geometry']]
    if first:
        combined = this_layer
        first = False
    else:
        combined = combined.overlay(this_layer,how='union')

combined[layers] = combined[layers].fillna(0)
combined[layers] = combined[layers].astype(int)

print( combined[layers].sum() )

#%%
#
#  Add combined counts by scenario
#

depths = ['2','4','6']

for d in depths:
    low = f'FL_MFL2_low_{d}ft'
    slr = f'FL_MFL2_slr_{d}ft'
    combined[f'both_{d}ft'] = combined[low] | combined[slr]

#
#  Save the result
#

combined.to_file(out_file,layer='combined',index=False)

#%%
#
#  Draw some individual maps
#

for r in layers:
    fig,ax1 = plt.subplots(dpi=300)
    fig.suptitle(r)
    combined.plot(r,markersize=10,legend=True,ax=ax1)
    ax1.axis('off')
    fig.tight_layout()
    fig.savefig(f'centroids-{r}.png')

#%%
#
#  Draw combined maps
#

for d in depths:
    fig,ax1 = plt.subplots(dpi=300)
    fig.suptitle(f'SLR and low, {d}ft')
    combined.plot(f'both_{d}ft',markersize=10,legend=True,ax=ax1)
    ax1.axis('off')
    fig.tight_layout()
    fig.savefig(f'centroids-both_{d}.png')
