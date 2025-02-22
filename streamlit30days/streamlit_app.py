import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

#４日目
st.header("st.write")
#例１
st.write("Hello, *World!* :sunglasses:")

#例２
st.write(1234)

#例３
df = pd.DataFrame({
    "first column":[1,2,3,4],
    "second column":[10,20,30,40]
})
st.write(df)

#例４
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

#例５
df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=["a","b","c"]
)
c = alt.Chart(df2).mark_circle().encode(
    x="a", y="b", size="c", color="c", tooltip=["a","b","c"]
)
st.write(c)

# #２日目
# st.header("st.button")
# if st.button ("Say hello"):
#     st.write("Why say hello?")
# else:
#     st.write("Goodbye")