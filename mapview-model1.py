from kivy_garden.mapview import MapView, MapMarker, MapSource
from kivy.app import App

class MapviewTest(App):
    def build(self):
        apiKey = 'c7b23514f42f4878b7a8397f7ecfdef5'
        source = MapSource(url='https://tile.thunderforest.com/landscape/{z}/{x}/{y}.png?apikey=c7b23514f42f4878b7a8397f7ecfdef5',
                           cache_key="thunderforest-map", tile_size=512,
                           image_ext="png", attribution="@ThunderForest")

        mapview = MapView(zoom=20, lat=47.28577789414191, lon=11.14638256730083)
        mapview.map_source.from_provider("thunderforest-cycle")
        mapview.map_source = source
        m1 = MapMarker(lat=47.28577789414191, lon=11.14638256730083)
        mapview.add_marker(m1)
        return mapview



MapviewTest().run()


