import numpy as np

from geopy import distance


def get_speed_from_dataframe(route_dataframe):
    return route_dataframe

def get_speed(initial_point, final_point):
    distance = get_distance_in_meters_from_geographic_point(initial_point, final_point)
    time = get_time(initial_point, final_point)
    return distance/time


def get_distance_in_meters_from_geographic_point(initial_point, final_point):
    initial_point_lat_lon = initial_point[:2]
    initia_point_elevation = initial_point[2]
    final_point_elevation = final_point[2]
    final_point_lat_lon = final_point[:2]
    distance_2d = distance.distance(initial_point_lat_lon, final_point_lat_lon).m
    distance_3d = np.sqrt(distance_2d**2 + (final_point_elevation - initia_point_elevation) ** 2)
    return distance_3d

def get_time(initial_point, final_point):
    return (final_point.time - initial_point.time).total_seconds()
