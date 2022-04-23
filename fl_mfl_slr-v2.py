import fiona
import geopandas as gpd
import matplotlib.pyplot as plt

source = 'FL_MFL_slr_data_dist/FL_MFL_slr_final_dist.gdb'

layers = fiona.listlayers(source)
print( sorted(layers) )

this_layer = 'FL_MFL2_slr_3ft'
example = gpd.read_file(source,layer=this_layer)

print( len(example) )
print( example.columns )
print( example.crs )

example = example.to_crs(epsg=32617)

counties = gpd.read_file('cb_2019_us_county_500k.zip')
md = counties.query('GEOID == "12086"')
md = md.to_crs(epsg=32617)
           
#%%          
fig,ax1 = plt.subplots(dpi=300)
md.boundary.plot(color='black',linewidth=0.5,ax=ax1)
example.plot(ax=ax1)
fig.savefig(this_layer+'.png')
ax1.axis('off')
