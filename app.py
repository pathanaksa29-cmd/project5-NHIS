import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load your processed data
df = pd.read_csv("C:/dataset1/final_user_satisfaction.csv")

st.title("TellCo Telecom User Analytics Dashboard")

# Sidebar filters
user_filter = st.sidebar.text_input("Search MSISDN Number")

if user_filter:
    st.write(df[df['MSISDN_Number'] == user_filter])
else:
    st.write(df.head())

# Tabs for analysis
tab1, tab2, tab3, tab4 = st.tabs(["User Overview", "Engagement", "Experience", "Satisfaction"])

# ---------------- Tab 1: User Overview ----------------
with tab1:
    st.subheader("Top Handsets")
    top_handsets = df['handset_type'].value_counts().head(10)
    st.bar_chart(top_handsets)

    st.subheader("Handset Distribution Pie Chart")
    fig, ax = plt.subplots()
    top_handsets.plot.pie(autopct='%1.1f%%', ax=ax)
    st.pyplot(fig)

# ---------------- Tab 2: Engagement ----------------
with tab2:
    st.subheader("User Engagement Scatterplot")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x="session_frequency", y="total_traffic_bytes",
                    hue="satisfaction_cluster", ax=ax)
    st.pyplot(fig)

    st.subheader("Top 10 Engaged Users by Traffic")
    st.write(df.nlargest(10, "total_traffic_bytes")[["MSISDN_Number","total_traffic_bytes"]])

# ---------------- Tab 3: Experience ----------------
with tab3:
    st.subheader("Experience Metrics by Handset")
    exp_metrics = df.groupby("handset_type")[["average_throughput_kbps",
                                              "average_TCP_retransmission_bytes"]].mean()
    st.write(exp_metrics)

    st.subheader("Throughput Distribution Boxplot")
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x="handset_type", y="average_throughput_kbps", ax=ax)
    plt.xticks(rotation=90)
    st.pyplot(fig)

# ---------------- Tab 4: Satisfaction ----------------
with tab4:
    st.subheader("Top 10 Satisfied Customers")
    st.write(df.nlargest(10, "satisfaction_score")[["MSISDN_Number","satisfaction_score"]])

    st.subheader("Correlation Heatmap")
    corr = df[['engagement_score','experience_score','satisfaction_score']].corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# ---------------- Download Button ----------------
st.download_button("Download Satisfaction Data", df.to_csv(index=False), "satisfaction.csv")
