import pandas as pd
import geopandas as gpd
import folium

# Carregar o GeoDataFrame já salvo em formato SHP
gdf = gpd.read_file('caminho_para_seu_arquivo.shp')

# Passo 7: Criar um mapa usando Folium e adicionar marcadores para as localizações dos prédios
# Substitua 'latitude' e 'longitude' pelas coordenadas do centro do seu mapa
# Para Uberlândia, as coordenadas são: -18.9186, -48.2772
map_center = (-18.9186, -48.2772)
m = folium.Map(location=map_center, zoom_start=13)

print(gdf.head(40))

# Passo 1: Determinar o número de subconjuntos e calcular o tamanho aproximado de cada subconjunto
num_subsets = 7
subset_size = len(gdf) // num_subsets
remaining_locations = len(gdf) % num_subsets

# Passo 2: Definir cores únicas para cada subconjunto
colors = ['red', 'blue', 'green', 'orange', 'purple', 'pink', 'cadetblue']  # Adicione mais cores conforme necessário

# Atribuir as cores para os mapeadores
Atrs = ['Nome_1', 'Nome_2', 'Nome_3', 'Nome_4', 'Nome_5', 'Nome_6', 'Nome_7']

start_idx = 0

for i in range(num_subsets):
    subset_end = start_idx + subset_size
    if i < remaining_locations:
        subset_end += 1

    subset = gdf[start_idx:subset_end]
    color = colors[i]
    Atr = Atrs[i]
    subset.to_file('caminho_para_salvar_o_arquivo_' + str(i) + '_'+ Atr + '.shp', driver='ESRI Shapefile')

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
    m.save('caminho_para_salvar_o_arquivo_' + Atr + '.html')

# Passo 8: Salvar o mapa como um arquivo HTML ou exibi-lo em um Jupyter Notebook
m.save('caminho_para_salvar_o_arquivo_final.html')

# O arquivo HTML resultante conterá um mapa com marcadores para as localizações dos prédios.
