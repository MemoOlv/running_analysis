from running_analysis import (
    get_route_dataframe,
    get_speed,
    get_distance_in_meters_from_geographic_point,
    get_time,
)


gpx_path = "data/gpx/medio_maraton_ensenada.gpx"
route_dataframe = get_route_dataframe(gpx_path)


def test_get_speed():
    obtained_speed = get_speed(route_dataframe)
    expected_speed = 4
    assert obtained_speed == expected_speed


def test_get_distance_in_meters_from_geographic_point():
    initial_point = route_dataframe.iloc[3]
    final_point = route_dataframe.iloc[4]
    obtained_distance = get_distance_in_meters_from_geographic_point(initial_point, final_point)
    expected_distance = 14.695700224768062
    assert obtained_distance == expected_distance

def test_get_time():
    initial_point = route_dataframe.iloc[3]
    final_point = route_dataframe.iloc[4]
    obtained_time = get_time(initial_point, final_point)
    expected_time = 4
    assert obtained_time == expected_time
