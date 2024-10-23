import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model

# Load the saved PyCaret model pipeline
model_pipeline = load_model('lr_breast_cancer_classifier')

# Streamlit UI
st.title('Breast Cancer Classification')

# Input fields for features
texture_worst = st.number_input('Worst Texture', min_value=0.0, step=0.00001)
concavity_worst = st.number_input('Worst Concavity', min_value=0.0, step=0.00001)
radius_se = st.number_input('Standard Error Radius', min_value=0.0, step=0.00001)
smoothness_worst = st.number_input('Worst Smoothness', min_value=0.0, step=0.00001)
symmetry_worst = st.number_input('Worst Symmetry', min_value=0.0, step=0.00001)
concavity_mean = st.number_input('Mean Concavity', min_value=0.0, step=0.00001)
fractal_dimension_se = st.number_input('Standard Error fractal dimension', min_value=0.0, step=0.00001)
area_se = st.number_input('Standard Error area', min_value=0.0, step=0.00001)




# Prediction button
if st.button('Classify'):
    # Create a DataFrame with the input values
    input_data = pd.DataFrame({
        'texture_worst': [texture_worst],
        'concavity_worst': [concavity_worst],
        'radius_se': [radius_se],
        'smoothness_worst': [smoothness_worst],
        'symmetry_worst': [symmetry_worst],
        'concavity_mean': [concavity_mean],
        'fractal_dimension_se' :[fractal_dimension_se],
        'area_se':[area_se]
    })

    # Make predictions using the loaded model pipeline
    prediction = predict_model(model_pipeline, data=input_data)
    prediction_label = "Malignant" if prediction['prediction_label'][0] == 1 else "Benign"
    prediction_score = prediction['prediction_score'][0]  

    # Display the prediction
    st.write(f'Prediction: {prediction_label}')
    st.write(f'Prediction Score:{prediction_score}')