import pandas as pd

def load_and_merge_data(sentiment_path, historical_path):
    """
    Loads trade history and market sentiment data, parses diverse datetime strings,
    isolates clean calendar dates, and inner-merges on the common timeline.
    """
    df_sentiment = pd.read_csv(sentiment_path)
    df_trades = pd.read_csv(historical_path)
    
    # Strip whitespace from all column headers immediately
    df_sentiment.columns = df_sentiment.columns.str.strip()
    df_trades.columns = df_trades.columns.str.strip()
    
    # Target columns based on your sample layouts
    sent_date_col = 'date' if 'date' in df_sentiment.columns else df_sentiment.columns[0]
    trade_time_col = 'Timestamp IST' if 'Timestamp IST' in df_trades.columns else 'Timestamp'
    
    # Enforce dayfirst=True for both files to parse DD-MM-YYYY correctly
    df_sentiment['Join_Date'] = pd.to_datetime(df_sentiment[sent_date_col], dayfirst=True, errors='coerce').dt.date
    df_trades['Join_Date'] = pd.to_datetime(df_trades[trade_time_col], dayfirst=True, errors='coerce').dt.date
    
    # Drop rows where date parsing failed completely
    df_sentiment = df_sentiment.dropna(subset=['Join_Date'])
    df_trades = df_trades.dropna(subset=['Join_Date'])
    
    # --- DATE OVERLAP DIAGNOSTIC ---
    if not df_sentiment.empty and not df_trades.empty:
        print("\n" + "-"*50)
        print(f"Sentiment Data Date Range: {df_sentiment['Join_Date'].min()} to {df_sentiment['Join_Date'].max()}")
        print(f"Trading History Date Range: {df_trades['Join_Date'].min()} to {df_trades['Join_Date'].max()}")
        print("-"*50)
    
    # Perform the daily chronological merge
    merged_df = pd.merge(df_trades, df_sentiment, on='Join_Date', how='inner')
    
    print(f"[DATA INFRA] Merge complete. Extracted rows: {merged_df.shape}")
    return merged_df
