# Tutorial de Mapeamento Geoespacial com Python

Este tutorial demonstra como criar um mapa geoespacial de localizações usando Python.

### Passo 1: Importação de Bibliotecas Necessárias

Importamos as bibliotecas necessárias para manipulação de dados, dados geoespaciais e criação de mapas.

```python
import pandas as pd  # Para manipulação de dados
import geopandas as gpd  # Para dados geoespaciais
import folium  # Para criar mapas
from geopy.geocoders import Nominatim  # Para geocodificação de endereços
from shapely.geometry import Point  # Para trabalhar com geometrias
```

### Passo 2: Carregar os Dados

Carregamos os dados em um DataFrame. Substitua o caminho pelo caminho do seu arquivo de dados.

```python
df_mun_func = pd.read_csv('caminho_do_arquivo/microdados_uberlandia_em_funcionamento_reduzido.csv', delimiter=';', encoding='iso-8859-1', low_memory=False)
```

### Passo 3: Criar uma Função de Geocodificação

Criamos uma função para geocodificar endereços usando Geopy. No caso, estamos usando a API Nominatim do OpenStreetMap. A função retorna um objeto Point do Shapely. No entanto, os testes que realizamos mostraram que a API não é muito precisa para endereços no Brasil. Portanto, é recomendável usar outra API ou fonte de dados para obter melhores resultados. Ensinamos como usar a API do Google Maps para geocodificação em outro tutorial.

```python
def geocode_address(address):
    geolocator = Nominatim(user_agent="uberlandia_locator")  # Criar um geocodificador
    location = geolocator.geocode(address)  # Obter coordenadas do endereço
    if location:
        return Point(location.longitude, location.latitude)  # Retornar como um Ponto
    else:
        return None  # Retornar None se a geocodificação falhar
```

### Passo 4: Criar uma Coluna com o Endereço Completo

Combinamos os dados de endereço para formar um endereço completo.

```python
df_mun_func['full_address'] = 'Brasil' + ', ' + 'MG' + ', ' + df_mun_func['NO_MUNICIPIO'] + ', ' + df_mun_func['DS_ENDERECO'] + ', ' + df_mun_func['NU_ENDERECO']
```

### Passo 5: Aplicar a Função de Geocodificação

Aplicamos a função de geocodificação para criar uma coluna de geometria.

```python
df_mun_func['geometry'] = df_mun_func['full_address'].apply(geocode_address)
```

### Passo 6: Criar um GeoDataFrame

Transformamos o DataFrame em um GeoDataFrame. Um **GeoDataFrame** é um DataFrame que contém uma coluna de geometria. Neste caso, a coluna de geometria contém os pontos criados pela função de geocodificação.

```python
gdf = gpd.GeoDataFrame(df_mun_func, geometry='geometry')
```

### Passo 7: Criar um Mapa com Folium

Criamos um mapa usando Folium e adicionamos marcadores para as localizações.
Sugerimos que você consulte a documentação do Folium para aprender mais sobre como criar mapas com Folium. Você pode encontrar a documentação aqui: https://python-visualization.github.io/folium/ 

O Marcador pode ser personalizado com ícones e popups. Você pode encontrar mais informações sobre como personalizar marcadores aqui: https://python-visualization.github.io/folium/modules.html#folium.map.Marker (Mostraremos a personalização em um outro tutorial)

```python
map_center = (-18.9186, -48.2772)  # Coordenadas do centro do mapa para Uberlândia
m = folium.Map(location=map_center, zoom_start=13)

# Loop para adicionar marcadores no mapa
for idx, row in gdf.iterrows():
    if not pd.isnull(row['geometry']):
        folium.Marker(location=[row.geometry.y, row.geometry.x], popup=row['NO_ENTIDADE']).add_to(m)
```

### Passo 8: Salvar o Mapa

Salvamos o mapa como um arquivo HTML.

```python
m.save('caminho_para_salvar_o_arquivo/mapa_de_localizacoes.html')
```

O arquivo HTML resultante conterá um mapa com marcadores para as localizações dos prédios.
```
