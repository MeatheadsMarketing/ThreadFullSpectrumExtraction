import streamlit as st
from interface import thread_preview_tab

st.set_page_config(page_title="ThreadFullSpectrumExtraction Dashboard", layout="wide")

# --- Sidebar Navigation ---
st.sidebar.title("🧠 Thread Navigation")
selected_tab = st.sidebar.radio("Select a View", [
    "📊 Export Summary",
    "🧩 Recovery Matrix",
    "✅ Validation Panel",
    "📝 Fragment Search",
    "🔍 Shortcut Index",
    "🧠 Assistant Tag Map",
    "✏️ Fragment Editor",
    "📦 Export Composer",
    "⚙️ Prompt Debug Console",
    "📈 Recovery Confidence",
    "📜 Session Summary",
    "📅 Recovery Log Timeline",
    "📂 File Uploader",
    "🔧 System Tools",
    "📤 Export Trigger",
    "🧭 Thread Map",
    "📋 Fragment Count",
    "🔄 Lifecycle Viewer",
    "📥 Notion Sync Trigger",
    "📊 Export Metadata"
])

# --- Top Feedback Bar ---
st.toast("Welcome to ThreadFullSpectrumExtraction v1.1", icon="🧠")

# --- Tab Routing Logic ---
if selected_tab == "📊 Export Summary":
    thread_preview_tab.render_export_summary()

elif selected_tab == "🧩 Recovery Matrix":
    thread_preview_tab.render_recovery_matrix()

elif selected_tab == "✅ Validation Panel":
    thread_preview_tab.render_validation_check()

elif selected_tab == "📝 Fragment Search":
    st.text_input("Search for Fragment ID or Keyword")

elif selected_tab == "🔍 Shortcut Index":
    st.markdown("### All Shortcuts Detected:")
    st.code("#X, #S, #SNS, #O")

elif selected_tab == "🧠 Assistant Tag Map":
    st.markdown("`#X`, `#O`, `#SNS`, `#MERGE-RUN` shown as assistant origin tags.")

elif selected_tab == "✏️ Fragment Editor":
    frag = st.selectbox("Select fragment to edit", ["frag_SNS_001.md", "frag_O_002.md"])
    st.text_area("Edit Fragment:", height=200)

elif selected_tab == "📦 Export Composer":
    st.multiselect("Select items to include in export", ["thread_export.md", "thread_table.csv", "audit_log.json"])

elif selected_tab == "⚙️ Prompt Debug Console":
    user_prompt = st.text_area("Test Regeneration Prompt:")
    if st.button("Simulate Response"):
        st.success(f"🧠 Simulated GPT Response for: {user_prompt[:50]}...")

elif selected_tab == "📈 Recovery Confidence":
    st.progress(85, text="Recovery Coverage: 85%")

elif selected_tab == "📜 Session Summary":
    st.markdown("Thread ID: FSE_v1.1 | Fragments: 3 | Status: ✅")

elif selected_tab == "📅 Recovery Log Timeline":
    st.markdown("✅ MSG 21 Recovered — 🔴 MSG 23 Drifted — ✅ MSG 25 Fixed")

elif selected_tab == "📂 File Uploader":
    st.file_uploader("Upload Recovery Logs")

elif selected_tab == "🔧 System Tools":
    st.button("Run Drift Check")
    st.button("Run Export Validation")

elif selected_tab == "📤 Export Trigger":
    st.download_button("Download Final Export", data="export_bundle", file_name="bundle.zip")

elif selected_tab == "🧭 Thread Map":
    st.markdown("MSG 1 → MSG 10 → MSG 22 → (Recovered) → MSG 35")

elif selected_tab == "📋 Fragment Count":
    st.metric(label="Recovered Fragments", value="3")

elif selected_tab == "🔄 Lifecycle Viewer":
    st.markdown("Phase: Recovery → Validation → Ready")

elif selected_tab == "📥 Notion Sync Trigger":
    st.button("Sync Export Log to Notion")

elif selected_tab == "📊 Export Metadata":
    st.json({
        "export_status": "complete",
        "version": "v1.1",
        "fragments": 3,
        "shortcuts": 6
    })