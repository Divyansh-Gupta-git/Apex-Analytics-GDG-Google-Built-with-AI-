# Visionary Match Tracker 🏏
AI-powered cricket analytics built with **Gemini** and **AntiGravity agentic workflows** for the Build With AI :: Agentic Premier League hackathon.

---

## 📌 Purpose
Cricket coverage today only shows basic stats like runs and ball speed. Our project goes deeper — automatically detecting **ball type, shot type, timing, and direction** from video clips, and presenting them in a live dashboard with commentary.

---

## 🎯 Goals
- **Automated Match Insights**: Detect ball trajectory, bat swing, classify deliveries and shots.
- **Real-Time Analytics**: Generate JSON stats → scorecards, heatmaps, speed charts.
- **Fan Engagement**: AI-powered commentary snippets for interactive match viewing.
- **Scalable Workflow**: Orchestrated end-to-end pipeline using AntiGravity agentic workflows.

---

## ⚙️ Tech Stack
- **Gemini Vision** → Video frame analysis (ball trajectory, bat swing, shot classification).
- **AntiGravity Workflows** → Orchestration of analysis → dashboard updates.
- **Streamlit / React** → Dashboard UI (scorecard, heatmap, charts).
- **Google AI Studio** → Prompt-driven workflow chaining.

---

## 🚀 How It Works
1. **Video Generation**  
   Synthetic cricket clips generated with Gemini (e.g., cover drive vs fast bowler, pull shot vs spinner).

2. **Video Analysis**  
   Gemini Vision detects ball type, shot type, direction, and outputs JSON:
   ```json
   { "timestamp": "00:12", "ball_type": "pace", "shot_type": "cover drive", "direction": "extra cover" }
