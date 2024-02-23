from kivy_garden.mapview import MapView, MapMarker, MapSource
import geocoder
currentGeocoder = geocoder.ip('me')
from kivymd.app import MDApp



class ZequentMapView(MapView):

   
    app=MDApp.get_running_app()
    latitude = 48
    longitude = 48
   
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.zoom=20
        apiKey = 'c7b23514f42f4878b7a8397f7ecfdef5'
        source = MapSource(url='https://tile.thunderforest.com/landscape/{z}/{x}/{y}.png?apikey='+apiKey,
                            cache_key="thunderforest-map", tile_size=512,
                            image_ext="png", attribution="@ThunderForest")
        self.map_source.from_provider("thunderforest-cycle")
        self.map_source = source
        self.updateMap()
        
    
    def updateMap(self):
        latitude = 48
        longitude = 48

        if(self.app is not None ):
            latitude = self.app.latitude
            longitude = self.app.longitude
            
        self.center_on(latitude, longitude)

    def on_touch_down(self, touch):
        self.app=MDApp.get_running_app()
        print(self.lat)
        self.updateMap()
        return super().on_touch_down(touch)
    
    def build(self):
        pass