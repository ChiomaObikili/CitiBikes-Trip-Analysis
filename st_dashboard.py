# st_dashboard.py

# Importing libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from datetime import datetime as dt
from streamlit_keplergl import keplergl_static

# Page config
st.set_page_config(page_title="NewYork Bikes Strategy Dashboard", layout="wide")

# Title and intro
st.title("NewYork Bikes Strategy Dashboard")
st.markdown("The dashboard will help with the expansion problems NewYork city currently faces")

# ---------------------------
# 🚴 Data visualization section
# 
####################### Import data #########################################

df = pd.read_csv('reduced_data_to_plot.csv', index_col = 0)
top20 = pd.read_csv('top20.csv', index_col = 0)

# ########################### DEFINE THE CHARTS ############################


## Bar chart 

fig = go.Figure(go.Bar(x = top20['start_station_name'], y = top20['value'], marker = {'color' : top20['value'], 'colorscale' : 'Blues'}))
fig.update_layout(
    title = 'Top 20 Most Popular Bike Stations in Newyork',
    xaxis_title = 'Start Stations', 
    yaxis_title = 'Sum of Trips', 
    width = 900, height = 600
)
st.plotly_chart(fig, use_container_width = True)

## Line chart

df = pd.read_csv('reduced_data_to_plot.csv', index_col=0)
top20 = pd.read_csv('top20.csv', index_col=0)

# Making sure 'date' column exists and is datetime
print("Columns in df:", df.columns.tolist())  # Debugging step

if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])
else:
    st.error("No 'date' column found in reduced_data_to_plot.csv")
    st.stop()

# Aggregating daily bikes ride
daily_rides = df.groupby('date').size().reset_index(name='bike_rides_daily')

# # Merge with temperature (assuming 'avgTemp' is daily)
df_daily = pd.merge(daily_rides, df[['date', 'avgTemp']].drop_duplicates(), on='date')

# Filtering data for 2022
df_2022 = df_daily[df_daily['date'].dt.year == 2022]


# taking a random 100k rows 
df_sample = df_2022.sample(n=min(100000, len(df_2022)), random_state=42).sort_values('date')

fig_2 = make_subplots(specs=[[{"secondary_y": True}]])

# Daily bike rides
fig_2.add_trace(
    go.Scatter(
        x=df_sample['date'],
        y=df_sample['bike_rides_daily'],
        name='Daily bike rides',
        marker={'color': 'blue'},
        mode='lines+markers'
    ),
    secondary_y=False
)

# Daily temperature
fig_2.add_trace(
    go.Scatter(
        x=df_sample['date'],
        y=df_sample['avgTemp'],
        name='Daily temperature',
        marker={'color': 'red'},
        mode='lines+markers'
    ),
    secondary_y=True
)

fig_2.update_layout(
    title='Newyork Daily Bike Rides and Temperature in 2022 (Sampled Points)',
    xaxis_title='Date',
    yaxis_title='Bike Rides',
    yaxis2_title='Temperature (°C)',
    legend_title='Metrics',
    template='plotly_white'
)

fig_2.show()

st.plotly_chart(fig_2, use_container_width=True)

### Add the map  ###

path_to_html = "Newyork Bikes Trips Aggregated.html"

# Read file and keep in variable 
with open(path_to_html, 'r') as f:
    html_data = f.read()

## Show in web page 
st.header("Aggregated Bike Trips in Newyork")
st.components.v1.html(html_data,height = 1000)
