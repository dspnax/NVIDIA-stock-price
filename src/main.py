import matplotlib.pyplot as plt

from data_loader import load_stock_data
from returns import compute_log_returns
from volatility import rolling_volatility
from statistics import normality_test, stationarity_test


def main():
    # Load data
    df = load_stock_data("../data/raw/NVIDIA_Stock_Price.csv")

    # Compute log-returns
    returns = compute_log_returns(df["Price"])
    df = df.loc[returns.index]
    df["Log Return"] = returns

    # Compute volatility
    df["Volatility_30d"] = rolling_volatility(df["Log Return"], window=30)

    # Statistical tests
    p_norm = normality_test(df["Log Return"])
    p_adf = stationarity_test(df["Log Return"])

    print("Statistical Tests")
    print("-----------------")
    print(f"Normality p-value: {p_norm:.6f}")
    print(f"Stationarity (ADF) p-value: {p_adf:.6f}")

    # Plot price
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Price"], label="NVIDIA Price")
    plt.title("NVIDIA Stock Price")
    plt.grid(True)
    plt.legend()
    plt.show()

    # Plot volatility
    plt.figure(figsize=(12, 4))
    plt.plot(df.index, df["Volatility_30d"], label="30-day Volatility")
    plt.title("Rolling Volatility of Log Returns")
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
    