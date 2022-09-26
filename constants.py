from pathlib import Path


BASE_DIR: Path = Path(__file__).absolute().parent
DATA_DIR: Path = BASE_DIR.joinpath("data")
