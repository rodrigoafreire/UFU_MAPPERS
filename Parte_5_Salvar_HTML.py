import pandas as pd
import geopandas as gpd
import folium

# Carregar o GeoDataFrame já salvo em SHP
gdf = gpd.read_file('E:/GitHub/UFU_MAPPERS/microdados/SHP/UDI_em_funcionamento_publicas.shp')

# Step 7: Create a map using Folium and add markers for building locations
# Replace 'latitude' and 'longitude' with your desired map center coordinates
# No caso de Uberlandia, as coordenadas são: -18.9186, -48.2772
map_center = (-18.9186, -48.2772)
m = folium.Map(location=map_center, zoom_start=13)

print(gdf.head(40))

# Step 1: Determine the number of subsets and calculate the approximate size of each subset
num_subsets = 7
subset_size = len(gdf) // num_subsets
remaining_locations = len(gdf) % num_subsets

# Step 2: Define unique colors for each subset
colors = ['red', 'blue', 'green', 'orange', 'purple', 'pink', 'cadetblue']  # Add more colors as needed

# Atribuir as cores para os mapeadores
Atrs = ['Rodrigo', 'Mauricio', 'Bento', 'Deborah', 'Iago', 'Maria Cecilia', 'Renato']

start_idx = 0

for i in range(num_subsets):
    subset_end = start_idx + subset_size
    if i < remaining_locations:
        subset_end += 1

    subset = gdf[start_idx:subset_end]
    color = colors[i]
    Atr = Atrs[i]
    subset.to_file('E:/GitHub/UFU_MAPPERS/microdados/SHP/UDI_em_funcionamento_publicas_' + str(i) + '_'+ Atr + '.shp', driver='ESRI Shapefile')

    for idx, row in subset.iterrows():
        if not pd.isnull(row['geometry']):
            location = [row.geometry.y, row.geometry.x]
            popup_text = row['NO_ENTIDAD'] + '---' + Atr
        
            marker = folium.Marker(
                location=location,
                popup=popup_text,
                icon=folium.Icon(color=color, icon='school', prefix='fa')
            )
            marker.add_to(m)

    start_idx = subset_end
    m.save('E:/GitHub/UFU_MAPPERS/microdados/dados/Escolas_Publicas_'+ Atr + '.html')

# Step 8: Save the map as an HTML file or display it in a Jupyter Notebook
m.save('E:/GitHub/UFU_MAPPERS/microdados/dados/Escolas_Publicas_2.html')

# The resulting HTML file will contain a map with markers for building locations.

