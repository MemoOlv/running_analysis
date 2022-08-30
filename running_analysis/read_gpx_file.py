import gpxpy

def read_gpx_file(gpx_file_path):
    with open(gpx_file_path) as gpx_file:
        gpx = gpxpy.parse(gpx_file)
    return gpx