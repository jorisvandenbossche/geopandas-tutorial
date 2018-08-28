# calculating the relative number of bike stations by area
districts2['n_bike_stations_by_area'] = (
    districts2['n_bike_stations'] / districts2.geometry.area)