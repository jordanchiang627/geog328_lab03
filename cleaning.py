import geopandas as gpd

# flake8: noqa

ca_earth = gpd.read_file('assets/california-earthquakes.geojson')
print(ca_earth.head(5))

ca_earth = ca_earth[ca_earth['year'] > 1999]
print(ca_earth.head())

ca_earth.to_file("assets/caearthquakes.geojson", driver = "GeoJSON")