from running_analysis import (
    get_route_dataframe,
    get_speed_in_meters_per_second,
    get_distance_in_meters_from_geographic_point,
    get_time,
    get_speed_from_dataframe,
)


gpx_path = "data/gpx/medio_maraton_ensenada.gpx"
route_dataframe = get_route_dataframe(gpx_path)

initial_point = route_dataframe.iloc[3]
final_point = route_dataframe.iloc[4]

def test_get_speed_from_dataframe():
    obtained_speed = get_speed_from_dataframe(route_dataframe)
    obtained_length_speed_dataframe = len(obtained_speed)
    expected_length_speed_dataframe = 1730
    assert obtained_length_speed_dataframe == expected_length_speed_dataframe

def test_get_speed_in_meters_per_second():
    obtained_speed = get_speed_in_meters_per_second(initial_point, final_point)
    expected_speed = 14.695700224768062/1.0
    assert obtained_speed == expected_speed

def test_get_distance_in_meters_from_geographic_point():
    obtained_distance = get_distance_in_meters_from_geographic_point(initial_point, final_point)
    expected_distance = 14.695700224768062
    assert obtained_distance == expected_distance

def test_get_time():
    obtained_time = get_time(initial_point, final_point)
    expected_time = 1.0
    assert obtained_time == expected_time
