import datetime
import os
from running_analysis import (
    get_gpx_segment_points,
    get_route_dataframe,
    get_route_list_of_dictionaries,
    read_gpx_file,
    write_route_csv,
)


gpx_path = "tests/data/medio_maraton_ensenada.gpx"


def test_read_gpx_file():
    gpx_object = read_gpx_file(gpx_path)
    obtained_number_of_tracks = gpx_object.get_track_points_no()
    expected_number_of_tracks = 1730
    assert obtained_number_of_tracks == expected_number_of_tracks


def test_get_segemnt_points():
    gpx_object = read_gpx_file(gpx_path)
    obtained_gpx_point = get_gpx_segment_points(gpx_object)[0]
    obtained_latitude_gpx_point = obtained_gpx_point.latitude
    expected_latitude_gpx_point = 31.843262
    assert obtained_latitude_gpx_point == expected_latitude_gpx_point


def test_get_route_dictionary():
    obtained_dictionary = get_route_list_of_dictionaries(gpx_path)[0]
    expected_dictionary = {
        "latitude": 31.843262,
        "longitude": -116.611852,
        "elevation": 477.8,
        "time": datetime.datetime(2022, 8, 14, 0, 51),
    }
    assert obtained_dictionary["latitude"] == expected_dictionary["latitude"]
    assert obtained_dictionary["elevation"] == expected_dictionary["elevation"]
    assert isinstance(obtained_dictionary["time"], datetime.datetime)


def test_get_route_dataframe():
    obtained_route_dataframe = get_route_dataframe(gpx_path)
    obtained_route_dataframe_columns = obtained_route_dataframe.columns
    expected_route_dataframe_columns = ["latitude", "longitude", "elevation", "time"]
    assert (obtained_route_dataframe_columns == expected_route_dataframe_columns).all()


def test_write_route_csv():
    gpx_path = "tests/data/medio_maraton_ensenada.gpx"
    csv_path = "tests/data/half_maraton_ensenada.csv"
    if os.path.exists(csv_path):
        os.remove(csv_path)
    write_route_csv(gpx_path, csv_path)
    assert os.path.exists(csv_path)
