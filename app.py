from kivy_garden.mapview import MapView, MapMarkerPopup
from kivy.app import App
from kivy.uix.button import Button

IBK_LAT = 47.2645632
IBK_LONG = 11.3873967

data = [
    {"fname": "Michael", "lname": "Kohlegger", "dname": "Olli", "kind": "Duck Tolling Retriever", "lat":47.271505, "long":11.3957557},
    {"fname": "Heidi", "lname": "Mustermann", "dname": "Orlando", "kind": "Corgy", "lat":47.28318, "long":11.4058351},
    {"fname": "Paul", "lname": "Berger", "dname": "Sissy", "kind": "Huskey", "lat":47.270127, "long":11.3849021},
    {"fname": "Rita", "lname": "Mair", "dname": "Bello", "kind": "German Sheppard", "lat":47.257723, "long":11.3712541}
]

class MapViewApp(App):
    def build(self):

        mapview = MapView(zoom=13, lat=IBK_LAT, lon=IBK_LONG)

        def callback(instance):
            print('The button <%s> is being pressed' % instance.text)

        for item in data:

            marker = MapMarkerPopup(
                lon=item["long"],
                lat=item["lat"]
            )

            button = Button(
                text=f"[b]{item["fname"]} {item["lname"]}[/b]\nmit {item["kind"]} {item["dname"]}",
                halign="center",
                background_color=(255,255,255),
                color=(0,0,0),
                size_hint=(2.5,0.5),
                markup=True
            )

            button.bind(on_press=callback)

            marker.add_widget(
                button,
            )

            mapview.add_widget(marker)

        return mapview

MapViewApp().run()