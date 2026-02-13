import streamlit as st
import pandas as pd
import joblib

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Honey Quality Dashboard",
    page_icon="🍯",
    layout="wide"
)

st.title("Honey Purity & Price Prediction Dashboard")

# load data and models
df = pd.read_csv("honey_dataset.csv")

purity_model = joblib.load("models/honey_purity_model.pkl")
price_model = joblib.load("models/honey_price_model.pkl")

feature_columns_purity = joblib.load("models/feature_columns_purity.pkl")
feature_columns_price = joblib.load("models/feature_columns_price.pkl")

# tabs
tab1, tab2 = st.tabs(["Prediction", "Data Analysis"])

# tab 1
with tab1:

    st.header("Enter Honey Parameters")

    col1, col2 = st.columns(2)

    with col1:
        CS = st.number_input("CS", step=0.01)
        Density = st.number_input("Density", step=0.01)
        WC = st.number_input("Water Content (WC)", step=0.01)
        pH = st.number_input("pH", step=0.01)

    with col2:
        EC = st.number_input("Electrical Conductivity (EC)", step=0.01)
        F = st.number_input("F", step=0.01)
        G = st.number_input("G", step=0.01)
        Viscosity = st.number_input("Viscosity", step=0.01)

    pollen_options = [col.replace("Pollen_analysis_", "")
                      for col in feature_columns_purity
                      if "Pollen_analysis_" in col]

    Pollen_analysis = st.selectbox("Pollen Analysis", pollen_options)

    if st.button("Predict"):

        input_dict = {
            "CS": CS,
            "Density": Density,
            "WC": WC,
            "pH": pH,
            "EC": EC,
            "F": F,
            "G": G,
            "Viscosity": Viscosity
        }

        input_df = pd.DataFrame([input_dict])

        pollen_column = f"Pollen_analysis_{Pollen_analysis}"
        input_df[pollen_column] = 1

        input_purity = input_df.reindex(columns=feature_columns_purity, fill_value=0)
        input_price = input_df.reindex(columns=feature_columns_price, fill_value=0)

        purity_prediction = purity_model.predict(input_purity)[0]
        price_prediction = price_model.predict(input_price)[0]

        st.subheader("Prediction Results")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Predicted Purity", f"{purity_prediction:.3f}")

        with col2:
            st.metric("Predicted Price (₹)", f"{price_prediction:.2f}")

# tab 2
with tab2:

    st.header("Exploratory Data Analysis")

    st.subheader("Correlation Matrix")
    st.image("plots/correlation_matrix.png")

    st.subheader("Feature Distribution")
    st.image("plots/feature_distribution.png")

    st.subheader("Price Distribution")
    st.image("plots/price_distribution.png")

    st.subheader("Price vs Purity")
    st.image("plots/price_vs_purity.png")

    st.subheader("Purity Model Comparison")
    st.image("plots/purity_model_comparison.png")

    st.subheader("Price Model Comparison")
    st.image("plots/price_model_comparison.png")

    st.subheader("Purity Actual vs Predicted")
    st.image("plots/purity_actual_vs_predicted.png")

    st.subheader("Price Actual vs Predicted")
    st.image("plots/price_actual_vs_predicted.png")
