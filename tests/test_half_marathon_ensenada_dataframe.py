from typer.testing import CliRunner
import os
from ..src.half_marathon_ensenada_dataframe import app

runner = CliRunner()


def test_half_marathon_ensenada_dataframe():
    csv_path = "data/processed/half_maraton_ensenada.csv"
    if os.path.exists(csv_path):
        os.remove(csv_path)
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert os.path.exists(csv_path)