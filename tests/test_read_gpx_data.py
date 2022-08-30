from running_analysis import read_gpx_file

def test_read_gpx_file():
    gpx_file_path = "data/medio_maraton_ensenada.gpx"
    obtained_gpx = read_gpx_file(gpx_file_path)
    obtained_number_of_tracks = obtained_gpx.get_track_points_no()
    expected_number_of_tracks = 835
    assert obtained_number_of_tracks == expected_number_of_tracks