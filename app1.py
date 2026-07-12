import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="TellCo Telecom Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 TellCo Telecom Analytics Dashboard")

st.markdown(
"""
### User Overview • Engagement • Experience • Satisfaction
"""
)

# ----------------------------
# Read CSV files
# ----------------------------

feature_store = pd.read_csv("feature_store.csv")

satisfaction = pd.read_csv("satisfaction_scores.csv")

# ----------------------------
# Sidebar
# ----------------------------

st.sidebar.title("Dashboard")

page = st.sidebar.radio(
    "Select Analysis",
    [
        "Home",
        "User Overview",
        "Engagement",
        "Experience",
        "Satisfaction"
    ]
)
if page=="Home":

    st.header("Project Summary")

    c1,c2,c3,c4=st.columns(4)

    c1.metric(
        "Total Users",
        len(feature_store)
    )

    c2.metric(
        "Avg Session",
        round(
            feature_store["Session_Frequency"].mean(),
            2
        )
    )

    c3.metric(
        "Avg Duration",
        round(
            feature_store["Total_Duration_ms"].mean(),
            2
        )
    )

    c4.metric(
        "Avg Traffic (MB)",
        round(
            feature_store["Total_Traffic"].mean()/1000000,
            2
        )
    )

    st.divider()

    col1,col2,col3=st.columns(3)

    col1.metric(
        "Avg Engagement",
        round(
            satisfaction["Engagement_Score"].mean(),
            2
        )
    )

    col2.metric(
        "Avg Experience",
        round(
            satisfaction["Experience_Score"].mean(),
            2
        )
    )

    col3.metric(
        "Avg Satisfaction",
        round(
            satisfaction["Satisfaction_Score"].mean(),
            2
        )
    )

    st.divider()

    st.subheader("Feature Store")

    st.dataframe(
        feature_store.head(20),
        use_container_width=True
    )

    st.subheader("Satisfaction Dataset")

    st.dataframe(
        satisfaction.head(20),
        use_container_width=True
    )
    