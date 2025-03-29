import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from yield_us import get_us_yields
from yield_canadian import get_canadian_yields

st.title("📈 US & Canadian Yield Curve Dashboard")

# --- US Yield Curve ---
st.subheader("🇺🇸 US Treasury Yield Curve")
us_yields = get_us_yields()
us_df = pd.DataFrame(list(us_yields.items()), columns=["Maturity", "Yield (%)"])
st.dataframe(us_df)

fig_us = go.Figure()
fig_us.add_trace(go.Scatter(x=us_df["Maturity"], y=us_df["Yield (%)"], mode="lines+markers"))
fig_us.update_layout(title="US Yield Curve", xaxis_title="Maturity", yaxis_title="Yield (%)")
st.plotly_chart(fig_us)

# --- Canadian Yield Curve ---
st.subheader("🇨🇦 Canadian Government Yield Curve")
ca_yields = get_canadian_yields()
ca_df = pd.DataFrame(list(ca_yields.items()), columns=["Maturity", "Yield (%)"])
st.dataframe(ca_df)

fig_ca = go.Figure()
fig_ca.add_trace(go.Scatter(x=ca_df["Maturity"], y=ca_df["Yield (%)"], mode="lines+markers"))
fig_ca.update_layout(title="Canadian Yield Curve", xaxis_title="Maturity", yaxis_title="Yield (%)")
st.plotly_chart(fig_ca)