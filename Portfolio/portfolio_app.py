# portfolio_app.py (Enhanced Aesthetic Version)

import streamlit as st

st.set_page_config(
    page_title="Orach Paul Francis | Portfolio",
    page_icon="🧰",
    layout="centered"
)

# -----------------------------
# Custom CSS for Aesthetic Styling
# -----------------------------
st.markdown("""
<style>
    body {
        background-color: #f0f4f8;
    }
    .main {
        background: linear-gradient(135deg, #f0f4f8, #e6f0fa);
        font-family: 'Segoe UI', sans-serif;
        padding: 2rem;
        border-radius: 15px;
    }
    .stButton>button {
        background-color: #007ACC;
        color: white;
        padding: 10px 24px;
        border-radius: 10px;
        font-size: 16px;
        border: none;
        transition: 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton>button:hover {
        background-color: #005b99;
    }
    .stMarkdown h1, h2, h3, h4 {
        color: #003366;
    }
    .css-1aumxhk {
        max-width: 900px;
        margin: auto;
    }
    .stImage>img {
        border-radius: 50%;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    hr {
        border: none;
        height: 1px;
        background: #007ACC;
        margin-top: 20px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
col1, col2 = st.columns([1, 3])
with col1:
    st.image("Portfolio/orach.jpg", width=150)
with col2:
    st.title("Orach Paul Francis")
    st.subheader("Problem Solver | Petroleum Engineer | Python Developer | Agile Project Manager")
    st.markdown("""
    Dynamic and results-driven Petroleum Engineer with strong expertise in formation evaluation,
    well log interpretation, digital oilfield integration, and oilfield safety solutions. Proficient in
    Geolog, Techlog, Petrel, Python, and geospatial tools like ArcGIS and QGIS. Passionate about
    bridging petroleum engineering with software innovation for upstream success.
    """)

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------
# Education & Certifications
# -----------------------------
st.header("🎓 Education")
col3, col4 = st.columns(2)
with col3:
    st.write("**BSc. Oil and Gas Production**")
    st.caption("Kyambogo University")
with col4:
    st.write("**More on LinkedIn**")
    st.markdown("[View Profile](https://linkedin.com/in/orachpaulfrancis)")

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------
# Featured Projects
# -----------------------------
st.header("🛠️ Featured Projects")

col5, col6 = st.columns(2)
with col5:
    st.markdown("""
    - 🛢️ [Oilfield Unit Converter](https://orach-oilfield-converter.streamlit.app/):
      Convert pressure, temperature, volume, flow rate, and more.
    """)
with col6:
    st.markdown("""
    - 🧙‍♂️ [Sorting Hat Game](https://orach.pythonanywhere.com/):
      Fun logic-based web app inspired by the Harry Potter Sorting Hat.
    """)

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------
# Key Skills
# -----------------------------
st.header("🔧 Key Skills")

col7, col8 = st.columns(2)
with col7:
    st.markdown("""
    - Log Analysis (Determin, Multimin)
    - Formation Evaluation (Geolog, Techlog, Petrel)
    - Python, Pandas, Matplotlib
    - Streamlit App Development
    - Geospatial Analysis (ArcGIS, QGIS, Surfer)
    - Digital Oilfield Integration
    - Data Visualization & Analysis (Power BI)
    """)
with col8:
    st.markdown("""
    - Well Log Interpretation
    - Scrum & Agile Methodologies
    - HSE Compliance & Field Safety
    - Project Management & Planning
    - Strategic Planning & Execution
    - Communication & Team Leadership
    - Continuous Learning & Adaptability
    """)

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------
# Links
# -----------------------------
st.header("🔗 Connect With Me")
st.markdown("""
📫 **Contact Me:**  
[LinkedIn](http://linkedin.com/in/orachpaulfrancis) | [GitHub](http://github.com/ORACHPAULFRANCIS) |
[Kaggle](https://www.kaggle.com/orachpaulfrancis) | [HackerRank](https://www.hackerrank.com/profile/orachpf) |
[Codedex](https://www.codedex.io/@Orach) | [Microsoft Learn](https://learn.microsoft.com/en-us/users/orachpaulfrancis-0241/achievements)
""")

# -----------------------------
# Footer
# -----------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("Created with ❤️ using Streamlit | © 2025 Orach Paul Francis")
