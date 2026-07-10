import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------

st.set_page_config(
    page_title="TellCo Telecom Dashboard",
    page_icon="📡",
    layout="wide"
)

# -----------------------------------------------------
# LOAD DATA
# -----------------------------------------------------

@st.cache_data
def load_data():
    feature_store = pd.read_csv("outputs/feature_store.csv")
    satisfaction = pd.read_csv("outputs/satisfaction_scores.csv")
    return feature_store, satisfaction


feature_store, satisfaction = load_data()

# -----------------------------------------------------
# HEADER
# -----------------------------------------------------

st.title("📡 TellCo Telecom Analytics Dashboard")
st.caption(
    "User Overview • Engagement • Experience • Satisfaction"
)

st.divider()

# -----------------------------------------------------
# KPI CARDS
# -----------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Customers",
    f"{len(feature_store):,}"
)

c2.metric(
    "Avg Session Frequency",
    f"{feature_store['Session_Frequency'].mean():.2f}"
)

c3.metric(
    "Avg Duration",
    f"{feature_store['Total_Duration_ms'].mean():,.0f}"
)

c4.metric(
    "Avg Traffic",
    f"{feature_store['Total_Traffic'].mean()/1e6:.2f} MB"
)

st.divider()

# -----------------------------------------------------
# APPLICATION TRAFFIC
# -----------------------------------------------------

applications = [
    "Gaming",
    "Youtube",
    "Netflix",
    "Google",
    "Social_Media",
    "Email",
    "Other"
]

application_usage = (
    feature_store[applications]
    .sum()
    .sort_values(ascending=False)
)

col1, col2 = st.columns(2)

with col1:

    fig = px.bar(
        x=application_usage.index,
        y=application_usage.values,
        title="Application Traffic",
        labels={
            "x":"Application",
            "y":"Traffic (Bytes)"
        }
    )

    fig.update_layout(height=420)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    fig = px.histogram(
        satisfaction,
        x="Satisfaction_Score",
        nbins=30,
        title="Satisfaction Score Distribution"
    )

    fig.update_layout(height=420)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# -----------------------------------------------------
# CORRELATION MATRIX
# -----------------------------------------------------

corr_cols = [
    "Session_Frequency",
    "Total_Duration_ms",
    "Total_Traffic",
    "Gaming",
    "Youtube",
    "Netflix",
    "Google"
]

corr = feature_store[corr_cols].corr()

fig = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="RdBu_r",
    title="Feature Correlation Matrix"
)

fig.update_layout(height=650)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# -----------------------------------------------------
# TOP 10 SATISFIED CUSTOMERS
# -----------------------------------------------------

top10 = (
    satisfaction
    .sort_values(
        "Satisfaction_Score",
        ascending=False
    )
    .head(10)
)

fig = px.bar(
    top10,
    x="MSISDN/Number",
    y="Satisfaction_Score",
    title="Top 10 Satisfied Customers"
)

fig.update_layout(
    xaxis_title="Customer ID",
    yaxis_title="Satisfaction Score",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# -----------------------------------------------------
# DATA PREVIEW
# -----------------------------------------------------

st.subheader("Feature Store")

st.dataframe(
    feature_store,
    use_container_width=True,
    height=350
)

st.caption(
    "Developed using Streamlit, Pandas and Plotly."
)