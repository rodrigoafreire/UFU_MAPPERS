# Passo 1: Importar bibliotecas necessárias
import pandas as pd  # Para manipulação de dados
import geopandas as gpd  # Para dados geoespaciais
import folium  # Para criar mapas
from geopy.geocoders import Nominatim  # Para geocodificação de endereços
from shapely.geometry import Point  # Para trabalhar com geometrias

# Passo 2: Carregar seus dados em um DataFrame
# Substitua 'caminho_para_seu_arquivo.csv' pelo caminho para o seu arquivo de dados (por exemplo, um arquivo CSV)
df_mun_func = pd.read_csv('caminho_para_seu_arquivo.csv', delimiter=';', encoding='iso-8859-1', low_memory=False)

# Passo 3: Criar uma função de geocodificação usando Geopy
def geocode_address(address):
    geolocator = Nominatim(user_agent="localizador_personalizado")  # Criar um geocodificador
    location = geolocator.geocode(address)  # Obter coordenadas a partir do endereço
    if location:
        return Point(location.longitude, location.latitude)  # Retornar como um Ponto
    else:
        return None  # Retornar None se a geocodificação falhar

# Passo 4: Criar uma nova coluna 'full_address' com o endereço combinado
df_mun_func['full_address'] = 'Brasil' + ', ' + 'MG' + ', ' + df_mun_func['NO_MUNICIPIO'] + ', ' + df_mun_func['DS_ENDERECO'] + ', ' + df_mun_func['NU_ENDERECO']

# Passo 5: Aplicar a função de geocodificação para criar uma coluna 'geometry'
df_mun_func['geometry'] = df_mun_func['full_address'].apply(geocode_address)

# Passo 6: Criar um GeoDataFrame a partir do DataFrame
gdf = gpd.GeoDataFrame(df_mun_func, geometry='geometry')

# Passo 7: Criar um mapa usando Folium e adicionar marcadores para as localizações dos prédios
# Substitua 'latitude' e 'longitude' pelas coordenadas do centro do seu mapa
# Para Uberlândia, as coordenadas são: -18.9186, -48.2772
map_center = (-18.9186, -48.2772)
m = folium.Map(location=map_center, zoom_start=13)

print(gdf.head(40))

# Percorrer cada linha no GeoDataFrame e adicionar um marcador para cada prédio
for idx, row in gdf.iterrows():
    if not pd.isnull(row['geometry']):
        folium.Marker(location=[row.geometry.y, row.geometry.x], popup=row['NO_ENTIDADE']).add_to(m)

# Passo 8: Salvar o mapa como um arquivo HTML ou exibi-lo em um Jupyter Notebook
m.save('caminho_para_salvar_o_arquivo/mapa_localizacoes_predios.html')

# O arquivo HTML resultante conterá um mapa com marcadores para as localizações dos prédios.
