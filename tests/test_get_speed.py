from running_analysis import (
    add_speed_to_dataframe,
    get_distance_in_meters_from_geographic_point,
    get_pace_from_speed,
    get_route_dataframe,
    get_speed_from_dataframe,
    get_speed_in_meters_per_second,
    get_time,
)


gpx_path = "tests/data/medio_maraton_ensenada.gpx"
route_dataframe = get_route_dataframe(gpx_path).iloc[0:10]

initial_point = route_dataframe.iloc[3]
final_point = route_dataframe.iloc[4]


def test_add_speed_to_dataframe():
    dataframe_with_speed = add_speed_to_dataframe(route_dataframe)
    expected_first_speed = dataframe_with_speed["speed"].iloc[0]
    obtained_first_speed = 0
    assert obtained_first_speed == expected_first_speed


def test_get_pace_from_speed():
    obtained_speed = add_speed_to_dataframe(route_dataframe)
    obtained_pace = get_pace_from_speed(obtained_speed)
    obtained_length_pace_dataframe = len(obtained_pace)
    expected_length_pace_dataframe = 10
    assert obtained_length_pace_dataframe == expected_length_pace_dataframe
    obtained_first_pace = obtained_pace["pace"].iloc[3]
    expected_first_pace = 0.5621480475337237
    assert obtained_first_pace == expected_first_pace


def test_get_speed_from_dataframe():
    obtained_speed = get_speed_from_dataframe(route_dataframe)
    obtained_length_speed_dataframe = len(obtained_speed)
    expected_length_speed_dataframe = 9
    assert obtained_length_speed_dataframe == expected_length_speed_dataframe
    obtained_first_speed = obtained_speed[0]
    expected_first_speed = 1.4467392395149936
    assert obtained_first_speed == expected_first_speed
    obtained_first_speed = obtained_speed[3]
    expected_first_speed = 14.695700224768062
    assert obtained_first_speed == expected_first_speed


def test_get_speed_in_meters_per_second():
    obtained_speed = get_speed_in_meters_per_second(initial_point, final_point)
    expected_speed = 14.695700224768062 / 1.0
    assert obtained_speed == expected_speed


def test_get_distance_in_meters_from_geographic_point():
    obtained_distance = get_distance_in_meters_from_geographic_point(initial_point, final_point)
    expected_distance = 14.695700224768062
    assert obtained_distance == expected_distance


def test_get_time():
    obtained_time = get_time(initial_point, final_point)
    expected_time = 1.0
    assert obtained_time == expected_time
