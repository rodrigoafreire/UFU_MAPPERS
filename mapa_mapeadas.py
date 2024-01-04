import folium
from folium.plugins import Search

# Criar um mapa base com Folium
mapa = folium.Map(location=[-18.9186, -48.2772], zoom_start=12, tiles='cartodbpositron')

# Caminho para o arquivo GeoJSON
geojson_path = 'E:/GitHub/UFU_MAPPERS/Arquivos_de_Suporte/GEOJSON/Edificacoes_escolas_mapeadas.geojson'

# Função para exibir o nome da escola no popup
def add_popup(feature):
    if 'name' in feature['properties']:
        return feature['properties']['name']
    return 'Sem Nome'

# Adicionar o GeoJSON ao mapa
camada_geojson = folium.GeoJson(
        open(geojson_path, encoding='utf-8-sig').read(),
        name='geojson',
        tooltip=folium.GeoJsonTooltip(fields=['name'], aliases=['Escola: ']),
        popup=folium.GeoJsonPopup(fields=['name'], aliases=['Escola: '])
    ).add_to(mapa)

# Add a search tool to the map
search = Search(
    layer=camada_geojson,
    geom_type='MultiPolygon',
    placeholder="Busque uma Escola (Iniciar com E E, EMEI, E M, etc.)",
    collapsed=False,
    weight=3,
    search_label='name'  # This should be the property name in your GeoJSON file that contains the school names
).add_to(mapa)

# Salvar o mapa em um arquivo HTML
mapa.save('mapa_folium_escolas.html')

print("Mapa salvo como 'mapa_folium_escolas.html'")
