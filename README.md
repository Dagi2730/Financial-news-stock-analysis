# 📊 Financial News & Stock Analysis

## 📋 Overview

This project analyzes the relationship between financial news sentiment and stock market returns for major technology stocks. Using daily news sentiment scores and historical stock prices, it investigates whether sentiment can predict short-term stock price movements.

The analysis covers seven major tickers: **AAPL, AMZN, GOOG, META, MSFT, NVDA, and TSLA**. Key techniques include:

- 🔗 Data merging of stock prices and sentiment scores  
- 📈 Calculation of daily stock returns  
- 🔍 Correlation analysis between sentiment and returns (same-day and lagged)  
- 📊 Visualization of correlation results  
- ✍️ Summary of findings and insights  

---

## 🎯 Motivation

Financial news sentiment can influence investor behavior and market dynamics. Understanding this relationship can support better trading strategies, risk management, and market prediction models. This project aims to assess if daily sentiment data provides meaningful signals for stock returns.

---

## 📂 Project Structure

- 📓 `notebooks/`: Jupyter notebooks for exploratory data analysis (EDA), correlation computations, and visualizations.  
- 📁 `data/`: Raw and processed datasets (stock prices, sentiment scores).  
- 🛠️ `scripts/`: Python scripts for data processing and analysis (optional).  
- 📄 `README.md`: This documentation file.  

---

## 🛠️ Requirements

- Python 3.8+  
- pandas  
- numpy  
- scipy  
- matplotlib  
- seaborn  
- Jupyter Notebook  

Install dependencies via pip:

```bash
pip install pandas numpy scipy matplotlib seaborn jupyter

📈 Key Results
Same-day correlations between sentiment and stock returns are close to zero and statistically insignificant for all tickers.

Lagged sentiment (1-5 days prior) also shows no consistent significant correlation.

Findings suggest that daily aggregated sentiment may not strongly predict daily stock returns in this dataset.

🔮 Future Work
Explore intraday sentiment data for finer resolution analysis.

Use alternative sentiment metrics or more advanced NLP techniques.

Apply nonlinear models or machine learning to capture complex relationships.

Extend analysis to other sectors or global markets.

👤 Author
Dagmawit Andargachew
