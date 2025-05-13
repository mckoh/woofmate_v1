import folium

IBK_LONG = 47.2645632
IBK_LAT = 11.3873967

data = [
    {"fname": "Michael", "lname": "Kohlegger", "dname": "Olli", "kind": "Duck Tolling Retriever", "geo": [47.271505,11.3957557]},
    {"fname": "Heidi", "lname": "Mustermann", "dname": "Orlando", "kind": "Corgy", "geo": [47.28318,11.4058351]},
    {"fname": "Paul", "lname": "Berger", "dname": "Sissy", "kind": "Huskey", "geo": [47.270127,11.3849021]},
    {"fname": "Rita", "lname": "Mair", "dname": "Bello", "kind": "German Sheppard", "geo": [47.257723,11.3712541]}
]

map = folium.Map(
    location=[IBK_LONG, IBK_LAT],
    #width="50%",
    #height="50%",
    zoom_start=14,
    tiles="OpenStreetMap",
    zoom_control=True
)

dog_icon = folium.Icon(
    color='red',
    icon_color='white',
    prefix="fa",
    icon='paw',
    angle=0
)

for person in data:
    marker = folium.Marker(
        location=person["geo"],
        popup=f"{person["fname"]} {person["lname"]} with {person["kind"]} {person["dname"]}",
        tooltip=f"{person["fname"]} {person["lname"]} with {person["kind"]} {person["dname"]}",
        icon=dog_icon,
        draggable=False
    )

    marker.add_to(map)

map.save("index.html")

