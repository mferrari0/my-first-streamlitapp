# Streamlit live coding script
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy



# First some MPG Data Exploration
@st.cache
def load_data(path):
    df = pd.read_csv(path)
    return df


volc_df_raw = load_data(path="./data/volcano_ds_pop.csv")
df = deepcopy(volc_df_raw)

# Add title and header
st.title("Volcanoes World Map")

st.header("Based on Type of Volcano")

fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", hover_name="Volcano Name", hover_data=["Status", "Type"],
                        color="Type", zoom=0.5, height=400, width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


st.plotly_chart(fig)

