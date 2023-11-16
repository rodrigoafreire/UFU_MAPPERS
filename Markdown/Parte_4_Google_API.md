# Tutorial de Mapeamento de Escolas com Python e Google Maps API

Este tutorial ensina como usar Python, junto com a API do Google Maps, para mapear a localização de escolas. 

## Introdução
A API do Google Maps é uma ferramenta poderosa para desenvolvedores que permite integrar recursos de mapeamento e geolocalização em aplicativos e sites. Este guia fornecerá uma visão geral de como adquirir uma chave de API, entender os custos potenciais, usá-la eficientemente e evitar problemas comuns.

### Como Adquirir uma Chave de API
1. **Crie uma conta no Google Cloud Platform (GCP)**: Visite [Google Cloud Platform](https://cloud.google.com/) e crie uma conta. Se você já tiver uma conta do Google, pode usar a mesma para acessar o GCP.
2. **Crie um projeto no GCP**: Após fazer login, crie um novo projeto no GCP. Isso fornecerá um ambiente isolado para gerenciar seus serviços e chaves de API.
3. **Habilite a API do Google Maps**: No painel do projeto, acesse a seção "APIs e Serviços" e habilite as APIs necessárias, como Maps JavaScript API, Geocoding API, etc.
4. **Obtenha sua chave de API**: Após habilitar as APIs necessárias, vá para "Credenciais" e crie uma chave de API. Anote sua chave, pois ela será necessária para fazer chamadas à API do Google Maps em seu código.

### Entendendo os Custos
- **Uso Gratuito**: O Google oferece um nível de uso gratuito para suas APIs do Maps. Este nível é suficiente para muitos desenvolvedores com necessidades básicas.
- **Custos Adicionais**: Se o uso exceder o nível gratuito, o Google cobrará taxas adicionais. Estas taxas variam com base no tipo de serviço da API utilizado e no número de solicitações feitas.
- **Estimativa de Custos**: Use o [Calculadora de preços](https://cloud.google.com/maps-platform/pricing) do Google para estimar os custos com base no seu uso previsto.

### Uso Eficiente da API
- **Limite suas requisições**: Tente limitar suas requisições à API para se manter dentro do nível de uso gratuito ou para reduzir custos.
- **Otimize as chamadas de API**: Consolide chamadas à API sempre que possível e evite chamadas desnecessárias.
- **Cache quando possível**: Armazene em cache os resultados das chamadas à API para evitar requisições repetidas.

### Evitando Problemas
- **Restrinja sua chave de API**: No Console do Google Cloud, restrinja o uso da sua chave de API a domínios ou IPs específicos para aumentar a segurança.
- **Monitore o uso**: Regularmente, verifique o uso da sua API no Console do GCP para identificar e corrigir quaisquer problemas de uso excessivo.
- **Atualize-se sobre mudanças**: Fique atento às atualizações do Google, pois as políticas e preços podem mudar.

### Documentação e Recursos
- Para mais informações, consulte a [documentação oficial da API do Google Maps](https://developers.google.com/maps/documentation).
- Em caso de dúvidas ou problemas, você também pode usar [Google Maps Platform Support](https://developers.google.com/maps/support/).

---
---
---
## Utilizando a API do GoogleMaps 

```
Este guia serve como uma introdução básica à API do Google Maps, fornecendo informações essenciais para começar a usar este poderoso serviço em seus projetos.
```

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

Carregamos os dados em um DataFrame do Pandas. Substitua o caminho pelo caminho do seu arquivo de dados.

```python
df_mun_func = pd.read_csv('caminho_do_arquivo/microdados_uberlandia_em_funcionamento.csv', delimiter=';', encoding='iso-8859-1', low_memory=False)
```

### Passo 3: Criação de uma Função de Geocodificação

Criamos uma função para geocodificar endereços usando a biblioteca Geopy.

```python
def geocode_address(address):
    geolocator = Nominatim(user_agent="uberlandia_locator")  # Criar um geocodificador
    location = geolocator.geocode(address)  # Obter coordenadas do endereço
    if location:
        print(Point(location.longitude, location.latitude))
        return Point(location.longitude, location.latitude)  # Retornar como um Ponto
    else:
        return None  # Retornar None se a geocodificação falhar
```

### Passo 4: Criação de uma Coluna com Endereço Completo

Combinamos dados de endereço para formar um endereço completo.

```python
df_mun_publicas['full_address'] = 'Brasil' + ', ' + 'MG' + ', ' + df_mun_publicas['NO_MUNICIPIO'] + ', ' + df_mun_publicas['DS_ENDERECO'] + ', ' + df_mun_publicas['NU_ENDERECO']
df_mun_particulares['full_address'] = 'Brasil' + ', ' + 'MG' + ', ' + df_mun_particulares['NO_MUNICIPIO'] + ', ' + df_mun_particulares['DS_ENDERECO'] + ', ' + df_mun_particulares['NU_ENDERECO']
```

### Passo 5: Aplicação da Função de Geocodificação

Aplicamos a função de geocodificação para criar colunas de geometria.

```python
df_mun_publicas['geometry'] = df_mun_publicas['full_address'][0:15].apply(geocode_address)
df_mun_particulares['geometry'] = df_mun_particulares['full_address'][0:15].apply(geocode_address)
```

### Passo 6: Criação de um GeoDataFrame

Transformamos os DataFrames em GeoDataFrames.

```python
gdf_publicas = gpd.GeoDataFrame(df_mun_publicas, geometry='geometry')
gdf_particulares = gpd.GeoDataFrame(df_mun_particulares, geometry='geometry')
```

### Passo 7: Criação de um Mapa com Folium

Criamos um mapa usando Folium e adicionamos marcadores para as localizações das escolas.

```python
map_center = (-18.9186, -48.2772)  # Coordenadas do centro do mapa para Uberlândia
m = folium.Map(location=map_center, zoom_start=13)

# Loop para adicionar marcadores no mapa
for idx, row in gdf_publicas.iterrows():
    if not pd.isnull(row['geometry']):
        folium.Marker(location=[row.geometry.y, row.geometry.x], popup=row['NO_ENTIDADE'], icon=(folium.Icon(color='green', icon='school', prefix='fa'))).add_to(m)

for idx, row in gdf_particulares.iterrows():
    if not pd.isnull(row['geometry']):
        folium.Marker(location=[row.geometry.y, row.geometry.x], popup=row['NO_ENTIDADE'], icon=(folium.Icon(color='lightgray', icon='school', prefix='fa'))).add_to(m)
```

### Passo 8: Salvamento do Mapa

Salvamos o mapa como um arquivo HTML.

```python
m.save('caminho_para_salvar_o_arquivo/mapa_de_localizacoes.html')
```

O arquivo HTML resultante conterá um mapa com marcadores para as localizações das escolas.
```