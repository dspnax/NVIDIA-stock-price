import argparse
import pandas as pd
import matplotlib.pyplot as plt

from data_loader import load_stock_data
from returns import compute_log_returns
from volatility import rolling_volatility
from statistics import normality_test, stationarity_test
from config import WINDOW_SIZE, DATA_PATH, OUTPUT_PATH
from logger import setup_logger


def run_pipeline(plot: bool = False, save: bool = False):
    logger = setup_logger()
    logger.info("Starting pipeline...")

    # Load data
    df = load_stock_data(DATA_PATH)
    logger.info("Data loaded")

    # Compute returns
    returns = compute_log_returns(df["Price"])
    df = df.loc[returns.index]
    df["Log Return"] = returns
    logger.info("Log returns computed")

    # Volatility
    df["Volatility"] = rolling_volatility(df["Log Return"], WINDOW_SIZE)
    logger.info("Volatility computed")

    # Stats
    p_norm = normality_test(df["Log Return"])
    p_adf = stationarity_test(df["Log Return"])

    logger.info(f"Normality p-value: {p_norm:.6f}")
    logger.info(f"ADF p-value: {p_adf:.6f}")

    # Save results
    if save:
        df.to_csv(OUTPUT_PATH)
        logger.info(f"Results saved to {OUTPUT_PATH}")

    # Plot
    if plot:
        plt.figure()
        plt.plot(df["Price"])
        plt.title("Price")
        plt.grid()

        plt.figure()
        plt.plot(df["Volatility"])
        plt.title("Volatility")
        plt.grid()

        plt.show()

    logger.info("Pipeline completed")


def main():
    parser = argparse.ArgumentParser(description="NVIDIA Stock Analysis CLI")

    parser.add_argument("--plot", action="store_true", help="Show plots")
    parser.add_argument("--save", action="store_true", help="Save results")

    args = parser.parse_args()

    run_pipeline(plot=args.plot, save=args.save)


if __name__ == "__main__":
    main()
    