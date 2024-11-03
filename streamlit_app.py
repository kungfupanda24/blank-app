
# My first app
#Here's our first attempt at using data to create a table:

import streamlit as st
import pandas as pd
import numpy as np
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.table(df)

st.write("this is my second attempt to create a table")

st.write(pd.DataFrame({
    'first column' : [5,6,7,8],
    'second column':[50,60,70,80]
}))

st.write("##################lets draw a line chart now###########################")

chart_data = pd.DataFrame(
    np.random.randn(50, 2),
    columns =['tatamotor','maruti'])


st.line_chart(chart_data)

