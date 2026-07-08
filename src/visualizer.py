import os
import matplotlib.pyplot as plt
import seaborn as sns

def generate_performance_chart(report_df):
    """
    Generates a dual-axis analytical performance visualization 
    tracking win rates and mean returns across market sentiments.
    """
    if report_df.empty:
        print("[VISUALIZER] Skipped plotting: Summary dataframe is empty.")
        return

    # Define the sentiment progression spectrum
    sentiment_order = ['extreme fear', 'fear', 'neutral', 'greed', 'extreme greed']
    
    # Clean the input dataframe rows to ensure exact key sorting compatibility
    report_df['classification'] = report_df['classification'].str.strip().str.lower()
    report_df = report_df.set_index('classification').reindex(sentiment_order).reset_index()

    # Configure dark terminal dashboard aesthetic rules
    plt.style.use('dark_background')
    fig, ax1 = plt.subplots(figsize=(10, 6), dpi=120)
    
    # --- AXIS 1: Bar Chart displaying Mean Profit and Loss (PnL) ---
    sns.barplot(
        data=report_df, 
        x='classification', 
        y='mean_pnl', 
        ax=ax1, 
        palette='Blues_d', 
        hue='classification', 
        legend=False, 
        alpha=0.85
    )
    ax1.set_title('Trader Performance Breakdown Across Market Sentiment Regimes', fontsize=13, pad=15, weight='bold')
    ax1.set_xlabel('Crypto Fear & Greed Index Classification', fontsize=11, labelpad=10)
    ax1.set_ylabel('Mean Profit/Loss (USD)', color='#4A90E2', fontsize=11, weight='bold')
    ax1.tick_params(axis='y', labelcolor='#4A90E2')
    ax1.grid(True, axis='y', linestyle='--', alpha=0.15)

    # --- AXIS 2: Line Graph displaying Execution Strategy Win Rate % ---
    ax2 = ax1.twinx()
    sns.lineplot(
        data=report_df, 
        x='classification', 
        y='win_rate', 
        ax=ax2, 
        color='#E2844A', 
        marker='o', 
        linewidth=2.5, 
        markersize=8,
        sort=False
    )
    ax2.set_ylabel('Execution Strategy Win Rate (%)', color='#E2844A', fontsize=11, weight='bold')
    ax2.tick_params(axis='y', labelcolor='#E2844A')
    
    # Annotate direct text values over the data nodes
    for idx, row in report_df.iterrows():
        ax2.annotate(
            f"{row['win_rate']:.1f}%", 
            (idx, row['win_rate']),
            textcoords="offset points", 
            xytext=(0,10), 
            ha='center', 
            color='#E2844A', 
            weight='bold',
            fontsize=9
        )

    plt.tight_layout()
    
    # Force print absolute storage path for clarity
    output_img = os.path.abspath("quant_performance_chart.png")
    plt.savefig(output_img, bbox_inches='tight', dpi=300)
    print(f"[VISUALIZER] Analytical data metric dashboard plot successfully exported to: '{output_img}'")
    
    # --- FORCE CHART POP-UP WINDOW ---
    print("[VISUALIZER] Launching interactive plot window display window...")
    plt.show() 
