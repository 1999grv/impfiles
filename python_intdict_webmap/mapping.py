import folium
import pandas as pd
from geopy.geocoders import ArcGIS

df=pd.read_csv("Volcanoes.txt")
lat=list(df["LAT"])
lon=list(df["LON"])
elev=list(df["ELEV"])

def find_color(el):
    if(el<1000):
        return "green"
    elif(el>=1000 and el<3000):
        return "orange"
    else:
        return "red"

map=folium.Map(location=[df["LAT"][0],df["LON"][0]],zoom_start=6,tiles="Stamen Terrain")
fg=folium.FeatureGroup(name="My Map")
for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius=6, popup=str(el)+" m",fill_color=find_color(el),color="grey",fill_opacity=0.7))
fg.add_child(folium.GeoJson(data=open('World.json','r', encoding='utf-8-sig').read(), style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']< 10000000 else 'orange' if 10000000 <= x['properties']['POP2005']<20000000 else 'red'}))
map.add_child(fg)
map.save("Map1.html")
