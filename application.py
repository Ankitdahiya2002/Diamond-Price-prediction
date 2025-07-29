import streamlit as st
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

st.set_page_config(page_title="Diamond Price Prediction", layout="centered")

st.title("💎 Diamond Price Predictor")

st.markdown("Fill in the features below to get the predicted price of the diamond.")

with st.form("prediction_form"):
    carat = st.number_input("Carat", min_value=0.0, step=0.01)
    depth = st.number_input("Depth", min_value=0.0, step=0.1)
    table = st.number_input("Table", min_value=0.0, step=0.1)
    x = st.number_input("X (length in mm)", min_value=0.0, step=0.01)
    y = st.number_input("Y (width in mm)", min_value=0.0, step=0.01)
    z = st.number_input("Z (depth in mm)", min_value=0.0, step=0.01)

    cut = st.selectbox("Cut", ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
    color = st.selectbox("Color", ['D', 'E', 'F', 'G', 'H', 'I', 'J'])
    clarity = st.selectbox("Clarity", ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])

    submit = st.form_submit_button("Predict")

if submit:
    try:
        data = CustomData(
            carat=carat,
            depth=depth,
            table=table,
            x=x,
            y=y,
            z=z,
            cut=cut,
            color=color,
            clarity=clarity
        )
        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data)

        st.success(f"💰 Predicted Diamond Price: ${round(pred[0], 2)}")
    except Exception as e:
        st.error(f"Error: {str(e)}")
