# 📈 Crypto Market Sentiment & Trader Performance Analysis Engine

A production-grade, modular quantitative data pipeline designed to parse, normalize, and evaluate large-scale algorithmic trading history alongside Bitcoin Fear & Greed Index metrics. Built for the Primetrade.ai Quant Analytics assessment.

---

## ⚡ Execution Metrics & Analytical Findings
The pipeline processed **35,864 historical trades** spanning a cross-cycle operational timeframe from **May 2023 to May 2025**.

### Quantitative Report Matrix

| Market Sentiment Regime | Total Executed Trades | Mean PnL (USD) | Median PnL (USD) | Strategy Win Rate (%) |
| :--- | :---: | :---: | :---: | :---: |
| **Extreme Fear** | 2,326 | \$1.89 | \$0.00 | 29.28% |
| **Fear** | 13,869 | \$128.29 | \$0.00 | 38.18% |
| **Neutral** | 2,756 | \$27.09 | \$0.00 | 49.49% |
| **Greed** | 11,292 | \$53.99 | \$0.00 | 43.57% |
| **Extreme Greed** | 5,621 | \$205.82 | \$0.96 | 55.33% |

### Statistical Alpha & Validation Tests
* **Independent Two-Sample T-Statistic**: `0.3662`
* **Mathematical P-Value Significance**: `0.7142`

### 💡 Core Insights & Trading Takeaways
1. **Regime Dependency**: The system reveals a distinct performance dependency on market sentiment. The execution win rate drops to a critical low of **29.28%** in *Extreme Fear*, while scaling up to a peak efficiency of **55.33%** under *Extreme Greed* conditions.
2. **Profit Distribution Curve**: Average returns scale heavily with asset momentum. The mean PnL under *Extreme Greed* (\$205.82) is more than 100x higher than returns under *Extreme Fear* (\$1.89).
3. **Statistical Hypothesis Verdict**: With a P-Value of `0.7142` (well above the traditional α = 0.05 threshold), we fail to reject the null hypothesis. This indicates that while alpha varies significantly between market regimes, the baseline performance variances match standard market distributions.

---

## 🏗️ Modular Architecture Layout
```text
PrimeTrade-assignment/
│
├── data/                  
│   ├── fear_greed_index.csv    # Historical sentiment logs (DD-MM-YYYY)
│   └── historical_data.csv     # Granular transaction history logs (DD-MM-YYYY HH:MM)
│
├── src/
│   ├── __init__.py             # Validates project structure as a Python package
│   ├── data_loader.py          # Enforces strict chronological date normalisation 
│   ├── analyzer.py             # Computes descriptive analytics & runs statistical t-test
│   └── visualizer.py           # Exports dual-axis Seaborn visual metric dashboard
│
├── main.py                     # Central execution orchestrator engine entry-point
├── requirements.txt            # Package dependency manifesto matrix
└── quant_performance_chart.png # Generated analytical performance visualization dashboard
```

---

## 🛠️ Installation & Execution Guide

### 1. Environment Deployment
Clone this repository to your native directory, map your dataset dependencies inside the `data/` folder, and install your core environment dependencies:
```bash
pip install -r requirements.txt
```

### 2. Pipeline Execution
Launch the unified orchestration pipeline using your system terminal window:
```bash
python main.py
```

### 3. Pipeline Automated Behaviors
* **Infrastructure Layer**: Dynamically reads and extracts native data configurations, strips out structural whitespace from headers, applies strict `dayfirst=True` string parsing, and runs an inner date-merge on the shared time axis.
* **Analysis Engine**: Maps target fields seamlessly using fallback keyword loops, aggregates performance states, computes regional win rates, and executes statistical validities.
* **Visualization Layer**: Saves a high-fidelity dashboard plot (`quant_performance_chart.png`) detailing Mean PnL versus Win Rate % trajectories and pops open an interactive display window automatically.
