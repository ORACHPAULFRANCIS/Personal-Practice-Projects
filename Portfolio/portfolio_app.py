
# portfolio_app.py (Canva-Inspired Version)
st.markdown('<meta name="theme-color" content="#ffffff">', unsafe_allow_html=True)
import streamlit as st

st.set_page_config(
    page_title="Orach Paul Francis | Portfolio",
    page_icon="🧰",
    layout="wide"
)

# -----------------------------
# Canva-Inspired CSS Styling
# -----------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(to right, #dbeafe, #e0f2fe) !important;
        color: #1f2937 !important;
    }

    /* Force consistent card and section colors in dark mode */
    .card, .stMarkdown, .stText, .stSubheader, .stTitle {
        color: #1f2937 !important;
        background-color: white !important;
    }

    .stButton>button {
        background-color: #2563eb;
        color: white;
        padding: 0.6rem 1.2rem;
        border-radius: 8px;
        font-size: 16px;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 10px rgba(37, 99, 235, 0.3);
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
    }

    .stImage>img {
        border-radius: 50%;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
    }

    h1, h2, h3 {
        color: #1e3a8a;
        font-weight: 800;
    }

    hr {
        border: none;
        height: 2px;
        background: #93c5fd;
        margin: 2rem 0;
    }

    /* 🔗 Link styling */
    a {
        color: #2563eb;
        text-decoration: none;
        font-weight: 600;
        transition: color 0.3s ease;
    }
    a:hover {
        color: #1d4ed8;
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
col1, col2 = st.columns([1, 2])
with col1:
    st.image("Portfolio/orach.jpg", width=200)
with col2:
    st.title("Orach Paul Francis")
    st.markdown("#### Top Problem Solving Voice | Petroleum Engineer | Python Coder | Chairperson Membership Committee (Geological Society of Uganda) | IWCF 1 | Petrophysics | Power BI | Agile Project Management | Solutions Architecture")
    st.markdown("""
    <div class='card'>
    Dynamic and results-driven Petroleum Engineer with strong expertise in subsurface data interpretation, formation evaluation, drilling planning, data analysis with python and technical project execution within the oil and gas sector.

Demonstrated success in aligning technical solutions with field operations, enhancing reservoir performance, and supporting HSE compliance across upstream operations. 

Skilled in Geolog, Petrel, Python, Numpy, Pandas, Matplotlib, Power BI, Streamlit, Flask and other industry-standard tools to deliver data-driven insights, optimize well planning, and drive operational excellence. 
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------
# Education
# -----------------------------
st.subheader("🎓 Education")
st.markdown("""
<div class='card'>
<b>Bachelor of Science in Oil and Gas Production</b><br>
Kyambogo University
<br><br>
More available on <a href='https://linkedin.com/in/orachpaulfrancis' target='_blank'>LinkedIn</a>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Featured Projects
# -----------------------------
st.subheader("🛠️ Featured Projects")

col3, col4 = st.columns(2)
with col3:
    st.markdown("""
    <div class='card'>
    🛢️ <b><a href='https://orach-oilfield-converter.streamlit.app/' target='_blank'>Oilfield Unit Converter</a></b><br>
    Web-based app for converting pressure, temperature, volume, flow rate, and more.
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class='card'>
    🧙‍♂️ <b><a href='https://orach.pythonanywhere.com/' target='_blank'>Sorting Hat Game</a></b><br>
    A fun web app inspired by Harry Potter’s Sorting Hat — coded in Flask.
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# Key Skills
# -----------------------------
st.subheader("🔧 Key Skills")

col5, col6 = st.columns(2)
with col5:
    st.markdown("""
    <div class='card'>
    - Log Analysis (Determin, Multimin)<br>
    - Geolog, Techlog, Petrel<br>
    - Python, Pandas, Streamlit<br>
    - ArcGIS, QGIS, Surfer<br>
    - Digital Oilfield Integration<br>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class='card'>
    - Well Log Interpretation<br>
    - HSE & Field Safety Compliance<br>
    - Agile & Scrum Methodologies<br>
    - Power BI, Data Viz & Dashboards<br>
    - Team Collaboration & Project Management
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# Connect With Me
# -----------------------------
st.subheader("🔗 Connect With Me")
st.markdown("""
<div class='card' style='line-height: 2; font-size: 16px;'>
📫 You can find me on: <br>
<a href='https://linkedin.com/in/orachpaulfrancis' target='_blank'>LinkedIn</a> |
<a href='https://github.com/ORACHPAULFRANCIS' target='_blank'>GitHub</a> |
<a href='https://www.kaggle.com/orachpaulfrancis' target='_blank'>Kaggle</a> |
<a href='https://www.hackerrank.com/profile/orachpf' target='_blank'>HackerRank</a> |
<a href='https://www.codedex.io/@Orach' target='_blank'>Codedex</a> |
<a href='https://learn.microsoft.com/en-us/users/orachpaulfrancis-0241/achievements' target='_blank'>Microsoft Learn</a>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# Footer
# -----------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; font-size:14px;'>Created with ❤️ using Streamlit | © 2025 Orach Paul Francis</div>", unsafe_allow_html=True)
