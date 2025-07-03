# 🔥 FantasyInsights

A data science project that classifies fantasy football players into meaningful **performance archetypes** based on weekly consistency, volatility, and scoring trends. Instead of just ranking players by total points, this tool helps fantasy managers understand *how* players score — whether they’re steady contributors, boom-or-bust wildcards, or trap picks with high usage but poor results.

---

## 🚀 Features

- Clusters players into performance archetypes using machine learning
- Analyzes volatility, ceiling, floor, and usage patterns
- Generates consistent metrics like:
  - Average Fantasy Points
  - Standard Deviation (Volatility)
  - Boom Rate
  - Bust Rate
  - Consistency Score
- Optional Streamlit dashboard for interactive exploration

---

## 🛠 How It Works

1. **Data Collection**  
   Weekly player performance is collected from fantasy football APIs or CSVs.

2. **Feature Engineering**  
   Key metrics like boom/bust rate, floor/ceiling, and usage trends are extracted.

3. **Clustering**  
   Players are grouped using K-Means to identify behavior-based archetypes.

4. **Visualization**  
   Outputs include scatter plots, cluster summaries, and optional web dashboards.

---

## 📁 Project Structure

boom_bust_archetypes/
├── data/ # Raw + cleaned data files
├── notebooks/ # EDA and visualization
├── src/ # Data loading, feature generation, clustering
├── streamlit_app/ # Optional Streamlit dashboard
├── requirements.txt
└── README.md

---

## 📦 Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/FantasyInsights.git
   cd FantasyInsights
2. Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate  # or `venv\Scripts\activate` on Windows
3. Install dependencies:
    pip install -r requirements.txt
4. Run the clustering pipeline:
    python src/main.py
5. (Optional) Launch the dashboard:
    streamlit run streamlit_app/app.py

---

### ✅ `requirements.txt`

```txt
pandas>=1.5.0
numpy>=1.21.0
scikit-learn>=1.1.0
matplotlib>=3.5.0
seaborn>=0.11.2
streamlit>=1.14.0

---
### ✅ MIT License

Copyright (c) 2025 Suraj Menon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
