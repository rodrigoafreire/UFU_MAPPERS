import pandas as pd
import geopandas as gpd
from shapely import wkt  
import folium

gdf = gpd.read_file('E:/GitHub/UFU_MAPPERS/microdados/dados/uberlandia_em_func_google.shp')

map_center = (-18.9186, -48.2772)
m = folium.Map(location=map_center, zoom_start=13, control_scale=True, tiles="Cartodb dark_matter")

print(gdf.head(2))

# Loop through each row in the GeoDataFrame and add a marker for each building
for idx, row in gdf.iterrows():
    if not pd.isnull(row['geometry']):
        folium.Marker(location=[row.geometry.y, row.geometry.x], popup=row['NO_ENTIDAD'],
                      icon=folium.Icon(color='blue', icon='school', prefix='fa'), lazy=True).add_to(m)

# Step 8: Save the map as an HTML file or display it in a Jupyter Notebook
m.save('E:/GitHub/UFU_MAPPERS/microdados/dados/building_locations_map_google_3.html')

# The resulting HTML file will contain a map with markers for building locations.

