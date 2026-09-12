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
        "ASUS",
        "Lenovo",
        "HP",
        "Dell",
        "Acer",
        "MSI",
        "Samsung",
        "Apple",
        "Infinix",
        "Microsoft",
        "Other"
    ]
)

RAM_Expandable = st.selectbox(
    "RAM Expandable",
    [
        "Not Expandable",
        "4 GB Expandable",
        "8 GB Expandable",
        "12 GB Expandable",
        "16 GB Expandable",
        "32 GB Expandable",
        "48 GB Expandable",
        "64 GB Expandable",
        "Other"
    ]
)

RAM_TYPE = st.selectbox(
    "RAM Type",
    [
        "DDR4 RAM",
        "DDR5 RAM",
        "LPDDR5 RAM",
        "LPDDR4X RAM",
        "LPDDR5X RAM",
        "DDR3 RAM",
        "LPDDR3 RAM",
        "LPDDR4 RAM",
        "DDR2 RAM",
        "Unknown"
    ]
)

Ghz = st.number_input(
    "Processor Speed (GHz)",
    min_value=0.5,
    max_value=6.0,
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
        "MediaTek",
        "Qualcomm",
        "ARM",
        "Microsoft",
        "ATI",
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
        "Dedicated/Unknown"
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
        "Core Ultra 5",
        "Core Ultra 7",
        "Core Ultra 9",
        "Ryzen 3",
        "Ryzen 5",
        "Ryzen 7",
        "Ryzen 9",
        "Celeron",
        "Pentium",
        "Athlon",
        "Snapdragon",
        "MediaTek",
        "Apple",
        "Other"
    ]
)

Laptop_Type = st.selectbox(
    "Laptop Type",
    [
        "General",
        "Gaming",
        "Ultrabook",
        "2-in-1",
        "Chromebook",
        "MacBook"
    ]
)

if st.button("Predict Laptop Price"):

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
        f"Predicted Laptop Price: ₹{prediction:,.0f}"
    )