from running_analysis import read_gpx_file, get_gpx_segment_points


def test_read_gpx_file():
    gpx_path = "data/medio_maraton_ensenada.gpx"
    gpx_object = read_gpx_file(gpx_path)
    obtained_number_of_tracks = gpx_object.get_track_points_no()
    expected_number_of_tracks = 1730
    assert obtained_number_of_tracks == expected_number_of_tracks

def test_get_segemnt_points():
    gpx_path = "data/medio_maraton_ensenada.gpx"
    gpx_object = read_gpx_file(gpx_path)
    obtained_gpx_point = get_gpx_segment_points(gpx_object)[0]
    obtained_latitude_gpx_point = obtained_gpx_point.latitude
    expected_latitude_gpx_point = 31.843262
    assert obtained_latitude_gpx_point == expected_latitude_gpx_point
