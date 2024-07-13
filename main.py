import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Metrocraft")
st.title('Metrocraft: ')
st.subheader("The AI urban planning and civil policy platform for frustrated citizens and sci-fi enthusiasts!")
df = pd.DataFrame(
  [[37.7699, -122.226]],
  columns = ["lat", "lon"]
)
st.map(df)