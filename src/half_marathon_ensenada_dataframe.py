from running_analysis import write_route_csv
import typer

app = typer.Typer()

default_gpx_path = "data/gpx/medio_maraton_ensenada.gpx"
default_csv_path = "data/processed/half_maraton_ensenada.csv"

@app.command()
def write_csv(gpx_path: str = typer.Argument(default_gpx_path), csv_path: str = typer.Argument(default_csv_path)):
    write_route_csv(gpx_path, csv_path)

if __name__ == "__main__":
    app()
    