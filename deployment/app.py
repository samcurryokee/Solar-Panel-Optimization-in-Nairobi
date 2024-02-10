import streamlit as st
from joblib import load
from keras.models import load_model
import pandas as pd
import base64

# Function to convert image to Base64


def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


image_path = 'solar.jpg'
image_bytes = get_base64_of_bin_file(image_path)

bg_image = f'''
<style>
.stApp {{
    background-image: url("data:image/jpeg;base64,{image_bytes}");
    background-size: cover;
}}
</style>
'''

st.markdown(bg_image, unsafe_allow_html=True)
# # Load the trained model
model = load_model('keras_model.h5')


def solar_energy_prediction():
    st.markdown("<h1 style='color: black;'>SunOptimize Technologies</h1>",
                unsafe_allow_html=True)

    # Sidebar for user input
    st.sidebar.header('Input Parameters')

    # Input fields for each feature
    surface_area = st.sidebar.number_input('Surface Area', value=500)
    potential_installable_area = st.sidebar.number_input(
        'Potential Installable Area', value=500)
    peak_installable_capacity = st.sidebar.number_input(
        'Peak Installable Capacity', value=500)
    estimated_tilt = st.sidebar.number_input('Estimated Tilt Angle', value=45)
    estimated_building_height = st.sidebar.number_input(
        'Estimated Building Height', value=50)
    estimated_capacity_factor = st.sidebar.number_input(
        'Estimated Capacity Factor', value=0.85, step=0.01)

    # Encoding for Assumed Building Type
    building_type_encoding = {
        'single family residential':   0.667723,
        'multi-family residential':   0.138512,
        'commercial':   0.058657,
        'public':   0.053359,
        'industrial':   0.046109,
        'peri-urban settlement':   0.035641
    }

    # Options for the categorical variable
    building_types = list(building_type_encoding.keys())
    assumed_building_type = st.sidebar.selectbox(
        'Assumed Building Type', building_types)

    # Encode the selected building type
    encoded_building_type = building_type_encoding[assumed_building_type]

    # Prepare input data for prediction
    input_data = pd.DataFrame({
        'Surface_area': [surface_area],
        'Potential_installable_area': [potential_installable_area],
        'Peak_installable_capacity': [peak_installable_capacity],
        'Assumed_building_type': [encoded_building_type],
        'Estimated_tilt': [estimated_tilt],
        'Estimated_building_height': [estimated_building_height],
        'Estimated_capacity_factor': [estimated_capacity_factor]
    })

    # Additional input field for the inputted value
    inputted_value = st.sidebar.number_input(
        'Current yearly energy consumption in units')

    # Make predictions
    prediction = model.predict(input_data)

    # Display prediction with larger font, black color, and bold style
    st.markdown("<h2 style='font-size:  2em; color: black; font-weight: bold;'>Solar Energy Potential Prediction:</h2>",
                unsafe_allow_html=True)
    st.markdown("<p style='font-size:  1.5em; color: black; font-weight: bold;'>The predicted energy potential per year in KWh is: {}</p>".format(
        prediction[0]), unsafe_allow_html=True)

    # Recommendations with larger font, black color, and bold style
    if prediction[0] < inputted_value:
        st.markdown(
            "<h2 style='font-size:  2em; color: black; font-weight: bold;'>Recommendation:</h2>", unsafe_allow_html=True)
        st.markdown(
            "<p style='font-size:  1.5em; color: black; font-weight: bold;'>No adoption is recommended.</p>", unsafe_allow_html=True)
    elif prediction[0] <= inputted_value * 1.2:
        st.markdown(
            "<h2 style='font-size:  2em; color: black; font-weight: bold;'>Recommendation:</h2>", unsafe_allow_html=True)
        st.markdown(
            "<p style='font-size:  1.5em; color: black; font-weight: bold;'>Hybrid adoption is acceptable.</p>", unsafe_allow_html=True)
    else:
        st.markdown(
            "<h2 style='font-size:  2em; color: black; font-weight: bold;'>Recommendation:</h2>", unsafe_allow_html=True)
        st.markdown(
            "<p style='font-size:  1.5em; color: black; font-weight: bold;'>Full adoption of solar is recommended.</p>", unsafe_allow_html=True)
# Function for Potential Installable Area


def potential_installable_area():
    # Load the trained model
    rf_model = load('randomForest.joblib')

    # Streamlit app
    st.markdown("<h1 style='color: black;'>SunOptimize Technologies</h1>",
                unsafe_allow_html=True)

    # Sidebar for user input
    st.sidebar.header('Input Parameters')

    # Define input fields for each feature
    surface_area = st.sidebar.number_input('Surface Area', value=0)
    estimated_tilt = st.sidebar.number_input('Estimated Tilt', value=0)
    estimated_building_height = st.sidebar.number_input(
        'Estimated Building Height', value=0)

    # Button to trigger prediction
    if st.button('Predict'):
        # Prepare input data for prediction
        input_data = pd.DataFrame({
            'Surface_area': [surface_area],
            'Estimated_tilt': [estimated_tilt],
            'Estimated_building_height': [estimated_building_height]
        })

        # Make predictions
        prediction = rf_model.predict(input_data)

        # Display prediction
        st.markdown("<p style='font-size:  1.5em; color: black; font-weight: bold;'>The predicted potential installable area is :{}</p>".format(
        prediction[0]), unsafe_allow_html=True)

# Main function to run the app


def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio(
        "Go to", ["Solar Energy Prediction", "Potential Installable Area"])

    if selection == "Solar Energy Prediction":
        # Code for the solar energy prediction app goes here
        solar_energy_prediction()
    elif selection == "Potential Installable Area":
        potential_installable_area()

 # Run the app
if __name__ == "__main__":
    main()
