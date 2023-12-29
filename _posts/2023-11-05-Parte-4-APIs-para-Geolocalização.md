---
layout: post
title: Parte 4 - APIS e Geolocalização das Escolas
categories: [Escolas, Python]
---

Vamos gerar um mapa com a localização das escolas. Para isso, vamos usar a biblioteca folium. A biblioteca folium é uma biblioteca Python que facilita a criação de mapas interativos e visualizações geoespaciais. No entanto, existem diversas possibilidades para gerar os mapas pois precisamos de uma ferramenta *geocoding* para transformar o endereço em coordenadas geográficas. Diversas empresas oferecem esse serviço, como o Google Maps, o Bing Maps e a Tomtom. Em geral, é possível usar os serviços de forma gratuita até um certo número de requisições. Também existe uma ferramenta de geocoding do OpenStreetMap, chama Nominatim, que é gratuita. Como veremos mais a frente cada um dos serviços tem suas vantagens e desvantagens. No caso do Openstreetmap, ele depende do mapeamento realizado de forma colaborativa. Por isso, é possível que alguns endereços não sejam encontrados. 

Além disso, para ter um controle das requisições, é necessário utilizar uma chave de acesso. Para isso, é necessário criar uma conta no site do serviço de geocoding. No caso do Nominatim, é necessário definir apenas um *user-agent*, um nome que ficará vinculado às requisições. Já nos outros serviços, a chave de acesso é um código que deve ser inserido no código. Ela serve para identificar o usuário e controlar o número de requisições.

Vamos precisar dos seguintes pacotes:

    pandas
    geopandas
    folium
    geopy
    shapely

Você pode verificar se os pacotes estão instalados usando o comando **pip list** no prompt de comando. Caso algum pacote não esteja instalado, você pode instalar usando o comando pip install nome_do_pacote. Caso você não possua as bibliotecas, bastar instalar usando o comando pip install nome_da_biblioteca.

    pip install pandas
    pip install geopandas
    pip install folium
    pip install geopy
    pip install shapely

Com as bibliotecas instaladas podemos prosseguir. A primeira etapa é importar as bibliotecas.

    import pandas as pd  # For handling data
    import geopandas as gpd  # For geospatial data
    import folium  # For creating maps
    from geopy.geocoders import Nominatim  # For geocoding addresses
    from shapely.geometry import Point  # For working with geometries

Note que algumas bibliotecas foram importadas com um apelido, e.g. *pandas as pd*. Isso é opcional, mas é uma prática comum para economizar tempo e digitação. Outras bibliotecas foram importadas sem apelido, e.g. *from geopy.geocoders import Nominatim*. Isso é necessário para que possamos usar as funções da biblioteca sem precisar digitar o nome da biblioteca antes da função, e.g. *Nominatim()* ao invés de *geopy.geocoders.Nominatim()*.

Carregar os dados
O primeiro passo é carregar o dataframe:
    
        df = pd.read_csv('C:/Users/.../ESCOLAS_UBERLANDIA_PARTE_2.CSV', delimiter=';', encoding='latin')

Vamos também definir uma variável para o user-agent do Nominatim:

    user_agent = 'definir um nome'

Vamos agora criar uma função no python para extrair os dados de geocoding do Nominatim. Para isso, usamos a função geocode() da biblioteca geopy. Os argumentos da função são o endereço que queremos geocodificar (address) e o user-agent que definimos anteriormente (user_agent). A função retorna um objeto do tipo Location, que contém as coordenadas geográficas do endereço.

    def geocode_address(address, user_agent):
        geolocator = Nominatim(user_agent=user_agent)
        location = geolocator.geocode(address)
        if location:
            return Point(location.longitude, location.latitude)
            print(location.longitude, location.latitude)
        else:
            return None    

Uma função é um bloco de código que executa uma tarefa específica. No caso, a função geocode_address() executa a tarefa de geocodificar um endereço. Para definir uma função, usamos a palavra reservada def, seguida do nome da função e dos argumentos da função entre parênteses. No caso, a função geocode_address() tem dois argumentos: address e user_agent. Em seguida, usamos a palavra reservada return para retornar o resultado da função. No caso, a função retorna um objeto do tipo Point, que contém as coordenadas geográficas do endereço. Se o endereço não for encontrado, a função retorna None. 
Para chamar uma função, usamos o nome da função seguido dos argumentos entre parênteses. No caso, para chamar a função geocode_address(), usamos o nome da função geocode_address() seguido dos argumentos address e user_agent entre parênteses. No caso, o argumento address é o endereço que queremos geocodificar e o argumento user_agent é o user-agent que definimos anteriormente. Vamos ver isso, logo mais.

A variável **address** corresponde ao endereço das escolas que desejamos buscar. No entanto, o endereço das escolas não está em uma única coluna. Ele está dividido em várias colunas no noss dataframe. Por isso, vamos criar uma nova coluna chamada **full_address** com o endereço completo de cada escola. Em seguida, criamos uma nova coluna chamada **geometry** que irá armazer as coordenadas extraídas da função que acabamos de definir: **geocode_address()**. Para isso, usamos a função apply() da biblioteca Pandas. Os argumentos da função são a função que queremos aplicar (no caso, a função geocode_address()) e o argumento axis=1 para aplicar a função linha por linha. O resultado da função é armazenado na coluna **geometry**.

Primeiro definimos uma coluna com o endereço completo:
 
    df_mun_func['full_address'] = df_mun_func['DS_ENDERECO'] + ', ' + df_mun_func['NU_ENDERECO'] + ', ' + df_mun_func['NO_BAIRRO'] + ', ' + df_mun_func['NO_MUNICIPIO'] + ', ' + 'MG' + ', ' + 'Brasil'

Em seguida, definimos a coluna geometry e aplicamos a função geocode_address():

    df_mun_func['geometry'] = df_mun_func['full_address'].apply(geocode_address, user_agent=user_agent)

ao usar a função *apply* e chamar a função *geocode_address*, o endereço completo de cada escola é passado como argumento para a função *geocode_address*. Em seguida, a função *geocode_address* retorna um objeto do tipo Point, que contém as coordenadas geográficas do endereço. O resultado é armazenado na coluna **geometry**.
Agora temos nosso dataframe df_mun_func com as coordenadas necessárias para visualizar as escolas em um mapa. No entanto, precisamos transformar o dataframe em um geodataframe, que lida com dados geoespaciais e possibilita, por exemplo, gerar um arquivo shapefile. Para isso, usamos a função GeoDataFrame() da biblioteca geopandas. Os argumentos da função são o dataframe que queremos transformar (no caso, df_mun_func), o argumento geometry='geometry' para indicar que a coluna geometry contém as coordenadas geográficas.

    gdf = gpd.GeoDataFrame(df_mun_func, geometry='geometry')

Agora, vamos gerar um mapa com a localização das escolas. Para isso, usamos a função folium.Map() da biblioteca folium. Os argumentos da função são o local onde queremos centralizar o mapa (location), o nível de zoom (zoom_start) e o tipo de mapa (tiles). No caso, o local é definido pelas coordenadas geográficas de Uberlândia, o nível de zoom é 13 *(Mas podemos definir de diferentes maneiras) e o tipo de mapa é OpenStreetMap.

    map_center = (-18.9186, -48.2772) # Coordenadas geográficas de Uberlândia
    m = folium.Map(location=map_center, zoom_start=13) # Gerar o mapa

Com o mapa gerado, precisamos inserir os pontos referentes a cada escola. Para isso, usamos a função folium.Marker() da biblioteca folium. Os argumentos da função são as coordenadas geográficas do ponto (location), o popup que será exibido ao clicar no ponto (popup) e o ícone que será exibido no ponto (icon). No caso, o popup é o nome da escola e o ícone é um ícone de escola. Em seguida, usamos a função add_to() para adicionar o ponto ao mapa.
Primeiro iteramos as linhas do geodataframe gdf usando a função iterrows() da biblioteca Pandas. Os argumentos da função são o geodataframe que queremos iterar (no caso, gdf). O resultado da função é armazenado na variável gdf. Em seguida, usamos a função folium.Marker() para adicionar o ponto ao mapa. Os argumentos da função são as coordenadas geográficas do ponto (location), o popup que será exibido ao clicar no ponto (popup) e o ícone que será exibido no ponto (icon). No caso, o popup é o nome da escola e o ícone é um ícone de escola. Em seguida, usamos a função add_to() para adicionar o ponto ao mapa.

    for idx, row in gdf.iterrows():
        if not pd.isnull(row['geometry']):
            folium.Marker(location=[row.geometry.y, row.geometry.x], popup=row['NO_ENTIDADE']).add_to(m)



**Explicando linha por linha**

>for index, row in gdf.iterrows():: 
Este é um loop for que itera pelas linhas de um DataFrame chamado gdf. Cada iteração do loop associa um índice (geralmente um número inteiro) a uma linha do DataFrame. O row representa uma linha de dados no DataFrame.

>if not pd.isnull(row['geometry']):: 
Este é um teste condicional que verifica se o valor da coluna 'geometry' na linha atual não é nulo (ou seja, se não é um valor NaN). Isso é feito usando a função pd.isnull() da biblioteca Pandas. O objetivo é verificar se há dados válidos na coluna 'geometry'.

>folium.Marker(location=[row.geometry.y, row.geometry.x], popup=row['NO_ENTIDADE']).add_to(m): 
Se o teste condicional for verdadeiro (ou seja, se a coluna 'geometry' contiver dados válidos), este código cria um marcador no mapa usando a biblioteca Folium. O marcador é posicionado nas coordenadas geográficas [row.geometry.y, row.geometry.x], que são obtidas da coluna 'geometry' do DataFrame gdf. O texto do popup é definido como o valor da coluna 'NO_ENTIDADE' da linha atual do DataFrame. O marcador é então adicionado ao objeto m.

Também podemos configurar nosso mapa de diferentes maneiras. Para isso, podemos consultar a documentação da biblioteca folium. Por exemplo, se quiser mudar o tipo do marcador, podemos alterar nosso código para:

    for idx, row in gdf.iterrows():
        if not pd.isnull(row['geometry']):
            folium.Marker(location=[row.geometry.y, row.geometry.x], popup=row['NO_ENTIDADE'], icon=folium.Icon(color='blue', icon='school', prefix='fa')).add_to(m)

Agora, vamos salvar o mapa em um arquivo HTML. Para isso, usamos a função save() da biblioteca folium. Os argumentos da função são o nome do arquivo (filename) e o argumento close_file=True para fechar o arquivo após salvar.

    m.save('mapa_escolas_uberlandia.html', close_file=True)

Também podemos salvar o mapa em um arquivo shp. Para isso, usamos a função to_file() da biblioteca geopandas. Os argumentos da função são o nome do arquivo (filename) e o argumento encoding='iso-8859-1' para definir o tipo de codificação.

    gdf.to_file('mapa_escolas_uberlandia.shp', encoding='iso-8859-1')

**Pronto, agora já temos um mapa com a localização das escolas de Uberlândia.**

### Parte 4.a - O código completo

    Assim, nosso código completo ficará da seguinte forma:

    # Etapa 1: Importe as bibliotecas necessárias
    import pandas as pd  # Para manipulação de dados
    import geopandas as gpd  # Para dados geoespaciais
    import folium  # Para criar mapas
    from geopy.geocoders import Nominatim  # Para geocodificação de endereços
    from shapely.geometry import Point  # Para trabalhar com geometrias

    # Etapa 2: Carregue seus dados em um DataFrame
    # Substitua 'seu_arquivo.csv' pelo caminho para o seu arquivo de dados (por exemplo, um arquivo CSV)
    df_mun_func = pd.read_csv('E:/GitHub/UFU_MAPPERS/microdados/dados/microdados_uberlandia_em_funcionamento_reduzido.csv', delimiter=';',
                            encoding='iso-8859-1', low_memory=False)

    # Etapa 3: Crie uma função de geocodificação usando Geopy
    def geocode_address(endereco):
        geolocalizador = Nominatim(user_agent="uberlandia_locator")  # Crie um geocodificador
        localizacao = geolocalizador.geocode(endereco)  # Obtenha coordenadas a partir do endereço
        if localizacao:
            return Point(localizacao.longitude, localizacao.latitude)  # Retorne como um Ponto
        else:
            return None  # Retorne Nenhum se a geocodificação falhar

    # Etapa 4: Crie uma nova coluna 'full_address' com o endereço combinado
    df_mun_func['full_address'] = 'Brasil' + ', ' + 'MG' + ', ' + df_mun_func['NO_MUNICIPIO'] + ', ' + df_mun_func['DS_ENDERECO'] + ', ' + df_mun_func['NU_ENDERECO']

    # Etapa 5: Aplique a função de geocodificação para criar uma coluna 'geometry'
    df_mun_func['geometry'] = df_mun_func['full_address'].apply(geocode_address)

    # Etapa 6: Crie um GeoDataFrame a partir do DataFrame
    gdf = gpd.GeoDataFrame(df_mun_func, geometry='geometry')

    # Etapa 7: Crie um mapa usando o Folium e adicione marcadores para as localizações dos edifícios
    # Substitua 'latitude' e 'longitude' pelas coordenadas desejadas para o centro do mapa
    # No caso de Uberlândia, as coordenadas são: -18.9186, -48.2772
    centro_mapa = (-18.9186, -48.2772)
    m = folium.Map(location=centro_mapa, zoom_start=13)

    print(gdf.head(40))

    # Percorra cada linha no GeoDataFrame e adicione um marcador para cada edifício
    for idx, linha in gdf.iterrows():
        if not pd.isnull(linha['geometry']):
            folium.Marker(location=[linha.geometry.y, linha.geometry.x], popup=linha['NO_ENTIDADE']).add_to(m)

    # Etapa 8: Salve o mapa como um arquivo HTML ou exiba-o em um Jupyter Notebook
    m.save('E:/GitHub/UFU_MAPPERS/microdados/dados/building_locations_map.html')

    # O arquivo HTML resultante conterá um mapa com marcadores para as localizações dos edifícios.


### Parte 4.b - Brincando com o mapa (estilos e cores)

O mapa gerado com o código fornecido apresenta um estilo bastante tradicional de visualização. No entanto, é possível alterar o estilo do mapa, dos marcadores e dos textos de descrição dos marcadores. Para isso, podemos consultar a documentação da biblioteca folium. 


Por exemplo, se quisermos mudar o tipo do marcador, podemos alterar nosso código para:

    for idx, row in gdf.iterrows():
        if not pd.isnull(row['geometry']):
            folium.Marker(location=[row.geometry.y, row.geometry.x], popup=row['NO_ENTIDADE'], icon=folium.Icon(color='blue', icon='school', prefix='fa')).add_to(m)




