# --- TASK 05: Cloud Orchestration Logic (Fixed for n8n) ---

# We simulate the data processing here
# In n8n, we must return a LIST of DICTIONARIES 
# Each dictionary MUST have a "json" key

output = []

# Mock stock data simulation
stocks = [
    {"ticker": "TCS.NS", "change": 0.0299},
    {"ticker": "ICICIBANK.NS", "change": 0.0050},
    {"ticker": "SUNPHARMA.NS", "change": -0.0120}
]

for s in stocks:
    status = "NEUTRAL"
    message = "Stable"
    
    if abs(s["change"]) > 0.02:
        status = "ALERT"
        message = f"High Volatility: {s['ticker']} moved {s['change']*100:.2f}%"
    
    # This is the specific format n8n requires:
    output.append({
        "json": {
            "ticker": s["ticker"],
            "change_pct": s["change"] * 100,
            "status": status,
            "alert_message": message
        }
    })

return output