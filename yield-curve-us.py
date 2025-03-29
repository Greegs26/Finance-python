import pandas as pd
import matplotlib.pyplot as plt
from fredapi import Fred

import streamlit as st
import plotly.graph_objects as go

from dotenv import load_dotenv
import os

# Use this to fetch API key
load_dotenv()
FRED_API_KEY=os.getenv("FRED_API_KEY")
fred = Fred(api_key=FRED_API_KEY)

# Streamlit app title
st.title("US Treasury Yield Curve Dashboard")


# Retrieve US Treasury yield curve data from FRED
# These are the series IDs for different maturities
series_ids = {
    '1 Mo': 'DGS1MO',
    '3 Mo': 'DGS3MO',
    '6 Mo': 'DGS6MO',
    '1 Yr': 'DGS1',
    '2 Yr': 'DGS2',
    '3 Yr': 'DGS3',
    '5 Yr': 'DGS5',
    '7 Yr': 'DGS7',
    '10 Yr': 'DGS10',
    '20 Yr': 'DGS20',
    '30 Yr': 'DGS30'
}

# Fetch the latest data for each maturity
latest_data = {}
for maturity, series_id in series_ids.items():
    try:
        series_data = fred.get_series(series_id)
        latest_data[maturity] = series_data.iloc[-1]
    except Exception as e:
        print(f"Error retrieving data for {maturity}: {e}")
        latest_data[maturity] = None

# Remove maturities with no data
latest_data = {k: v for k, v in latest_data.items() if v is not None}

# Prepare data for plotting
maturities = list(latest_data.keys())
yields = list(latest_data.values())
yield_df = pd.DataFrame({"Maturity": maturities, "Yield (%)": yields})

# Display table
st.subheader("Latest Treasury Yields")
st.dataframe(yield_df)

# Plot using Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=maturities,
    y=yields,
    mode='lines+markers',
    name='Yield Curve'
))
fig.update_layout(
    title="US Treasury Yield Curve",
    xaxis_title="Maturity",
    yaxis_title="Yield (%)",
    template="plotly_white"
)
st.plotly_chart(fig)

## Create a DataFrame to display the maturities and yields
#yield_df = pd.DataFrame({
    #'Maturity': maturities,
    #'Yield (%)': yields
#})

## Print the DataFrame as a table
#print("US Treasury Yields")
#print(yield_df)

## Plot the yield curve
#plt.figure(figsize=(10, 6))
#plt.plot(maturities, yields, marker='o')
#plt.title('US Treasury Yield Curve')
#plt.xlabel('Maturity')
#plt.ylabel('Yield (%)')
#plt.grid(True)
#plt.show()