import pandas as pd
import numpy as np
from scipy import stats

def analyze_trader_behavior(df):
    """
    Computes trading performance indicators, risk multipliers, 
    and verifies pattern validity using Two-Sample Statistical testing.
    """
    # Map exact column names from your two files
    sentiment_col = 'classification'
    pnl_col = 'Closed PnL'
    
    # Strip spaces and lowercase sentiment tags to make comparisons bulletproof
    df[sentiment_col] = df[sentiment_col].astype(str).str.strip().str.lower()
    
    # Force the PnL column to numeric type in case there are string artifacts
    df[pnl_col] = pd.to_numeric(df[pnl_col], errors='coerce')
    df = df.dropna(subset=[pnl_col])
    
    print(f"[ANALYZER] Computing metrics across {len(df)} rows using column '{pnl_col}'...")
    
    # 1. Performance aggregations grouped by Market Sentiment
    summary = df.groupby(sentiment_col).agg(
        total_trades=(pnl_col, 'count'),
        mean_pnl=(pnl_col, 'mean'),
        median_pnl=(pnl_col, 'median')
    ).reset_index()
    
    # 2. Compute exact Win Rate percentage metric per sentiment environment
    win_rates = df.groupby(sentiment_col).apply(
        lambda x: (x[pnl_col] > 0).sum() / len(x) * 100 if len(x) > 0 else 0,
        include_groups=False
    ).reset_index(name='win_rate')
    
    analysis_report = pd.merge(summary, win_rates, on=sentiment_col)
    
    # 3. Statistical Validity: Isolate trading data matrices for key regimes
    # Your index sample includes Fear/Extreme Fear, which standardizes to fear keywords
    fear_mask = df[sentiment_col].str.contains('fear', na=False)
    greed_mask = df[sentiment_col].str.contains('greed', na=False)
    
    fear_pnl = df[fear_mask][pnl_col].dropna()
    greed_pnl = df[greed_mask][pnl_col].dropna()
    
    # Run an Independent Two-Sample T-Test to check noise vs actual signal
    t_stat, p_val = 0.0, 1.0
    if len(fear_pnl) > 1 and len(greed_pnl) > 1:
        t_stat, p_val = stats.ttest_ind(fear_pnl, greed_pnl, equal_var=False)
        
    return analysis_report, t_stat, p_val
