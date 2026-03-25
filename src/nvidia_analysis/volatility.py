import pandas as pd

def rolling_volatility(returns: pd.Series, window: int = 30) -> pd.Series:
    """
    Compute rolling volatility (standard deviation) of returns.
    """
    return returns.rolling(window=window).std()