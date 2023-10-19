import pandas as pd
import geopandas as gpd
import folium
import googlemaps
from shapely.geometry import Point

# Replace 'YOUR_API_KEY' with your actual Google Maps Geocoding API key
api_key = 'seuapi aqui'

# Load your data into a DataFrame
df_mun_func = pd.read_csv('E:/GitHub/UFU_MAPPERS/microdados/dados/microdados_uberlandia_em_funcionamento.csv', delimiter = ';',
                           encoding = 'iso-8859-1', low_memory=False)

# Initialize the Google Maps Geocoding client
gmaps = googlemaps.Client(key=api_key)

# Define a function to geocode an address using Google Maps Geocoding API
def geocode_address(address):
    try:
        geocode_result = gmaps.geocode(address)
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            print(location)
            return Point(location['lng'], location['lat'])
        else:
            return None
    except Exception as e:
        print(f"Error geocoding address: {address}\nError: {str(e)}")
        return None


# Step 4: Create a new column 'full_address' with the combined address
df_mun_func['full_address'] = 'Brasil' + ', ' + 'MG' + ', ' + df_mun_func['NO_MUNICIPIO'] + ', ' + df_mun_func['DS_ENDERECO'] + ', ' + df_mun_func['NU_ENDERECO']

# Step 5: Apply the geocoding function to create a 'geometry' column
df_mun_func['geometry'] = df_mun_func['full_address'].apply(geocode_address)

# Step 6: Create a GeoDataFrame from the DataFrame
gdf = gpd.GeoDataFrame(df_mun_func, geometry='geometry')

# Step 6.a Save GeoDataFrame to a Shapefile
gdf.to_file('E:/GitHub/UFU_MAPPERS/microdados/dados/uberlandia_em_func_google.shp', driver='ESRI Shapefile')


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
m.save('E:/GitHub/UFU_MAPPERS/microdados/dados/building_locations_map_google_2.html')

# The resulting HTML file will contain a map with markers for building locations.

