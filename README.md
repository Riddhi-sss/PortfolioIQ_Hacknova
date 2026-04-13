# PortfolioIQ: Multi-Asset Quant Pipeline 🚀

### **Project Overview**
A professional-grade Machine Learning system designed to predict short-term price movements across the Indian Equity Market. This project evolved from a single-stock script into a modular, **Multi-Asset Inference Engine** that uses a Random Forest Classifier to identify high-probability trading signals.
---

## **🏗️ System Architecture**
The project follows a modular **Three-Tier Architecture** to ensure scalability and prevent "Training-Serving Skew."



1.  **Research Layer (`analysis.ipynb`):** * Conducted Exploratory Data Analysis (EDA) on a diversified basket of Nifty 50 stocks (Reliance, TCS, HDFC, etc.).
    * Engineered features using technical indicators like RSI and Volatility.
    * Trained a **Random Forest Classifier** to ensure the model learns market-wide patterns rather than sector-specific noise.

2.  **Engine Layer (`fetcher.py`):** * A universal data acquisition utility that standardizes `yfinance` MultiIndex data.
    * Automated calculation of RSI, ATR, and Volatility to maintain mathematical consistency across research and production.

3.  **Production Layer (`main_inference.py` & `automation.py`):** * **Inference Engine:** Periodically fetches live hourly data and generates signals based on the trained model.
    * **Supervisor/Watchdog:** An automation script that ensures 24/7 uptime by monitoring the process and auto-restarting the engine upon failure.

---

## **🛠️ Tech Stack**
* **Language:** Python 3.10
* **Libraries:** Scikit-Learn, Pandas, NumPy, yfinance, Joblib
* **Deployment:** Automated Python Supervisor, Telegram/n8n Webhook Integration

---


## **🚀 How to Run**

### **1. Installation**
```bash
# Clone the repository
git clone [https://github.com/Riddhi-sss/PortfolioIQ_Hacknova.git](https://github.com/Riddhi-sss/PortfolioIQ_Hacknova.git)
cd PortfolioIQ_Hacknova

# Set up the environment
python -m venv hacknova_env
.\hacknova_env\Scripts\activate  # Windows
pip install -r requirements.txt
   ```bash
   git clone [https://github.com/Riddhi-sss/PortfolioIQ_Hacknova.git](https://github.com/Riddhi-sss/PortfolioIQ_Hacknova.git)
   ```
### **2. Training the "Brain"**
* Open `scripts and notebooks/analysis.ipynb` in VS Code.
* Select `hacknova_env` as your kernel.
* Run all cells to fetch 2 years of multi-asset data and save the model as `portfolio_model_v2.joblib`.

### **3. Live Deployment**
To start the live monitor with the automated supervisor:

```bash
cd "scripts and notebooks"
python automation.py
```
### **2. Training the "Brain"**
* Open `scripts and notebooks/analysis.ipynb` in VS Code.
* Select `hacknova_env` as your kernel.
* Run all cells to fetch 2 years of multi-asset data and save the model as `portfolio_model_v2.joblib`.

### **3. Live Deployment**
To start the live monitor with the automated supervisor:

```bash
cd "scripts and notebooks"
python automation.py
```
