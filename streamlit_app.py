# streamlit_app.py (Enhanced UI Version)

import streamlit as st

# ----------------------------
# UI Settings
# ----------------------------
st.set_page_config(
    page_title="Oilfield Converter",
    page_icon="🛢️",
    layout="centered"
)

st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
        font-family: 'Segoe UI', sans-serif;
    }
    .stButton > button {
        background-color: #007ACC;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
    }
    .stSelectbox > div, .stTextInput > div, .stNumberInput > div {
        border-radius: 10px;
    }
    .block-container {
        padding-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("🛢️ Oilfield Unit Converter")
st.subheader("Quickly convert oilfield parameters with precision.")

# ----------------------------
# Unit Dictionaries
# ----------------------------
pressure_units = {
    "pa": 1,
    "kpa": 1000,
    "mpa": 1_000_000,
    "bar": 100000,
    "mbar": 100,
    "kg/cm2": 98066.5,
    "mmhg": 133.322,
    "cmh2o": 98.0665,
    "mmh2o": 9.80665,
    "psi": 6894.76,
    "psf": 47.8803,
    "inhg": 3386.39,
    "inh2o": 249.0889,
    "atm": 101325,
    "at": 98066.5,
    "torr": 133.322,
}

volume_units = {
    'l': 1,
    'ml': 0.001,
    'bbl': 158.987,
    'm3': 1000,
    'cm3': 0.001,
    'gal': 3.78541,
    'ft3': 28.3168,
    'in3': 0.0163871
}

depth_units = {
    'm': 1,
    'km': 1000,
    'cm': 0.01,
    'mm': 0.001,
    'ft': 0.3048,
    'in': 0.0254,
    'yd': 0.9144,
    'mi': 1609.34
}

density_units = {
    'kg/m3': 1,
    'g/cm3': 1000,
    'lb/ft3': 16.0185,
    'lb/gal': 119.826
}

flow_units = {
    'l/s': 1,
    'l/min': 1 / 60,
    'm3/h': 1000 / 3600,
    'bbl/d': 158.987 / 86400,
    'bbl/h': 158.987 / 3600,
    'gpm': 3.78541 / 60
}

temp_units = ['c', 'f', 'k', 'r', 'de', 'n', 're', 'ro']

def to_kelvin(value, unit):
    conversions = {
        'c': lambda x: x + 273.15,
        'f': lambda x: (x - 32) * 5/9 + 273.15,
        'k': lambda x: x,
        'r': lambda x: x * 5/9,
        'de': lambda x: 373.15 - x * 2/3,
        'n': lambda x: x * 100/33 + 273.15,
        're': lambda x: x * 5/4 + 273.15,
        'ro': lambda x: (x - 7.5) * 40/21 + 273.15,
    }
    return conversions[unit](value)

def from_kelvin(kelvin, unit):
    conversions = {
        'c': lambda x: x - 273.15,
        'f': lambda x: (x - 273.15) * 9/5 + 32,
        'k': lambda x: x,
        'r': lambda x: x * 9/5,
        'de': lambda x: (373.15 - x) * 3/2,
        'n': lambda x: (x - 273.15) * 33/100,
        're': lambda x: (x - 273.15) * 4/5,
        'ro': lambda x: (x - 273.15) * 21/40 + 7.5,
    }
    return conversions[unit](kelvin)

# ----------------------------
# Parameter Selector
# ----------------------------
parameter = st.selectbox("📌 Select parameter to convert:", ["Pressure", "Temperature", "Volume", "Depth", "Density", "Flow Rate"])

col1, col2 = st.columns(2)
value = col1.number_input("🔢 Enter value", format="%f")

if parameter == "Pressure":
    from_unit = col1.selectbox("From Unit", pressure_units.keys())
    to_unit = col2.selectbox("To Unit", pressure_units.keys())
    if st.button("Convert Pressure"):
        pa = value * pressure_units[from_unit]
        result = pa / pressure_units[to_unit]
        st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")

elif parameter == "Temperature":
    from_unit = col1.selectbox("From Unit", temp_units)
    to_unit = col2.selectbox("To Unit", temp_units)
    if st.button("Convert Temperature"):
        kelvin = to_kelvin(value, from_unit)
        result = from_kelvin(kelvin, to_unit)
        st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")

elif parameter == "Volume":
    from_unit = col1.selectbox("From Unit", volume_units.keys())
    to_unit = col2.selectbox("To Unit", volume_units.keys())
    if st.button("Convert Volume"):
        liters = value * volume_units[from_unit]
        result = liters / volume_units[to_unit]
        st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")

elif parameter == "Depth":
    from_unit = col1.selectbox("From Unit", depth_units.keys())
    to_unit = col2.selectbox("To Unit", depth_units.keys())
    if st.button("Convert Depth"):
        meters = value * depth_units[from_unit]
        result = meters / depth_units[to_unit]
        st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")

elif parameter == "Density":
    from_unit = col1.selectbox("From Unit", density_units.keys())
    to_unit = col2.selectbox("To Unit", density_units.keys())
    if st.button("Convert Density"):
        kg_m3 = value * density_units[from_unit]
        result = kg_m3 / density_units[to_unit]
        st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")

elif parameter == "Flow Rate":
    from_unit = col1.selectbox("From Unit", flow_units.keys())
    to_unit = col2.selectbox("To Unit", flow_units.keys())
    if st.button("Convert Flow Rate"):
        base = value * flow_units[from_unit]
        result = base / flow_units[to_unit]
        st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Orach Paul Francis")
st.markdown("🔗 [View Source on GitHub](https://github.com/yourusername/oilfield-unit-converter)")
