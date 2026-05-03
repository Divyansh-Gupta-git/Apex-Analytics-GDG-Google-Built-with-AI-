import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt

# --- Sample JSON stats from Gemini Vision ---
sample_stats = [
    {"timestamp": "00:05", "ball_type": "pace", "shot_type": "cover drive", "direction": "extra cover"},
    {"timestamp": "00:12", "ball_type": "spin", "shot_type": "pull shot", "direction": "mid-wicket"},
    {"timestamp": "00:20", "ball_type": "pace", "shot_type": "sweep", "direction": "fine leg"}
]

# --- Convert to DataFrame ---
df = pd.DataFrame(sample_stats)

# --- Streamlit UI ---
st.set_page_config(page_title="Visionary Match Tracker", layout="wide")
st.title("🏏 Visionary Match Tracker")
st.write("AI-powered cricket analytics using Gemini Vision + AntiGravity workflows")

# Scorecard
st.subheader("📊 Scorecard")
st.dataframe(df)

# Shot Direction Heatmap (simple bar chart for demo)
st.subheader("🎯 Shot Directions")
direction_counts = df['direction'].value_counts()
st.bar_chart(direction_counts)

# Ball Type Distribution
st.subheader("⚡ Ball Types")
ball_counts = df['ball_type'].value_counts()
st.bar_chart(ball_counts)

# Commentary snippets
st.subheader("🗣️ Commentary")
for _, row in df.iterrows():
    st.write(f"At {row['timestamp']} → {row['shot_type']} against {row['ball_type']} bowler, played toward {row['direction']}.")

