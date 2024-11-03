import pandas as pd
import numpy as np
import streamlit as st

st.write("##################lets plot a map now###########################")

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])


st.map(map_data)