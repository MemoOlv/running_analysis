import numpy as np
from geopy import distance


def get_pace_from_speed(route_dataframe):
    route_dataframe_with_speed = add_speed_to_dataframe(route_dataframe)
    route_dataframe_with_speed["pace"] = (100 / 6) * (1 / route_dataframe_with_speed["speed"])
    return route_dataframe_with_speed


def add_speed_to_dataframe(route_dataframe):
    list_of_speeds = get_speed_from_dataframe(route_dataframe)
    list_of_speeds.insert(0, 0)
    route_dataframe["speed"] = list_of_speeds
    return route_dataframe


def get_speed_from_dataframe(route_dataframe):
    return [
        get_speed_in_meters_per_second(route_dataframe.iloc[i], route_dataframe.iloc[i + 1])
        for i in range(len(route_dataframe) - 1)
    ]


def get_speed_in_meters_per_second(initial_point, final_point):
    distance = get_distance_in_meters_from_geographic_point(initial_point, final_point)
    time = get_time(initial_point, final_point)
    return distance / time


def get_distance_in_meters_from_geographic_point(initial_point, final_point):
    initial_point_lat_lon = initial_point[["latitude", "longitude"]]
    final_point_lat_lon = final_point[["latitude", "longitude"]]
    initia_point_elevation = initial_point["elevation"]
    final_point_elevation = final_point["elevation"]
    distance_2d = distance.distance(initial_point_lat_lon, final_point_lat_lon).m
    distance_3d = np.sqrt(distance_2d**2 + (final_point_elevation - initia_point_elevation) ** 2)
    return distance_3d


def get_time(initial_point, final_point):
    return (final_point["time"] - initial_point["time"]).total_seconds()
