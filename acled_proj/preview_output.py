import geopandas as gpd

gdf = gpd.read_file('shapefiles/output.shp')
print(gdf.head(20))

# TODO Fix error below 
# ERROR 4: Unable to open EPSG support file gcs.csv.  
# Try setting the GDAL_DATA environment variable to point to the directory containing EPSG csv files.