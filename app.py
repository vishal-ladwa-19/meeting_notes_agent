from pathlib import Path
import tempfile

import pandas as pd
import streamlit as st

from utils.llm_client import generate_response
from utils.parser import extract_text
from utils.validator import validate_response
from utils.charts import display_charts
from utils.report_generator import generate_markdown_report
from utils.history import (
    save_json,
    save_csv,
    save_report,
)
from utils.logger import log_info, log_error

# -------------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------------

st.set_page_config(
    page_title="Meeting Notes AI Agent",
    page_icon="📝",
    layout="wide"
)

# -------------------------------------------------------
# HEADER
# -------------------------------------------------------

st.title("📝 Meeting Notes AI Agent")

st.caption(
    "Upload a meeting transcript or paste it below. "
    "The AI will generate summaries, decisions and action items."
)

st.divider()

# -------------------------------------------------------
# INPUT SECTION
# -------------------------------------------------------

uploaded_file = st.file_uploader(
    "📂 Upload Meeting Transcript",
    type=["txt", "pdf", "docx"]
)

transcript = st.text_area(
    "OR Paste Meeting Transcript",
    placeholder="Paste your meeting transcript here...",
    height=250
)

analyze = st.button(
    "🚀 Analyze Meeting",
    use_container_width=True
)

# -------------------------------------------------------
# ANALYSIS
# -------------------------------------------------------

if analyze:

    # -----------------------------------
    # Validate Input
    # -----------------------------------

    if uploaded_file is None and not transcript.strip():
        st.warning(
            "Please upload a transcript or paste meeting text."
        )
        st.stop()

    # -----------------------------------
    # Read Uploaded File
    # -----------------------------------

    if uploaded_file is not None:

        try:

            suffix = Path(uploaded_file.name).suffix.lower()

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=suffix
            ) as tmp:

                tmp.write(uploaded_file.getvalue())

                transcript = extract_text(tmp.name)
                log_info(f"Uploaded file: {uploaded_file.name}")

        except Exception as e:

            st.error(f"Unable to read uploaded file.\n\n{e}")
            st.stop()

    # -----------------------------------
    # Load System Prompt
    # -----------------------------------

    try:

        with open(
            "prompts/system_prompt.txt",
            "r",
            encoding="utf-8"
        ) as file:

            system_prompt = file.read()

    except Exception as e:

        st.error(f"Cannot load system prompt.\n\n{e}")
        st.stop()

    # -----------------------------------
    # Call AI
    # -----------------------------------

    with st.spinner("🤖 AI is analyzing the meeting..."):

        result = generate_response(
            system_prompt,
            transcript
        )
        log_info("AI analysis completed successfully.")

    # -----------------------------------
    # Validate JSON
    # -----------------------------------

    try:

        analysis = validate_response(result)

    except Exception as e:

        log_error(str(e))

        st.stop()

    # -------------------------------------------------------
    # DASHBOARD
    # -------------------------------------------------------

    st.divider()

    st.subheader("📊 Meeting Statistics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Meeting Type",
            analysis.meeting_type
        )

    with col2:
        st.metric(
            "Health Score",
            f"{analysis.health_score}/100"
        )

    with col3:
        st.metric(
            "Action Items",
            len(analysis.action_items)
        )

    with col4:
        st.metric(
            "Decisions",
            len(analysis.decisions)
        )

    st.divider()

    st.subheader("📅 Follow-up Required")

    if analysis.follow_up_required:
        st.error("🔴 Yes, a follow-up meeting is recommended.")
    else:
        st.success("🟢 No follow-up meeting is required.")

    # -------------------------------------------------------
    # SUMMARY
    # -------------------------------------------------------

    st.subheader("📋 Executive Summary")

    st.info(analysis.summary)

    st.divider()

    # -------------------------------------------------------
    # DECISIONS
    # -------------------------------------------------------

    st.subheader("✅ Meeting Decisions")

    if analysis.decisions:

        for decision in analysis.decisions:

            st.success(decision)

    else:

        st.warning("No meeting decisions detected.")

    st.divider()


    st.subheader("⚠ Risks")

    if analysis.risks:

        for risk in analysis.risks:
            st.warning(risk)

    else:

        st.success("No significant risks detected.")

    st.divider()

# -------------------------------------------------------
# AI RECOMMENDATIONS
# -------------------------------------------------------

    st.subheader("💡 AI Recommendations")

    if analysis.recommendations:

        for recommendation in analysis.recommendations:
            st.info(recommendation)

    else:

        st.success("No recommendations generated.")
    # -------------------------------------------------------
    # ACTION ITEMS
    # -------------------------------------------------------

    st.subheader("📌 Action Item Manager")

    rows = []

    for index, item in enumerate(analysis.action_items):

        status = st.selectbox(
            f"Status for Task {index+1}",
            ["Pending", "In Progress", "Completed"],
            index=["Pending", "In Progress", "Completed"].index(item.status),
            key=f"status_{index}"
        )

        rows.append({
            "Task": item.task,
            "Owner": item.owner,
            "Due Date": item.due_date,
            "Priority": item.priority,
            "Status": status
        })

    df = pd.DataFrame(rows)

    st.data_editor(
        df,
        use_container_width=True,
        hide_index=True,
        disabled=["Task", "Owner", "Due Date", "Priority"]
    )
    
    display_charts(df)

    st.divider()

    # -------------------------------------------------------
    # DOWNLOAD JSON
    # -------------------------------------------------------
    col1, col2 = st.columns(2)

    with col1:

     st.download_button(
        label="⬇ Download JSON",
        data=result,
        file_name="meeting_analysis.json",
        mime="application/json",
        use_container_width=True
    )

    # -------------------------------------------------------
    # DOWNLOAD CSV
    # -------------------------------------------------------
    with col2:

        csv = df.to_csv(index=False)

        st.download_button(
            label="⬇ Download CSV",
            data=csv,
            file_name="action_items.csv",
            mime="text/csv",
            use_container_width=True
        )

        report = generate_markdown_report(analysis)
        log_info("Meeting report generated.")

        save_json(result)
        save_csv(df)
        save_report(report)

        st.download_button(
            label="📄 Download Meeting Report",
            data=report,
            file_name="Meeting_Report.md",
            mime="text/markdown",
            use_container_width=True,
        )
    st.divider()

    with st.expander("📄 View Transcript"):

        st.text(transcript)
    # -------------------------------------------------------
    # RAW JSON
    # -------------------------------------------------------

    with st.expander("🔍 View Raw AI JSON"):

        st.code(result, language="json")