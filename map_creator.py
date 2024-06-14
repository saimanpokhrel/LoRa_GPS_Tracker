import folium

def create_map(lat, lon):
    map = folium.Map(location=[lat, lon], zoom_start=15)
    folium.Marker([lat, lon], popup="GPS Location").add_to(map)
    map.save("static/map.html")
