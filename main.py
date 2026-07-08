import os
from src.data_loader import load_and_merge_data
from src.analyzer import analyze_trader_behavior
from src.visualizer import generate_performance_chart  # Import the new plotting script

def main():
    SENTIMENT_CSV = "data/fear_greed_index.csv" 
    TRADER_CSV = "data/historical_data.csv" 
    
    if not os.path.exists(SENTIMENT_CSV) or not os.path.exists(TRADER_CSV):
        print("[CRITICAL ERROR] Target dataset files not located inside the 'data/' directory.")
        return

    # Trigger Pipeline Engine
    df = load_and_merge_data(SENTIMENT_CSV, TRADER_CSV)
    report, t_stat, p_value = analyze_trader_behavior(df)
    
    # Log Summary Table Report Matrix
    print("\n" + "="*65)
    print("                PRIMETRADE.AI QUANT DESIGN REPORT")
    print("="*65)
    print(report.to_string(index=False))
    print("-"*65)
    print(f"Statistical T-Statistic Measure : {t_stat:.4f}")
    print(f"Mathematical P-Value Significance: {p_value:.4f}")
    
    if p_value < 0.05:
        print("Verdict: Significant signal found. Market emotion shapes asset outcomes.")
    else:
        print("Verdict: Performance distribution variations match typical market noise.")
    print("="*65 + "\n")

    # --- GENERATE DATA VISUALIZATION CHART ---
    generate_performance_chart(report)

if __name__ == "__main__":
    main()
