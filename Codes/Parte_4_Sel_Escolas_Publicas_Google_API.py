# O código abaixo lê os dados de endereço das escolas, realiza a geocodificação usando a API do Google, 
# gera o GeoDataFrame e salva o arquivo em formato SHP.

# Passo 1: Importar bibliotecas necessárias
import pandas as pd  # Para manipulação de dados
import geopandas as gpd  # Para dados geoespaciais
import folium  # Para criar mapas
from shapely.geometry import Point  # Para trabalhar com geometrias
import googlemaps  # Para a API do Google Maps

# Carregar a chave da API do Google
# Nao salve a API diretamente no código-fonte. Recomenda-se salvar a chave em um arquivo de texto e carregá-la no código. Assim, você pode compartilhar o código sem compartilhar a chave.
with open('.../Key_Google_API.txt', 'r') as arquivo_chave_api:
    chave_api = arquivo_chave_api.read()
print(chave_api)

# Passo 2: Carregar os dados em um DataFrame
# Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo de dados (por exemplo, um arquivo CSV)
df_mun_func = pd.read_csv('.../microdados_uberlandia_em_funcionamento.csv', 
                          delimiter=';', encoding='iso-8859-1', low_memory=False)

# Seleção de escolas Publicas (Federal, Estadual e Municipal)
selecao = (df_mun_func['TP_DEPENDENCIA'] == 1) | (df_mun_func['TP_DEPENDENCIA'] == 2) | (df_mun_func['TP_DEPENDENCIA'] == 3)
df_mun_publicas = df_mun_func.loc[selecao]
df_mun_particulares = df_mun_func.loc[~selecao]

# Exibir o total de escolas
print("Total de escolas: " + str(df_mun_func['CO_ENTIDADE'].count()))  
print("Total de escolas públicas: " + str(df_mun_publicas['CO_ENTIDADE'].count()))
print("Total de escolas particulares: " + str(df_mun_particulares['CO_ENTIDADE'].count()))

# Inicializar o cliente de geocodificação do Google Maps
gmaps = googlemaps.Client(key=chave_api)

# Função para geocodificar um endereço
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

# Passo 4: Criar uma nova coluna 'full_address' com o endereço combinado
df_mun_publicas['full_address'] = 'Brasil' + ', ' + 'MG' + ', ' + df_mun_publicas['NO_MUNICIPIO'] + ', ' + df_mun_publicas['DS_ENDERECO'] + ', ' + df_mun_publicas['NU_ENDERECO']
df_mun_particulares['full_address'] = 'Brasil' + ', ' + 'MG' + ', ' + df_mun_particulares['NO_MUNICIPIO'] + ', ' + df_mun_particulares['DS_ENDERECO'] + ', ' + df_mun_particulares['NU_ENDERECO']

# Passo 5: Aplicar a função de geocodificação para criar uma coluna 'geometry'
df_mun_publicas['geometry'] = df_mun_publicas['full_address'].apply(geocode_address)

# Salvar os dados de escolas públicas
df_mun_publicas.to_csv('.../Em_funcionamento_publicas.csv', sep=';', encoding='iso-8859-1', index=False)

# Passo 6: Criar um GeoDataFrame a partir do DataFrame e salvar em formato SHP
gdf_publicas = gpd.GeoDataFrame(df_mun_publicas, geometry='geometry')
gdf_publicas.to_file('.../Em_funcionamento_publicas.shp', driver='ESRI Shapefile')

# Passo 7: Criar um mapa usando Folium e adicionar marcadores para as localizações das escolas
# Substitua 'latitude' e 'longitude' pelas coordenadas desejadas do centro do mapa
# No caso de Uberlândia, as coordenadas são: -18.9186, -48.2772
centro_mapa = (-18.9186, -48.2772)
m = folium.Map(location=centro_mapa, zoom_start=13)

# Loop para adicionar marcadores no mapa
for idx, row in gdf_publicas.iterrows():
    if not pd.isnull(row['geometry']):
        folium.Marker(location=[row.geometry.y, row.geometry.x], popup=row['NO_ENTIDADE'], icon=folium.Icon(color='green', icon='school', prefix='fa')).add_to(m)

# Passo 8: Salvar o mapa como um arquivo HTML ou exibi-lo em um Jupyter Notebook
m.save('.../mapa_localizacoes_escolas.html')

# O arquivo HTML resultante conterá um mapa com marcadores para as localizações das escolas.
