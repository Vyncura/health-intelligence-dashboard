import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# Load the dataset (assuming it's already uploaded or available)
df = pd.read_csv('/content/hospital_readmission_dataset.csv')

# Since the specific financial columns might be missing in the raw readmission file,
# we will use the available data and add simulated financial metrics for the demonstration.
# Check available columns: print(df.columns)

# Simulating financial columns if they don't exist for the dashboard demo
if 'billed_amount' not in df.columns:
    np.random.seed(42)
    df['billed_amount'] = np.random.uniform(5000, 50000, size=len(df))
    df['collected_amount'] = df['billed_amount'] * np.random.uniform(0.6, 0.9, size=len(df))
    df['denial_reason'] = np.random.choice(['Coding Error', 'Lack of Info', 'Not Covered', 'Duplicate Claim', 'Timely Filing'], size=len(df))
    df['payer'] = np.random.choice(['Medicare', 'Medicaid', 'Blue Cross', 'Aetna', 'UnitedHealth'], size=len(df))
    df['days_in_ar'] = np.random.randint(15, 90, size=len(df))

# 1. Financial Capture: Billed vs. Collected
billed_total = df['billed_amount'].sum()
collected_total = df['collected_amount'].sum()

fig1 = go.Figure(data=[
    go.Bar(name='Billed', x=['Total Revenue'], y=[billed_total], marker_color='#3498db'),
    go.Bar(name='Collected', x=['Total Revenue'], y=[collected_total], marker_color='#2ecc71')
])
fig1.update_layout(title='Total Billed vs. Total Collected', barmode='group', template='plotly_white', yaxis_title='Amount ($)')

# 2. Top 5 Denial Reasons
denials = df['denial_reason'].value_counts().nlargest(5).reset_index()
denials.columns = ['Reason', 'Count']

fig2 = px.pie(denials, values='Count', names='Reason', title='Top 5 Denial Reasons', hole=0.4,
             color_discrete_sequence=px.colors.sequential.RdBu)

# 3. Days in A/R by Payer
ar_by_payer = df.groupby('payer')['days_in_ar'].mean().sort_values(ascending=False).reset_index()

fig3 = px.bar(ar_by_payer, x='payer', y='days_in_ar',
             title='Average Days in A/R by Payer',
             labels={'days_in_ar': 'Avg Days', 'payer': 'Insurance Provider'},
             color='days_in_ar', color_continuous_scale='Viridis')

# Show plots
fig1.show()
fig2.show()
fig3.show()
