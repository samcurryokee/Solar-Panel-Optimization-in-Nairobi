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

    # Display prediction with larger font, black color, and bold style
    st.markdown("<h2 style='font-size:  2.5em; color: white; font-weight: bold;'>Solar Energy Potential Prediction:</h2>",
                unsafe_allow_html=True)
    st.markdown("<p style='font-size:  2em; color: white; font-weight: bold;'>The predicted energy potential per year in KWh is: {}</p>".format(
        prediction[0]), unsafe_allow_html=True)

    # Recommendations with larger font, black color, and bold style
    if prediction[0] < inputted_value:
        st.markdown(
            "<h2 style='font-size:  2.5em; color: white; font-weight: bold;'>Recommendation:</h2>", unsafe_allow_html=True)
        st.markdown(
            "<p style='font-size:  2em; color: white; font-weight: bold;'>No adoption is recommended.</p>", unsafe_allow_html=True)
    elif prediction[0] <= inputted_value * 1.2:
        st.markdown(
            "<h2 style='font-size:  2.5em; color: white; font-weight: bold;'>Recommendation:</h2>", unsafe_allow_html=True)
        st.markdown(
            "<p style='font-size:  2em; color: white; font-weight: bold;'>Hybrid adoption is acceptable.</p>", unsafe_allow_html=True)
    else:
        st.markdown(
            "<h2 style='font-size:  2.5em; color: white; font-weight: bold;'>Recommendation:</h2>", unsafe_allow_html=True)
        st.markdown(
            "<p style='font-size:  2em; color: white; font-weight: bold;'>Full adoption of solar is recommended.</p>", unsafe_allow_html=True)
# Function for Potential Installable Area

def potential_installable_area():
        # Load the trained model
        rf_model = load('randomForest.joblib')

        # Streamlit app
        st.markdown("<h1 style='color: black;'>SUNOPTIMIZE TECHNOLOGIES</h1>",
                    unsafe_allow_html=True)

        # Sidebar for user input
        st.sidebar.header('Input Parameters')

        # Define input fields for each feature
        surface_area = st.sidebar.number_input('Surface Area', value=0)
        estimated_tilt_category = st.sidebar.selectbox(
        'Tilt Angle Category', options=['High', 'Moderate', 'Low',"flat"])
        estimated_tilt = {
        'High':  45,
        'Moderate':  30,
        'Low':  15,
        "flat": 1
        }[estimated_tilt_category]
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
# Make predictions
prediction = model.predict(input_data)

            # Display prediction
            st.markdown("<p style='font-size:  2em; color: white; font-weight: bold;'>The predicted potential installable area is :{}</p>".format(
                prediction[0]), unsafe_allow_html=True)

# Main function to run the app


def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio(
        "Go to", ["Potential Installable Area","Solar Energy Prediction"])

    if selection == "Solar Energy Prediction":
        # Code for the solar energy prediction app goes here
        solar_energy_prediction()
    elif selection == "Potential Installable Area":
        potential_installable_area()


 # Run the app
if __name__ == "__main__":
    main()
# Display prediction
st.subheader('Prediction:')
st.write(f'The predicted energy potential per year is: {prediction[0]}')
