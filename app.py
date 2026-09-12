import streamlit as st
import pandas as pd
import pickle

with open("pipe.pkl", "rb") as file:
    pipe = pickle.load(file)

st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="centered"
)

st.title("💻 Laptop Price Predictor")
st.write("Enter the laptop specifications to predict its price.")

Brand = st.selectbox(
    "Brand",
    [
        "Dell",
        "HP",
        "Lenovo",
        "ASUS",
        "Acer",
        "MSI",
        "Apple",
        "Samsung",
        "Microsoft",
        "Other"
    ]
)

RAM_Expandable = st.text_input(
    "RAM Expandable",
    placeholder="Example: Up to 32 GB"
)

RAM_TYPE = st.selectbox(
    "RAM Type",
    [
        "DDR4",
        "DDR5",
        "LPDDR4",
        "LPDDR4X",
        "LPDDR5",
        "LPDDR5X",
        "DDR3",
        "Other"
    ]
)

Ghz = st.number_input(
    "Processor Speed (GHz)",
    min_value=0.0,
    max_value=10.0,
    value=2.5,
    step=0.1
)

GPU_Brand = st.selectbox(
    "GPU Brand",
    [
        "Intel",
        "NVIDIA",
        "AMD",
        "Apple",
        "Integrated",
        "Other"
    ]
)

RAM_GB = st.number_input(
    "RAM (GB)",
    min_value=2,
    max_value=128,
    value=8,
    step=2
)

Display_inches = st.number_input(
    "Display Size (inches)",
    min_value=10.0,
    max_value=20.0,
    value=15.6,
    step=0.1
)

GPU_Type = st.selectbox(
    "GPU Type",
    [
        "Integrated",
        "Dedicated",
        "NVIDIA GeForce",
        "AMD Radeon",
        "Intel Iris",
        "Other"
    ]
)

SSD_GB = st.number_input(
    "SSD Storage (GB)",
    min_value=0,
    max_value=8000,
    value=512,
    step=128
)

Processor_Family = st.selectbox(
    "Processor Family",
    [
        "Core i3",
        "Core i5",
        "Core i7",
        "Core i9",
        "Ryzen 3",
        "Ryzen 5",
        "Ryzen 7",
        "Ryzen 9",
        "Apple M1",
        "Apple M2",
        "Apple M3",
        "Snapdragon",
        "Other"
    ]
)

Laptop_Type = st.selectbox(
    "Laptop Type",
    [
        "Gaming",
        "Business",
        "Ultrabook",
        "Student",
        "2 in 1",
        "Workstation",
        "Other"
    ]
)

if st.button("🔮 Predict Laptop Price"):

    input_data = pd.DataFrame({
        "Brand": [Brand],
        "RAM_Expandable": [RAM_Expandable],
        "RAM_TYPE": [RAM_TYPE],
        "Ghz": [Ghz],
        "GPU_Brand": [GPU_Brand],
        "RAM_GB": [RAM_GB],
        "Display_inches": [Display_inches],
        "GPU_Type": [GPU_Type],
        "SSD_GB": [SSD_GB],
        "Processor_Family": [Processor_Family],
        "Laptop_Type": [Laptop_Type]
    })

    prediction = pipe.predict(input_data)[0]

    st.success(
        f"💰 Predicted Laptop Price: ₹{prediction:,.0f}"
    )