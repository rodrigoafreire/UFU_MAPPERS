# Criando um Mapa com Dados Geoespaciais

Este tutorial irá orientá-lo através de um script Python que carrega dados geoespaciais e cria um mapa interativo. O script utiliza bibliotecas como `pandas`, `geopandas` e `folium`.

## Pré-requisitos

- Conhecimento básico de Python
- Python instalado no seu sistema
- Bibliotecas: `pandas`, `geopandas`, `folium`

## Passo 1: Importar Bibliotecas

```python
import pandas as pd
import geopandas as gpd
import folium
```

- `pandas`: Uma biblioteca para manipulação e análise de dados.
- `geopandas`: Uma extensão do `pandas` para trabalhar com dados geoespaciais.
- `folium`: Uma biblioteca para criar mapas interativos.

## Passo 2: Carregar Dados Geoespaciais

```python
gdf = gpd.read_file('caminho/para/seu/arquivo.shp')
```

- Substitua `'caminho/para/seu/arquivo.shp'` pelo caminho do seu arquivo SHP.
- `gdf` significa GeoDataFrame, uma estrutura de dados para dados geoespaciais.
- Caso queira utilizar o arquivo SHP disponibilizado neste repositório, acesse a pasta **Arquivos_de_Suporte**

## Passo 3: Criar um Mapa

Primeiro, crie um mapa vazio com a função `folium.Map()`.
A função `folium.Map()` recebe um parâmetro `location` que define o centro do mapa. O parâmetro `zoom_start` define o nível de zoom inicial do mapa. Outros parâmetros podem ser passados para a função `folium.Map()`, como `tiles` e `zoom_control`. Para saber mais consulte a documentação do Folium (https://python-visualization.github.io/folium/quickstart.html).

```python
# Substitua estas coordenadas pelo centro desejado do seu mapa
# Em Uberlândia, MG, Brasil os valores são: latitude = -18.9186, longitude = -48.2772

map_center = (-18.9186, -48.2772)
m = folium.Map(location=map_center, zoom_start=13)
```
- `map_center`: Uma tupla contendo latitude e longitude do centro do mapa.
- `zoom_start`: Nível de zoom inicial do mapa.

## Passo 4: Adicionar Marcadores ao Mapa

Vamos escolher a cor azul para os marcadores. Para isso, vamos definir uma variável `marker_color` com o valor `'blue'`.

```python
marker_color = 'blue'
```

Em seguida, vamos criar um loop para adicionar marcadores ao mapa. O loop deve iterar sobre as linhas do GeoDataFrame `gdf` criado no Passo 2. Para cada linha, o loop deve criar um marcador com a função `folium.Marker()`. O marcador deve ser adicionado ao mapa com a função `folium.Marker.add_to()`. Note que também conferimos se a linha possui um valor válido para a coluna `geometry` antes de criar o marcador. 

```python
for idx, row in gdf.iterrows():
    if not pd.isnull(row['geometry']): # Verifica se a linha possui um valor válido para a coluna 'geometry'
        location = [row.geometry.y, row.geometry.x] # Extrai a latitude e longitude da linha
        popup_text = row['NO_ENTIDAD']  # Substitua 'NO_ENTIDAD' pelo nome da coluna desejada

        marker = folium.Marker(
            location=location,
            popup=popup_text,
            icon=folium.Icon(color=marker_color, icon='school', prefix='fa')
        )
        marker.add_to(m)
```





O script provavelmente terá código adicional para adicionar marcadores ou outros elementos ao mapa. Este código varia dependendo do seu conjunto de dados e do que você deseja exibir.

## Passo 5: Salvar e Exibir o Mapa

O script provavelmente conclui com comandos para salvar o mapa como um arquivo HTML ou exibi-lo em um notebook Jupyter.


