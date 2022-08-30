import gpxpy


def read_gpx_file(gpx_path):
    with open(gpx_path) as gpx_file:
        gpx_object = gpxpy.parse(gpx_file)
    return gpx_object

def get_gpx_segment_points(gpx_object):
    return gpx_object.tracks[0].segments[0].points