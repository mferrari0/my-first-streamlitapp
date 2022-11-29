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


fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", hover_name="Volcano Name", hover_data=["Status", "Type"],
                        color_discrete_sequence=["red"], zoom=0.5, height=300)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

if st.checkbox("Show Map"):
    st.plotly_chart(fig)

st.header("Based on Type of Volcano")



left_column, middle_column, right_column = st.columns([3, 1, 1])



# Widgets: selectbox
types = ["All"]+sorted(pd.unique(df['Type']))
type = left_column.selectbox("Choose a Type", types)

if type == "All":
    reduced_df = df
else:
    reduced_df = df[df["Type"] == type]


fig2 = px.scatter_mapbox(reduced_df, lat="Latitude", lon="Longitude", hover_name="Volcano Name", hover_data=["Status", "Type"],
                        color_discrete_sequence=["red"], zoom=0.5, height=300)

fig2.update_layout(mapbox_style="open-street-map")
fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


st.plotly_chart(fig2)