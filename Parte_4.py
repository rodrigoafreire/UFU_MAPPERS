# Step 1: Import necessary libraries
import pandas as pd  # For handling data
import geopandas as gpd  # For geospatial data
import folium  # For creating maps
from geopy.geocoders import Nominatim  # For geocoding addresses
from shapely.geometry import Point  # For working with geometries

# Step 2: Load your data into a DataFrame
# Replace 'your_table.csv' with the path to your data file (e.g., a CSV file)
df_mun_func = pd.read_csv('E:/GitHub/UFU_MAPPERS/microdados/dados/microdados_uberlandia_em_funcionamento_reduzido.csv', delimiter = ';',
                           encoding = 'iso-8859-1', low_memory=False)

# Step 3: Create a geocoding function using Geopy
def geocode_address(address):
    geolocator = Nominatim(user_agent="uberlandia_locator")  # Create a geocoder
    location = geolocator.geocode(address)  # Get coordinates from the address
    if location:
        return Point(location.longitude, location.latitude)  # Return as a Point
    else:
        return None  # Return None if geocoding fails

# Step 4: Create a new column 'full_address' with the combined address
df_mun_func['full_address'] = 'Brasil' + ', ' + 'MG' + ', ' + df_mun_func['NO_MUNICIPIO'] + ', ' + df_mun_func['DS_ENDERECO'] + ', ' + df_mun_func['NU_ENDERECO']

# Step 5: Apply the geocoding function to create a 'geometry' column
df_mun_func['geometry'] = df_mun_func['full_address'].apply(geocode_address)

# Step 6: Create a GeoDataFrame from the DataFrame
gdf = gpd.GeoDataFrame(df_mun_func, geometry='geometry')

# Step 7: Create a map using Folium and add markers for building locations
# Replace 'latitude' and 'longitude' with your desired map center coordinates
# No caso de Uberlandia, as coordenadas são: -18.9186, -48.2772
map_center = (-18.9186, -48.2772)
m = folium.Map(location=map_center, zoom_start=13)

print(gdf.head(40))

# Loop through each row in the GeoDataFrame and add a marker for each building
for idx, row in gdf.iterrows():
    if not pd.isnull(row['geometry']):
        folium.Marker(location=[row.geometry.y, row.geometry.x], popup=row['NO_ENTIDADE']).add_to(m)

# Step 8: Save the map as an HTML file or display it in a Jupyter Notebook
m.save('E:/GitHub/UFU_MAPPERS/microdados/dados/building_locations_map.html')

# The resulting HTML file will contain a map with markers for building locations.
