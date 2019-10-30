import folium
import pandas as pd
import Icon_color

df=pd.read_json("pk.json")
#columns in df ['city', 'admin', 'country', 'population_proper', 'iso2', 'capital','lat', 'lng', 'population']

#Name of city save into cityname
cityname=list(df["city"])

#latitude
lat=list(df["lat"])

#longitude
long=list(df["lng"])

#Capital
capital=list(df["capital"])
#set Map to Main location
map=folium.Map(location=[30.3753, 69.3451],zoom_start=6)#add ,tiles="Mapbox bright"

#city points
fgc=folium.FeatureGroup(name="city_points")


for lat,long,city,cap in zip(lat,long,cityname,capital):
    #for circle icon
    fgc.add_child(folium.CircleMarker(location=[lat,long],radius=6,popup=str(city),fill=True,fill_color=Icon_color.color(cap),color="gray",fill_opacity=0.7))
    #for location icon
    # fgc.add_child(folium.Marker(location=[lat, long],popup=str(city),icon=folium.Icon(color=Icon_color.color(cap))))

#adding Polygon
fgp=folium.FeatureGroup(name="Population")
data=open("PolygonWorld.json","r",encoding="utf-8-sig").read()
fgp.add_child(folium.GeoJson(data=data,style_function=lambda x:{"fillColor":"yellow" if x["properties"]["POP2005"]<100000000
else "orange" if x["properties"]["POP2005"]>100000000 or x["properties"]["POP2005"]<150000000
else "red"}))

map.add_child(fgc)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map.html")