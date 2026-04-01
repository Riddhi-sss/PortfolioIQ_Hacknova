cat <<EOF > README.md
# PortfolioIQ: Multi-Agent Quant Pipeline 📈
**HackNova 1.0 Submission | Case Study: Prayas Capital**

An automated financial engineering and portfolio optimization system designed for a ₹10 Lakh investment across the Banking, IT, and Pharma sectors.

## 🚀 Project Overview
This project implements a complete quantitative trading lifecycle, from raw data ingestion to machine learning-based outperformance predictions and automated n8n alerting.

## 📁 Repository Structure
### 📜 Scripts & Notebooks
- **analysis.ipynb**: The core data science engine (Task 1-4 & 6).
- **automation.py**: Python logic for the n8n orchestration (Task 5).
- **.gitignore**: Configured to exclude \`hacknova_env\` and caches.

### 📊 Output Files (CSVs)
- **raw_fetched_dataset.csv**: 2 years of daily adjusted close prices.
- **metrics_summary.csv**: Risk-return metrics (Beta, Sharpe, Volatility).
- **portfolio_b_allocation.csv**: Optimized ₹10L allocation based on Sharpe Ratios.
- **ml_feature_matrix.csv**: Engineered features for ML training.
- **technical_signals.csv**: Daily Golden/Death cross status.

### 🖼️ Visual Outputs (PNGs)
- **risk_return_map.png**: Efficient frontier visualization.
- **correlation_heatmap.png**: Inter-sector diversification proof.
- **three_sma_charts.png**: Technical signal dashboard.

## 🤖 Machine Learning Model
- **Champion Model:** Random Forest vs Logistic Regression.
- **Target:** Predict 5-day relative outperformance vs. Nifty 50.
- **Validation:** 80/20 Temporal Split to prevent Data Leakage.

## ⚙️ Automation Layer
- **Orchestration:** n8n Workflow.
- **Logic:** Triggered daily at market close for real-time alerting.
EOF
