import streamlit as st 
from datetime import  date
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    file_path = "data/btc_df_cleaned.csv"
    data = pd.read_csv(file_path)
    return data

data = load_data()
st.markdown("# Challenge 1: :blue[Bitcoin Price Analysis]")

# DataFrames
st.markdown('## DataFrame')
st.dataframe(data.head())

# slider
data['Date'] = pd.to_datetime(data['Date'], errors='coerce').dt.date
data = data.dropna(subset=['Date'])
min_date = data['Date'].min()
max_date = data['Date'].max()
time_range = st.slider("Filter by Date Range:",value=(date(2018,10,22),date(2018,12,22)),format="MM/DD/YYYY",min_value=min_date,max_value=max_date)

price_feature = st.selectbox(
    "Choose a feature to analyze:",
    options=['open', 'close', 'high', 'low'],
    index=1  # Default to 'close'
)

selected_price = data[(data['Date'] >= time_range[0]) & (data['Date'] <= time_range[1])]
st.write("The ",price_feature ,"prices in ", time_range[0]," to ",time_range[1] ,"are: ")
st.write(selected_price[['Date', price_feature]])

# Analysis Modules
st.markdown("## :blue[Analysis Modules]")

# Calculate and display descriptive statistics for the selected date range
if not selected_price.empty:
    st.write("### Descriptive Statistics for the Selected Date Range:")
    st.write(selected_price.describe())
else:
    st.warning("No data available for the selected date range.")


# Interactive Visualizations
st.markdown("## :blue[Interactive Visualizations]")

# Price trend analysis: Line Chart
label = price_feature + " Price"
st.write("### Price Trend Analysis")
plt.figure(figsize=(10, 5))
plt.plot(selected_price['Date'], selected_price[price_feature], label=label,color='#60B4ED')
plt.title("Bitcoin Price Trend")
plt.xlabel("Date")
plt.ylabel(label)
plt.legend()
st.pyplot(plt)

# Advanced statistical visualization: Box Plot
st.write("### Advanced Statistical Visualization")
plt.figure(figsize=(5, 5))
plt.boxplot(selected_price[price_feature], vert=False, patch_artist=True,boxprops=dict(facecolor='#60B4ED', color='#60B4ED'))
plt.title("Box Plot of Bitcoin Prices")
plt.xlabel(label)
st.pyplot(plt)