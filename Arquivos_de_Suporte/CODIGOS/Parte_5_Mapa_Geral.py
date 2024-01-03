"""
Parte_5_Mapa_Geral.py

Este script Python utiliza as bibliotecas pandas, geopandas e folium para criar um mapa interativo com marcadores para as localizações dos prédios.

Passos:
1. Carrega um GeoDataFrame a partir de um arquivo SHP.
2. Define o centro do mapa com base em coordenadas específicas.
3. Cria um mapa usando a biblioteca folium.
4. Define uma cor para todos os marcadores.
5. Itera sobre o GeoDataFrame, adicionando marcadores ao mapa para cada prédio. A localização de cada marcador é determinada pelas coordenadas de cada prédio no GeoDataFrame. O texto do popup de cada marcador é o valor da coluna 'NO_ENTIDAD'.
6. Salva o mapa em um arquivo HTML.

Observações:
- Substitua 'caminho_para_GeoData_Frame.shp' pelo caminho para o seu arquivo SHP.
- Substitua 'latitude' e 'longitude' pelas coordenadas do centro do seu mapa. Para Uberlândia, as coordenadas são: -18.9186, -48.2772.
- Substitua 'NO_ENTIDAD' pelo nome da coluna desejada.
- Substitua 'Caminho/Meu_mapa.html' pelo caminho onde você deseja salvar o arquivo HTML do mapa.
"""

import pandas as pd
import geopandas as gpd
import folium

# Carregar o GeoDataFrame já salvo em formato SHP
gdf = gpd.read_file('caminho_para_GeoData_Frame.shp')

# Passo 7: Criar um mapa usando Folium e adicionar marcadores para as localizações dos prédios
# Substitua 'latitude' e 'longitude' pelas coordenadas do centro do seu mapa
# Para Uberlândia, as coordenadas são: -18.9186, -48.2772
map_center = (-18.9186, -48.2772)
m = folium.Map(location=map_center, zoom_start=13)

# Escolha uma cor para todos os marcadores
marker_color = 'blue'  # Por exemplo, azul

# Adicionar marcadores ao mapa
for idx, row in gdf.iterrows():
    if not pd.isnull(row['geometry']):
        location = [row.geometry.y, row.geometry.x]
        popup_text = row['NO_ENTIDAD']  # Substitua 'NO_ENTIDAD' pelo nome da coluna desejada

        marker = folium.Marker(
            location=location,
            popup=popup_text,
            icon=folium.Icon(color=marker_color, icon='school', prefix='fa')
        )
        marker.add_to(m)

# Salvar o mapa em HTML
m.save('Caminho/Meu_mapa.html')

# O arquivo HTML resultante conterá um mapa com marcadores para as localizações dos prédios.
