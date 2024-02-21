from kivy_garden.mapview import MapView, MapMarker, MapSource
import geocoder
currentGeocoder = geocoder.ip('me')
latitude, longitude = currentGeocoder.latlng

class ZequentMapView(MapView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        currLat =  latitude
        currLon = longitude
        self.zoom=20
        self.lat=currLat
        self.lon=currLon
        apiKey = 'c7b23514f42f4878b7a8397f7ecfdef5'
        source = MapSource(url='https://tile.thunderforest.com/landscape/{z}/{x}/{y}.png?apikey='+apiKey,
                            cache_key="thunderforest-map", tile_size=512,
                            image_ext="png", attribution="@ThunderForest")
        self.map_source.from_provider("thunderforest-cycle")
        self.map_source = source