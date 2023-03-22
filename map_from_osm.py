import folium
import osmnx as ox

style1 = {'fillColor': 'red', 'color': 'red'}

place = 'Uberlandia, Minas Gerais, Brazil'

m = folium.Map([-18.9146, -48.2754], zoom_start=10, tiles='CartoDb dark_matter')

tags_building = {'building':True}
building = ox.geometries_from_place(place, tags_building, buffer_dist=1000)
buildings = building[building.geom_type == 'Polygon']
folium.GeoJson(buildings, style_function=lambda x:style1).add_to(m)


graph = ox.graph_from_place(place, network_type='drive')
nodes, streets = ox.graph_to_gdfs(graph)
streets = ox.folium.plot_graph_folium(graph, graph_map=m)

popup_text = """
<h4>UFU Mappers</h4>
<p></p>
<img src="C:/Users/rodri/Downloads/Logotipo_2.png" width="100%" height="100%">
"""
popup = folium.Popup(html=popup_text, max_width=300)

folium.Marker(
    location=[-18.91843, -48.25575],
    icon=folium.Icon(color='blue', icon='circle', size=(5,5)),
    tooltip='Uberlandia, MG - Brazil',
    popup=popup
).add_to(m)



m.save('cafes.html')