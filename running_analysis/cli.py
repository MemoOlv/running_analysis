from running_analysis.read_gpx_file import write_route_csv
import typer

app = typer.Typer()

@app.command()
def write_csv(
    gpx_path: str = typer.Argument(),
    csv_path: str = typer.Argument(),
):
    write_route_csv(gpx_path, csv_path)

@app.command()
def dummy_command():
    print("Hey there, I'm an accesory")
