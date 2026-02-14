import pandas as pd
from scipy.stats import shapiro
from statsmodels.tsa.stattools import adfuller # type: ignore

def rolling_volatility(returns: pd.Series, window: int = 30) -> pd.Series:
    return returns.rolling(window).std()

def normality_test(returns: pd.Series):
    stat, p_value = shapiro(returns)
    return p_value

def stationarity_test(returns: pd.Series):
    result = adfuller(returns)
    return result[1]  
