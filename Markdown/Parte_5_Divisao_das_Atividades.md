# Tutorial de Criação de Mapa Interativo com Python

Este tutorial demonstra como criar um mapa interativo utilizando Python, Geopandas e Folium. O objetivo é mapear localizações específicas com marcadores coloridos em um mapa.

## Importação de Bibliotecas
Primeiro, importamos as bibliotecas necessárias.
```python
import pandas as pd
import geopandas as gpd
import folium
```

## Carregar Dados Geoespaciais
Carregamos um GeoDataFrame já existente a partir de um arquivo Shapefile (SHP).
```python
gdf = gpd.read_file('caminho_para_seu_arquivo.shp')
```

## Criação do Mapa Base
Inicializamos um mapa base usando a biblioteca Folium. As coordenadas são centradas em Uberlândia.
```python
map_center = (-18.9186, -48.2772)
m = folium.Map(location=map_center, zoom_start=13)
```

## Preparação dos Dados
Determinamos o número de subconjuntos e suas cores correspondentes.
```python
num_subsets = 7
subset_size = len(gdf) // num_subsets
remaining_locations = len(gdf) % num_subsets
colors = ['red', 'blue', 'green', 'orange', 'purple', 'pink', 'cadetblue']
```

## Atribuição de Cores e Salvar Subconjuntos
Cada subconjunto de dados é atribuído uma cor e salvo como um arquivo SHP.
```python
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
```

## Adição de Marcadores no Mapa
Marcadores são adicionados ao mapa para cada localização no GeoDataFrame.
```python
for i in range(num_subsets):
    subset = gdf[start_idx:subset_end]
    color = colors[i]
    Atr = Atrs[i]

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
```

## Salvamento do Mapa
Finalmente, o mapa é salvo como um arquivo HTML.
```python
m.save('caminho_para_salvar_o_arquivo_final.html')
```

Este tutorial oferece um exemplo prático de como criar um mapa interativo com marcadores para localizações específicas usando Python e bibliotecas geoespaciais.

```
