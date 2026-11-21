from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).parent / "modelling" / "data"


def load_data(data_dir=DATA_DIR):
    """Load all data/<country>/<league>/<season>.csv files into one DataFrame."""
    frames = {}
    for path in sorted(Path(data_dir).glob("*/*/*.csv")):
        df = pd.read_csv(path)
        # a few files have trailing commas in the header -> empty "Unnamed" columns
        df = df.loc[:, ~df.columns.str.startswith("Unnamed")]
        # key = (country, league, season), e.g. season "1920" = 2019/20
        frames[path.parts[-3], int(path.parts[-2]), path.stem] = df

    # .copy() consolidates the result (read_csv returns one block per column)
    data = pd.concat(frames, names=["country", "league", "season"]).copy()
    data = data.reset_index(["country", "league", "season"]).reset_index(drop=True)
    data["Date"] = pd.to_datetime(data["Date"], dayfirst=True)
    return data


if __name__ == "__main__":
    data = load_data()
    print(data.shape)
    print(data.head())
