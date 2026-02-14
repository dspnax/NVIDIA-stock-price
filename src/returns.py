import numpy as np
import pandas as pd

def log_returns(price_series: pd.Series) -> pd.Series:
    """
    Compute log-returns to ensure time additivity and variance stability.
    """
    return np.log(price_series / price_series.shift(1)).dropna()
