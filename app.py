import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import joblib

# Load the trained model and feature names
try:
    rf = joblib.load('./notebooks/random_forest_model.pkl')
    feature_names = joblib.load('./notebooks/feature_names.pkl')
except Exception as e:
    st.error(f"Error loading model files: {e}")



# Load your main dataset
df = pd.read_csv("./data/loyalty_users.csv")  # Replace with your actual CSV or load from memory

st.set_page_config(layout="wide")
st.title("🧪 Loyalty A/B Test Dashboard")

# Sidebar filters
with st.sidebar:
    st.header("Filters")
    selected_group = st.selectbox("Select Group", options=["All"] + sorted(df['group'].unique().tolist()))
    selected_tier = st.selectbox("Select Tier", options=["All"] + sorted(df['loyalty_tier'].unique().tolist()))
    
    # Apply filters
    df_filtered = df.copy()
    if selected_group != "All":
        df_filtered = df_filtered[df_filtered['group'] == selected_group]
    if selected_tier != "All":
        df_filtered = df_filtered[df_filtered['loyalty_tier'] == selected_tier]

# Top KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Users", f"{df_filtered['user_id'].nunique():,}")
col2.metric("Repeat Purchase Rate", f"{df_filtered['repeat_purchase'].mean()*100:.2f}%")
col3.metric("Average Revenue", f"${df_filtered['revenue'].mean():.2f}")

# Group Comparison Chart
st.subheader("📊 Group Comparison: Repeat Purchase & Revenue")

group_metrics = df_filtered.groupby('group').agg({
    'repeat_purchase': 'mean',
    'revenue': 'mean'
}).rename(columns={'repeat_purchase': 'Repeat Rate', 'revenue': 'Avg Revenue'})

st.bar_chart(group_metrics)

# Optional: Model Results
st.subheader("📈 Feature Importance (Random Forest)")

# Assuming you already trained RandomForestClassifier as `rf` with features `X.columns`
importances = rf.feature_importances_



# Plot
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=importances, y=feature_names, ax=ax)
ax.set_title("Feature Importance (Random Forest)")
st.pyplot(fig)

 
