import joblib
import requests
import time
import warnings
from datetime import datetime
from fetcher import get_market_features


warnings.filterwarnings("ignore")

# Loading the Model
MODEL_PATH = 'portfolio_model_v2.joblib'
try:
    model = joblib.load(MODEL_PATH)
    print(f"✅ Model loaded successfully: {MODEL_PATH}")
except Exception as e:
    print(f"❌ Error loading model: {e}")

# Configuration
N8N_WEBHOOK_URL = "https://riddhi-s.app.n8n.cloud/webhook/portfolio-alert" 
WATCHLIST = [
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS",
    "BHARTIARTL.NS", "SBI.NS", "LICI.NS", "ITC.NS", "HINDUNILVR.NS",
    "LT.NS", "BAJFINANCE.NS", "HCLTECH.NS", "MARUTI.NS", "SUNPHARMA.NS"
]
CONFIDENCE_THRESHOLD = 0.75  # Only alert if model is > 75% sure

def is_market_open():
    """Checks if the NSE market is currently open (9:15 AM - 3:30 PM IST, Mon-Fri)"""
    now = datetime.now()
    # 0=Monday, 4=Friday
    if now.weekday() <= 4:
        # Convert current time to minutes since midnight
        now_mins = now.hour * 60 + now.minute
        market_start = 9 * 60 + 15
        market_end = 15 * 60 + 30
        return market_start <= now_mins <= market_end
    return False

def run_portfolio_monitor():
    current_time = datetime.now().strftime('%H:%M:%S')
    print(f"\n--- 🔍 Scanning Watchlist at {current_time} ---")
    
    for ticker in WATCHLIST:
        features = get_live_market_data(ticker)
        
        if features is not None:
            prediction = model.predict(features)[0]
            prob = model.predict_proba(features)[0][1]
            
            status = "🚀 BUY" if prediction == 1 else "🛑 WAIT"
            print(f"[{ticker:12}] Signal: {status} | Confidence: {prob:.2%}")

            # --- UPDATE THIS BLOCK ---
            if prediction == 1 and prob > CONFIDENCE_THRESHOLD:
                # This is your new "Branded" payload
                payload = {
                    "project": "VectorAlpha 🛰️",
                    "ticker": ticker,
                    "confidence": f"{round(prob * 100, 2)}%",
                    "timestamp": current_time,
                    "message": "Outperformance detected vs Nifty 50 Benchmark."
                }
                
                try:
                    # Make sure this uses your n8n Webhook URL
                    response = requests.post(N8N_WEBHOOK_URL, json=payload, timeout=10)
                    with open("signal_log.csv", "a") as f:
                     f.write(f"{datetime.now()},{ticker},{prob}\n")
                except Exception as e:
                    print(f"   ⚠️ Webhook failed: {e}")

if __name__ == "__main__":

    while True:
        if is_market_open():
            run_portfolio_monitor()
        else:
            print(f"[{datetime.now().strftime('%H:%M')}] 💤 Market is closed. Resting...")
        
        # This part must be INDENTED (pushed to the right)
        print("Waiting 1 hour for next cycle...")
        time.sleep(3600)