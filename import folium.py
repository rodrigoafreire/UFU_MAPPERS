import folium

# create a new map centered on Uberlandia, MG - Brazil
map = folium.Map(location=[-18.9146, -48.2754], zoom_start=12)

# add a red marker to the map at the center of Uberlandia with a popup containing an image and text
popup_text = """
<h4>Uberlandia, MG - Brazil</h4>
<p>Uberlandia is a city in the state of Minas Gerais, Brazil. It is located in the Triângulo Mineiro region, and has a population of around 700,000 people.</p>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/CentrosulUdi2.jpg/1920px-CentrosulUdi2.jpg" width="100%" height="100%">
"""
popup = folium.Popup(html=popup_text, max_width=300)
folium.Marker(
    location=[-18.9146, -48.2754],
    icon=folium.Icon(color='blue', icon='star'),
    tooltip='Uberlandia, MG - Brazil',
    popup=popup
).add_to(map)

# save the map as an HTML file
map.save('map.html')