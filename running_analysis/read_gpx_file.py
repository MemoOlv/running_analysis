import gpxpy


def read_gpx_file(gpx_path):
    with open(gpx_path) as gpx_file:
        gpx_object = gpxpy.parse(gpx_file)
    return gpx_object

def get_gpx_segment_points(gpx_object):
    return gpx_object.tracks[0].segments[0].points

def get_route_list_of_dictionaries(gpx_points):
    return [{"latitude": point.latitude, "longitude": point.longitude, "elevation": point.elevation, "time": point.time} for point in gpx_points]
