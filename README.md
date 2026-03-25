# NVIDIA Stock Time-Series Analysis

## Overview

This project implements a modular pipeline for analyzing NVIDIA stock price dynamics using statistical time-series methods.

The system is designed with a focus on:

* log-return transformations
* volatility estimation
* statistical inference
* reproducible pipelines

## Features

* Log-return computation (time-additive transformation)
* Rolling volatility analysis
* Normality testing (Shapiro–Wilk)
* Stationarity testing (ADF)
* CLI-based execution
* Modular package structure

## Installation

### Option 1: Install as a package (recommended)

```bash
pip install -e .
```

### Option 2: Install dependencies manually

```bash
pip install -r requirements.txt
```

## Usage

```bash
python -m nvidia_analysis.main --plot --save
```

## Project Structure

```
src/nvidia_analysis/
    data_loader.py
    returns.py
    volatility.py
    statistics.py
    main.py
```

## Methodology

We transform raw prices into log-returns to ensure:

* additivity over time
* variance stabilization

Volatility is modeled using rolling standard deviation, while statistical tests assess:

* distribution properties
* stationarity of the time series

## Applications

Although focused on financial data, the methodology extends to:

* anomaly detection
* intrusion detection systems
* behavioral pattern analysis

## Author

dspnax
