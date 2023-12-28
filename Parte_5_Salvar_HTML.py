import pandas as pd
import geopandas as gpd
import folium

# Carregar o GeoDataFrame já salvo em SHP
gdf = gpd.read_file('E:/GitHub/UFU_MAPPERS/microdados/SHP/UDI_em_funcionamento_publicas.shp')

# Crie um mapa usando Folium e adicione marcadores para os locais dos prédios
# Substitua 'latitude' e 'longitude' pelas coordenadas do centro do mapa desejado
# No caso de Uberlandia, as coordenadas são: -18.9186, -48.2772
map_center = (-18.9186, -48.2772)
m = folium.Map(location=map_center, zoom_start=13)

# Nesse exemplo, vamos criar cores diferentes para as escolas de forma aleatoria, mas você pode criar cores diferentes para cada escola de acordo com o atributo desejado.
# Por exemplo, você pode criar cores de acordo com o tipo de escola (municipal, estadual, federal, etc) ou de acordo com o número de alunos matriculados.
# Passo 1: Determine o número de subconjuntos e calcule o tamanho aproximado de cada subconjunto
num_subsets = 7
subset_size = len(gdf) // num_subsets
remaining_locations = len(gdf) % num_subsets

# Passo 2: Defina cores únicas para cada subconjunto
colors = ['red', 'blue', 'green', 'orange', 'purple', 'pink', 'cadetblue']# Adicione mais cores conforme necessário

# Atribuir as cores para os mapeadores
Atrs = ['Rodrigo', 'Mauricio', 'Bento', 'Deborah', 'Iago', 'Maria Cecilia', 'Renato']

start_idx = 0

for i in range(num_subsets):
    subset_end = start_idx + subset_size
    if i < remaining_locations:
        subset_end += 1

    subset = gdf[start_idx:subset_end]
    color = colors[i]
    Atr = Atrs[i]
    subset.to_file('E:/GitHub/UFU_MAPPERS/microdados/SHP/UDI_em_funcionamento_publicas_' + str(i) + '_'+ Atr + '.shp', driver='ESRI Shapefile')

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
    m.save('E:/GitHub/UFU_MAPPERS/microdados/dados/Escolas_Publicas_'+ Atr + '.html')

# Step 8: Salvar o mapa em HTML para visualização. Colocar o  caminho do arquivo desejado.
m.save('E:/caminho/Meu_mapa.html')

# O mapa resultante em HTML conterá marcadores para os locais dos prédios.

