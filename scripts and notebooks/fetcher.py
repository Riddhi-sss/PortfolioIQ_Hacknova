import yfinance as yf
import pandas as pd
import numpy as np

def get_market_features(ticker_symbol, period="60d", interval="1h", training_mode=False):
    # 1. Fetch Data
    df = yf.download(ticker_symbol, period=period, interval=interval, progress=False)
    
    if df.empty:
        print(f"❌ Error: No data found for {ticker_symbol}")
        return None

    # --- DEBUGGING: See what yfinance is actually sending ---
    # print(f"DEBUG: Raw columns for {ticker_symbol}: {df.columns.tolist()}")

    # 2. FORCE FLATTEN (The MultiIndex Killer)
    if isinstance(df.columns, pd.MultiIndex):
        # We take the first level ('Close', 'Open') and discard the second ('RELIANCE.NS')
        df.columns = df.columns.get_level_values(0)
    
    # 3. Rename to standard casing (Fixes 'close' vs 'Close')
    df.columns = [str(col).strip().capitalize() for col in df.columns]
    
    # 4. Check for 'Adj close' which yfinance often uses
    if 'Close' not in df.columns and 'Adj close' in df.columns:
        df['Close'] = df['Adj close']

    # --- FINAL SAFETY CHECK ---
    if 'Close' not in df.columns:
        print(f"🚨 CRITICAL: 'Close' column still missing! Columns are: {df.columns.tolist()}")
        return None

    # 5. Manual RSI Calculation (Using the now-guaranteed 'Close')
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    df['Volatility'] = df['Close'].pct_change().rolling(window=10).std()
    
    # Clean and select features
    df = df.dropna()
    features = df[['RSI', 'Volatility', 'Close']] # Keep Close for the Target calculation in the notebook

    return features if training_mode else features.tail(1)

if __name__ == "__main__":
    # Quick Test
    sample = get_market_features("RELIANCE.NS")
    print("\n--- Current Market Snapshot ---")
    print(sample)
