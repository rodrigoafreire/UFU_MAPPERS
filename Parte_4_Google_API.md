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


```markdown
# Tutorial de Mapeamento Geoespacial de Escolas

Este tutorial demonstra como realizar a geocodificação de endereços de escolas usando a API do Google, gerar um GeoDataFrame e salvar os dados em formato SHP.

### Passo 1: Importar Bibliotecas Necessárias

```python
import pandas as pd  # Para manipulação de dados
import geopandas as gpd  # Para dados geoespaciais
import folium  # Para criar mapas
from shapely.geometry import Point  # Para trabalhar com geometrias
import googlemaps  # Para a API do Google Maps
```
**Dica**: Importar as bibliotecas corretas é fundamental para trabalhar com dados geoespaciais.

### Carregar a Chave da API do Google

```python
with open('E:/GitHub/UFU_MAPPERS/Config/Key_Google_API.txt', 'r') as arquivo_chave_api:
    chave_api = arquivo_chave_api.read()
print(chave_api)
```
**Dica**: Mantenha sua chave de API segura e não a compartilhe publicamente.

### Passo 2: Carregar os Dados em um DataFrame

```python
df_mun_func = pd.read_csv('E:/GitHub/UFU_MAPPERS/microdados/dados/microdados_uberlandia_em_funcionamento.csv', delimiter=';', encoding='iso-8859-1', low_memory=False)
```
**Dica**: Certifique-se de que o caminho para o arquivo CSV está correto.

### Seleção de Escolas e Exibição de Totais

```python
selecao = (df_mun_func['TP_DEPENDENCIA'] == 1) | (df_mun_func['TP_DEPENDENCIA'] == 2) | (df_mun_func['TP_DEPENDENCIA'] == 3)
df_mun_publicas = df_mun_func.loc[selecao]
df_mun_particulares = df_mun_func.loc[~selecao]
print("Total de escolas: " + str(df_mun_func['CO_ENTIDADE'].count()))  
print("Total de escolas públicas: " + str(df_mun_publicas['CO_ENTIDADE'].count()))
print("Total de escolas particulares: " + str(df_mun_particulares['CO_ENTIDADE'].count()))
```

### Inicializar o Cliente de Geocodificação do Google Maps

```python
gmaps = googlemaps.Client(key=chave_api)
```

### Função para Geocodificar um Endereço

```python
def geocode_address(endereco):
    try:
        resultado_geocode = gmaps.geocode(endereco)
        if resultado_geocode:
            localizacao = resultado_geocode[0]['geometry']['location']
            print(localizacao)
            return Point(localizacao['lng'], localizacao['lat'])
        else:
            return None
    except Exception as e:
        print(f"Erro ao geocodificar o endereço: {endereco}\nErro: {str(e)}")
        return None
```

### Passo 4: Criar uma Nova Coluna com o Endereço Combinado

```python
df_mun_publicas['full_address'] = 'Brasil' + ', ' + 'MG' + ', ' + df_mun_publicas['NO_MUNICIPIO'] + ', ' + df_mun_publicas['DS_ENDERECO'] + ', ' + df_mun_publicas['NU_ENDERECO']
df_mun_particulares['full_address'] = 'Brasil' + ', ' + 'MG' + ', ' + df_mun_particulares['NO_MUNICIPIO'] + ', ' + df_mun_particulares['DS_ENDERECO'] + ', ' + df_mun_particulares['NU_ENDERECO']
```

### Passo 5: Aplicar a Função de Geocodificação para Criar uma Coluna 'Geometry'

```python
df_mun_publicas['geometry'] = df_mun_publicas['full_address'].apply(geocode_address)
```

### Salvar os Dados de Escolas Públicas

```python
df_mun_publicas.to_csv('E:/GitHub/UFU_MAPPERS/microdados/dados/UDI_em_funcionamento_publicas.csv', sep=';', encoding='iso-8859-1', index=False)
```

### Passo 6: Criar um GeoDataFrame e Salvar em Formato SHP

```python
gdf_publicas = gpd.GeoDataFrame(df_mun_publicas, geometry='geometry')
gdf_publicas.to_file('E:/GitHub/UFU_MAPPERS/microdados/SHP/UDI_em_funcionamento_publicas.shp', driver='ESRI Shapefile')
```

### Passo 7: Criar um Mapa Usando Folium e Adicionar Marcadores

```python
centro_mapa = (-18.9186, -48.2772)
m = folium.Map(location=centro_mapa, zoom_start=13)
for idx, row in gdf_publicas.iterrows():
    if not pd.isnull(row['geometry']):
        folium.Marker(location=[row.geometry.y, row.geometry.x], popup=row['NO_ENTIDADE'], icon=folium.Icon(color='green', icon='school', prefix='fa')).add_to(m)
```

### Passo 8: Salvar o Mapa Como um Arquivo HTML

```python
m.save('E:/GitHub/UFU_MAPPERS/microdados/dados/mapa_localizacoes_escolares.html')
```

O arquivo HTML resultante conterá um mapa com marcadores para as localizações das escolas.
```