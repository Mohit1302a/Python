import streamlit as st
import pandas as pd
import numpy as np

#tile of the app
st.title("My Streamlit App")

#display a simple text
st.write("Welcome to my Streamlit app!")

#create a simple dataframe
df=pd.DataFrame({
    'A':[1,2,3,4],
    'B':[5,6,7,8],
    'C':[9,10,11,12]    
    })

#display the dataframe
st.write("Here is  created dataframe: ")
st.write(df)

#create a simple line chart
char_data=pd.DataFrame(
    np.random.randn(20,3),         #20 because we want 20 rows and 3 columns
    columns=['A', 'B', 'C']
)
st.write("Here is a simple line chart: ")
st.line_chart(char_data)