import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots

# -------------------------------
# 1. Create Synthetic Dataset
# -------------------------------
np.random.seed(42)
n = 200
df = pd.DataFrame({
    "Patient_ID": range(1, n+1),
    "Age": np.random.randint(20, 90, n),
    "Gender": np.random.choice(["Male", "Female"], n),
    "Readmitted": np.random.choice(["Yes", "No"], n, p=[0.3, 0.7]),
    "billed_amount": np.random.uniform(5000, 50000, n),
    "collected_amount": np.random.uniform(3000, 45000, n),
    "denial_reason": np.random.choice(
        ["Coding Error", "Lack of Info", "Not Covered", "Duplicate Claim", "Timely Filing"], n
    ),
    "payer": np.random.choice(
        ["Medicare", "Medicaid", "Blue Cross", "Aetna", "UnitedHealth"], n
    ),
    "days_in_ar": np.random.randint(15, 90, n)
})

# -------------------------------
# 2. Financial Capture: Billed vs Collected
# -------------------------------
billed_total = df['billed_amount'].sum()
collected_total = df['collected_amount'].sum()

fig1 = go.Figure(data=[
    go.Bar(name='Billed', x=['Total Revenue'], y=[billed_total], marker_color='#3498db'),
    go.Bar(name='Collected', x=['Total Revenue'], y=[collected_total], marker_color='#2ecc71')
])
fig1.update_layout(title='Total Billed vs. Total Collected', barmode='group', template='plotly_white')
fig1.show()

# -------------------------------
# 3. Top 5 Denial Reasons
# -------------------------------
denials = df['denial_reason'].value_counts().nlargest(5).reset_index()
denials.columns = ['Reason', 'Count']

fig2 = px.pie(denials, values='Count', names='Reason', title='Top 5 Denial Reasons', hole=0.4,
             color_discrete_sequence=px.colors.sequential.RdBu)
fig2.show()
