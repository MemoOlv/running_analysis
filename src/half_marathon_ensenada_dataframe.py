from running_analysis import get_route_dataframe
import typer

app = typer.Typer()

default_gpx_path = "data/gpx/medio_maraton_ensenada.gpx"
default_csv_path = "data/processed/half_maraton_ensenada.csv"

@app.command()
def write_route_csv(gpx_path: str = typer.Argument(default_gpx_path), csv_path: str = typer.Argument(default_csv_path)):
    route_dataframe = get_route_dataframe(gpx_path)
    route_dataframe.to_csv(csv_path, index=False)

if __name__ == "__main__":
    app()
    