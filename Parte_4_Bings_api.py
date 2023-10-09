import pandas as pd
import geopandas as gpd
import folium
import http.client
from shapely.geometry import Point
import json
import urllib.parse

# Replace 'YOUR_API_KEY' with your actual Bing Maps API key
api_key = 'z3nOPxYlgmXG24uetrkapw1NPvqOo0Kbc8VAq8DPx9Y'

# Load your data into a DataFrame
df_mun_func = pd.read_csv('E:/GitHub/UFU_MAPPERS/microdados/dados/microdados_uberlandia_em_funcionamento_reduzido.csv', delimiter = ';',
                           encoding = 'iso-8859-1', low_memory=False)

# Define a function to geocode an address using Bing Maps Geocoding API
def geocode_address(address):
    try:
        conn = http.client.HTTPSConnection('dev.virtualearth.net') 
        params = {
            'q': address,
            'key': api_key,
        }
        conn.request("GET", f'/REST/v1/Locations?' + str(address) + '?o=xml&key=' + api_key)
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        result = json.loads(data)

        if result.get('resourceSets'):
            locations = result['resourceSets'][0]['resources']
            if locations:
                location = locations[0]['point']
                return Point(location['coordinates'][1], location['coordinates'][0])
        else:
            return None
    except Exception as e:
        print(f"Error geocoding address: {address}\nError: {str(e)}")
        return None
    

# Step 4: Create a new column 'full_address' with the combined address
df_mun_func['full_address'] = df_mun_func['DS_ENDERECO'] + ' ' + df_mun_func['NU_ENDERECO'] + ' ' + df_mun_func['NO_MUNICIPIO'] + ' ' +  'MG' + ' ' + 'Brasil'
df_mun_func['full_address'] = df_mun_func['full_address'].str.replace(' ', '%')
df_mun_func['full_address'] = df_mun_func['full_address'].str.encode('utf-8')

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
m.save('E:/GitHub/UFU_MAPPERS/microdados/dados/building_locations_map_bing.html')

# The resulting HTML file will contain a map with markers for building locations.

