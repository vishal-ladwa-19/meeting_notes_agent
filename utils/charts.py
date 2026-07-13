import pandas as pd
import streamlit as st


def display_charts(df: pd.DataFrame):
    """
    Displays analytics charts.
    """

    if df.empty:
        return

    st.divider()

    st.subheader("📊 Meeting Analytics")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Priority Distribution")
        priority_counts = df["Priority"].value_counts()
        st.bar_chart(priority_counts)

    with col2:
        st.markdown("### Owner Workload")
        owner_counts = df["Owner"].value_counts()
        st.bar_chart(owner_counts)

    st.divider()

    st.subheader("📈 Analytics Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Tasks", len(df))

    with col2:
        high = df["Priority"].str.contains("High").sum()
        st.metric("High Priority", high)

    with col3:
        owners = df["Owner"].nunique()
        st.metric("Owners", owners)

    with col4:
        st.metric("Completion", "Pending")