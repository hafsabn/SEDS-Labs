import pandas as pd
import streamlit as st
import yfinance as yf
from pages.file_2 import date_range_selector
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

# Title
st.markdown("# :blue[Challenge 2]")

# Fetch date range
start_date, end_date = date_range_selector()

# Fetch Bitcoin data
btc_yf_df = yf.download('BTC-USD', start=start_date, end=end_date, interval='1d')

if not btc_yf_df.empty:
    btc_yf_df.columns = ['_'.join(map(str, col)) for col in btc_yf_df.columns]
    btc_yf_df.columns = btc_yf_df.columns.str.lower()
    btc_yf_df = btc_yf_df.rename(columns={
        'date_': 'date',
        'adj close_btc-usd': 'adj close',
        'close_btc-usd': 'close',
        'high_btc-usd': 'high',
        'low_btc-usd': 'low',
        'open_btc-usd': 'open',
        'volume_btc-usd': 'volume'
    })
    btc_yf_df.columns = btc_yf_df.columns.str.lower()
    btc_yf_df.index = btc_yf_df.index.date

    if 'adj close' in btc_yf_df.columns:
        btc_yf_df.drop(columns=['adj close'], inplace=True)
else:
    st.warning("Data could not be loaded. Check your connection or API settings.")

# Interactive Tabs
tab1, tab2, tab3 = st.tabs(["Data Overview", "Visualizations", "ML Prediction"])

# --- Tab 1: Data Overview ---
with tab1:
    st.subheader("Data Overview")
    if not btc_yf_df.empty:
        st.write(btc_yf_df)
        st.write(f"Data contains {btc_yf_df.shape[0]} rows and {btc_yf_df.shape[1]} columns.")
    else:
        st.warning("No data available for the selected date range.")

# --- Tab 2: Visualizations ---
with tab2:
    st.subheader("Visualizations")
    if not btc_yf_df.empty:
        # Line chart for price trends
        fig = px.line(btc_yf_df.reset_index(), x='index', y='close', title="Bitcoin Close Price Trend")
        st.plotly_chart(fig)

        # Correlation heatmap
        corr_matrix = btc_yf_df.corr()
        fig_corr = px.imshow(corr_matrix, text_auto=True, title="Correlation Matrix")
        st.plotly_chart(fig_corr)
    else:
        st.warning("No data available for visualization.")

# --- Tab 3: Machine Learning Prediction ---
with tab3:
    st.subheader("Machine Learning Prediction")
    if not btc_yf_df.empty:
        btc_yf_df['Prediction'] = btc_yf_df['close'].shift(-1)
        btc_yf_df = btc_yf_df.dropna() 
        # Preprocessing for prediction
        X = btc_yf_df[['close']]  # Use Close price as the feature
        y = btc_yf_df['Prediction']  # Target is the next day's price

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        # Create DataFrame for plotting
        prediction_df = pd.DataFrame({
        'Actual': y_test.values,
        'Predicted': y_pred
        }, index=X_test.index)

        # Line plot for actual vs predicted values
        fig_pred = px.line(
        prediction_df,
        title="Bitcoin Price (Actual vs Predicted)",
        labels={'value': 'Price', 'index': 'Date'},
        template="plotly_dark"
        )
        st.plotly_chart(fig_pred)


        # Scatter plot for prediction vs actual
        pred_df = pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred})
        fig_pred = px.scatter(pred_df, x='Actual', y='Predicted', title="Prediction vs Actual")
        st.plotly_chart(fig_pred)

        st.write("### Model Evaluation")
        st.write(f":red[Mean Squared Error:] {mse:.2f}")
        st.write(f":red[R-squared:] {r2}")
    else:
        st.warning("No data available for prediction.")
