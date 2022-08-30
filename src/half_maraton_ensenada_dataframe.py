from running_analysis import get_route_dataframe

gpx_path = "data/gpx/medio_maraton_ensenada.gpx"
route_dataframe = get_route_dataframe(gpx_path)
route_dataframe.to_csv("data/processed/half_maraton_ensenada.csv", index=False)