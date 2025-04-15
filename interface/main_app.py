import streamlit as st
from interface import thread_preview_tab

st.set_page_config(page_title="ThreadFullSpectrumExtraction Dashboard", layout="wide")

st.sidebar.title("🧠 Thread Navigation")
selected_tab = st.sidebar.radio("Select a View", [
    "📊 Export Summary",
    "🧩 Recovery Matrix",
    "✅ Validation Panel"
])

if selected_tab == "📊 Export Summary":
    thread_preview_tab.render_export_summary()

elif selected_tab == "🧩 Recovery Matrix":
    thread_preview_tab.render_recovery_matrix()

elif selected_tab == "✅ Validation Panel":
    thread_preview_tab.render_validation_check()