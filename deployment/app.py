import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('Neural_networks.joblib')

# Streamlit app
st.title('Solar Energy Potential Prediction')

# Sidebar for user input
st.sidebar.header('Input Parameters')

# Input fields for each feature
surface_area = st.sidebar.number_input('Surface Area', value=500)
potential_installable_area = st.sidebar.number_input('Potential Installable Area', value=500)
peak_installable_capacity = st.sidebar.number_input('Peak Installable Capacity', value=500)
# Options for the categorical variable
building_types = ['single family residential', 'multi-family residential', 'commercial', 'public', 'industrial', 'peri-urban settlement']
assumed_building_type = st.sidebar.multiselect('Assumed Building Type', building_types)
estimated_tilt = st.sidebar.number_input('Estimated Tilt Angle', value=45)
estimated_building_height = st.sidebar.number_input('Estimated Building Height', value=50)
estimated_capacity_factor = st.sidebar.number_input('Estimated Capacity Factor', value=0.85, step=0.01)

# Prepare input data for prediction
input_data = pd.DataFrame({
    'Surface_area': [surface_area],
    'Potential_installable_area': [potential_installable_area],
    'Peak_installable_capacity': [peak_installable_capacity],
    'Assumed_building_type': [assumed_building_type],
    'Estimated_tilt': [estimated_tilt],
    'Estimated_building_height': [estimated_building_height],
    'Estimated_capacity_factor': [estimated_capacity_factor]
})


# Make predictions
prediction = model.predict(input_data)

# Display prediction
st.subheader('Prediction:')
st.write(f'The predicted energy potential per year is: {prediction[0]}')
