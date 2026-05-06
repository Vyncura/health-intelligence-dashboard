# app.py
# Streamlit dashboard for synthetic hospital readmission data
# Safe sample dataset included to avoid sensitive info

import streamlit as st
import pandas as pd
import numpy as np

# -------------------------------
# 1. Load Sample Dataset
# -------------------------------
# Create synthetic dataset
np.random.seed(42)
data = {
    "Patient_ID": range(1, 101),
    "Age": np.random.randint(20, 90, 100),
    "Gender": np.random.choice(["Male", "Female"], 100),
    "Length_of_Stay": np.random.randint(1, 15, 100),
    "Readmitted": np.random.choice(["Yes", "No"], 100, p=[0.3, 0.7]),
    "Cost": np.random.randint(500, 5000, 100)
}
df = pd.DataFrame(data)

# -------------------------------
# 2. Dashboard Layout
# -------------------------------
st.title("🏥 Hospital Readmission Dashboard")
st.sidebar.header("Filters")

# Sidebar filters
age_filter = st.sidebar.slider("Select Age Range", 20, 90, (20, 90))
gender_filter = st.sidebar.multiselect("Select Gender", options=df["Gender"].unique(), default=df["Gender"].unique())

# Apply filters
filtered_df = df[
    (df["Age"].between(age_filter[0], age_filter[1])) &
    (df["Gender"].isin(gender_filter))
]

# -------------------------------
# 3. KPIs
# -------------------------------
st.subheader("Key Performance Indicators (KPIs)")
col1, col2, col3 = st.columns(3)

readmission_rate = (filtered_df["Readmitted"].value_counts(normalize=True).get("Yes", 0)) * 100
avg_cost = filtered_df["Cost"].mean()
avg_stay = filtered_df["Length_of_Stay"].mean()

col1.metric("Readmission Rate", f"{readmission_rate:.1f}%")
col2.metric("Avg. Cost", f"${avg_cost:,.0f}")
col3.metric("Avg. Length of Stay", f"{avg_stay:.1f} days")

# -------------------------------
# 4. Visualizations
# -------------------------------
st.subheader("Visualizations")

# Bar chart: Readmissions by Age
st.bar_chart(filtered_df.groupby("Age")["Readmitted"].apply(lambda x: (x=="Yes").sum()))

# Table: Patient Records
st.subheader("Patient Records")
st.dataframe(filtered_df)

# -------------------------------
# 5. Notes
# -------------------------------
st.markdown("""
**README‑Friendly Notes:**
- This dashboard uses a synthetic dataset (100 patients).
- Filters allow exploration by age and gender.
- KPIs highlight readmission rate, average cost, and average stay.
- Visualizations show readmissions by age and patient records.
- Ready for deployment on **Streamlit Cloud**.
""")
