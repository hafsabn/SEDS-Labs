import streamlit as st 
from datetime import datetime , date
import time
import pandas_datareader.data as pdr
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_option_menu import option_menu

# Input Texts
st.markdown("# Streamlit :red[Tutorial]")
name = st.text_input("Full name" , placeholder='e.g Benghenima Hafsa')
age = st.number_input("What's your age?",min_value=20,max_value=100)
date = st.date_input("Select a date range",value=(date(2023,12,1),date(2024,1,31)))

#Select Box & multi select
option = st.selectbox("Choose a model to train:",("A","B","C","D","E","F"))
options = st.multiselect("select the metric to analyse:",("one","two","three","four","five"))

#radio btn
model_choice = st.radio("which model of ml u want to train?",["LinReg","LogReg"])
st.write("The model you choosed is: ",model_choice)

# Sliders
age = st.slider("How old are you?",18,100,21)
st.write('you are',age)

values = st.slider("select a range of values: ",0.0,100.0,(25.0,75.0))
st.write('values: ',values[1]) # values[1] will select the second value

start_time = st.slider("When do you expect to start?",value=datetime(2020,1,1,9,30),format="MM/DD/YYYY - hh:mm")
st.write("start time: ", start_time)

# forms
st.markdown("## Forms")
with st.form("form"):
    st.subheader("ML Model Entry Form")
    df_data = st.file_uploader("Upload your own data frame")
    x_features = st.multiselect("select the input features:",("Col 1","Col 2","Col 3"))
    y_features = st.text_input("Identify your output feature",placeholder="e.g feature 1")
    model_choice = st.radio("which ml model do u want to train?",["LinReg","LogReg"])
    epochs = st.slider("How many epoches for training process?",100,500,300)
    submitted = st.form_submit_button("Train the model")

if submitted:
    pass


# Metrics
st.markdown("## Metrics")
st.metric("up",f"${61.21}",f"{1.21}%")
st.metric("down",f"${125.2001:.2f}",f"{-5.4:.2f}%")

# DataFrames
st.markdown('## DataFrames')
start_date = datetime(2023,11,1)
end_date = datetime(2023,12,30)
df = pdr.DataReader('BAC','stooq',start=start_date,end=end_date)
st.dataframe(df.style.highlight_max(axis=0),use_container_width=True)

st.markdown('### Line chart')
st.line_chart(data=df,y=["Open","High","Low","Close"],width=0,height=0,use_container_width=True)

st.markdown('### Bar Chart')
st.bar_chart(data=df,y=["Open","High","Low","Close"],width=0,height=0,use_container_width=True)

st.markdown('### Map chart')
df2 = pd.DataFrame(np.random.randn(1000, 2)/[10,10]+[35.2,-0.641389],
                   columns=['lat','lon'])
st.map(df2)

st.markdown('### Plotly chart')
df = px.data.iris()
fig = px.scatter(df, x='sepal_length',y='sepal_width',color='species',size='petal_length')
st.plotly_chart(fig, use_container_width=True)

# Status Messages & Spinners
st.markdown("## Status Messages & Spinners")
st.info('Your model has been trained',icon="ℹ️")
st.error("An error has occured during training your model",icon="🕯️")
with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Model comletely trained')

# Progress Bars & Session state

st.markdown("## Progress Bars & Session state")
progress_text = "Model training in progress. Please wait"
my_bar = st.progress(0,text=progress_text)
for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete+1,text=progress_text)
time.sleep(1)

st.number_input("How many epoches?",key="epoches",min_value=100,max_value=300)
st.session_state.epoches

st.write(st.session_state)

# Sidebars
st.markdown("## Sidebars")
with st.sidebar:
    selected = option_menu("Multiple disease prediction system",["diabetes","heart","parkinsons"],icons=['activity','heart','person'],default_index=0)

# Tabs
st.markdown("## Tabs")
tab1,tab2 = st.tabs(["Heart disease","Diabetes Disease"])
with tab1:
    st.subheader("cardio")

with tab2:
    st.subheader("kidney failure")

# Columns
st.markdown("## Columns")
col1,col2 = st.columns(2)
with col1:
    st.subheader("cardio")
with col2: 
    st.subheader("kidney")

# Expanders
st.markdown("## Expanders")
with st.expander("heart"):
    st.subheader("cardio")

with st.expander("diabets"):
    st.subheader("kidney")