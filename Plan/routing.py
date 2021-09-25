###### we create a  routing algorithim ########
##### we import the necessary modules ######



#### we will use folium for osmnx networkx for routing in gui pyqt5



try:
    import logging
    import geocoder
    from geopy.geocoders import Nominatim
    import numpy as np
    import pandas as pd
    import geopandas as gpd
    from shapely.geometry import Point, LineString
    import plotly_express as px
    import networkx as nx
    import osmnx as ox

    ox.config(use_cache=True, log_console=True)

except ImportError:
    logging.error("Theres a problem importing the current modules")

##### we use certain global variables
CURRENT_COORDINATES = geocoder.ip('me')


class routing:
    def __init__(self, location: str, distance: int, transport_mode: str, loc_type="address", coordinnates=CURRENT_COORDINATES.latlng,) -> None:
        self.loc = location
        self.dist = distance
        self.coordinate = coordinnates
        self.transport_mode = transport_mode
        self.loc_type = loc_type

    def create_graph(self):
        """Transport mode = ‘walk’, ‘bike’, ‘drive’, ‘drive_service’, ‘all’, ‘all_private’, ‘none’"""
        if self.loc_type == "address":
                G = ox.graph_from_address(self.loc, dist=self.dist, network_type=self.transport_mode)
        elif self.loc_type == "points":
                G = ox.graph_from_point(self.loc, dist=self.dist, network_type=self.transport_mode )
        return G

if __name__  == '__main__':
    #### this is only for debugging purposes
    routing = routing('nairobi', 2500, 'drive')
