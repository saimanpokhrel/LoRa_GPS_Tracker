import folium
def create_map(lat, lon):
    map_obj = folium.Map(location=[lat, lon], zoom_start=15)
    folium.Marker([lat, lon], popup="GPS Location").add_to(map_obj)
    map_obj.save("static\map.html")
