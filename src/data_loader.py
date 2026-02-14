import pandas as pd

def load_stock_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["Date"])
    df.set_index("Date", inplace=True)
    return df.sort_index()
