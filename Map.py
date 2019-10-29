import folium
import pandas as pd

map=folium.Map(location=[30.3753, 69.3451],zoom_start=6)
fg=folium.FeatureGroup(name="PakistanMap")
fg.add_child(folium.Marker(location=[30.3753, 69.3451],popup="shami",icon=folium.Icon(color="green")))
map.add_child(fg)
map.save("map.html")