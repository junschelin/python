import json
import plotly.express as px

#json.load : file 처리
#json.loads : str -> dict, dict -> str

mag = []
lat = []
lon = []

with open('./book_ex_from_github/pcc_3e/chapter_16/mapping_global_datasets/eq_data/eq_data_1_day_m1.geojson', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for feature in data['features']:
        mag.append(feature['properties']['mag'])
        lon.append(feature['geometry']['coordinates'][0])
        lat.append(feature['geometry']['coordinates'][1])
        
        
print(mag)
print(lat)
print(lon)

title = "Global Earthquakes"
fig = px.scatter_geo(lat=lat, lon=lon, size=mag, title=title, color=mag, labels={'color':'Magnitude'})
fig.show()