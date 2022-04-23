import fiona
import geopandas as gpd
import matplotlib.pyplot as plt

source = 'FL_MFL_slr_data_dist/FL_MFL_slr_final_dist.gdb'

layers = fiona.listlayers(source)
print( sorted(layers) )

this_layer = 'FL_MFL1_slr_3ft'
example = gpd.read_file(source,layer=this_layer)

print( len(example) )
print( example.columns )
print( example.crs )


##opens files > writes out layers >> gpkg >> figure out layer (to remedy CRS issues)