# portfolio_app.py (Refined Canva-Inspired Version)
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
    background-color: rgb(255, 255, 255);
    color: rgb(33, 33, 33);
  }

  .card, .stMarkdown, .stText, .stSubheader, .stTitle {
    background-color: rgb(240, 248, 245);
    color: rgb(33, 33, 33);
    padding: 1rem;
    border-radius: 8px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
  }

  .stButton > button {
    background-color: rgb(0, 128, 90);
    color: white;
    padding: 0.6rem 1.2rem;
    border: none;
    border-radius: 6px;
    font-weight: 600;
    box-shadow: 0 3px 8px rgba(0, 128, 90, 0.3);
    transition: background 0.3s ease;
  }
  .stButton > button:hover {
    background-color: rgb(0, 153, 110);
  }

  h1, h2, h3 {
    color: rgb(0, 102, 72);
    font-weight: 800;
  }

  a {
    color: rgb(0, 128, 90);
    text-decoration: none;
    transition: color 0.2s ease;
  }
  a:hover {
    color: rgb(0, 153, 110);
    text-decoration: underline;
  }

  hr {
    border: none;
    height: 2px;
    background-color: rgb(0, 128, 90);
    margin: 2rem 0;
  }

  .stImage > img {
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  }
</style>


""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
col1, col2 = st.columns([1, 2])
with col1:
    st.markdown("""
    <img src='Portfolio/orach.jpg' style='width:100%; border-radius: 50%; box-shadow: 0 6px 12px rgba(0,0,0,0.1);'/>
    """, unsafe_allow_html=True)
with col2:
    st.title("Orach Paul Francis")
    st.markdown("#### Top Problem Solving Voice | Petroleum Engineer | Python Coder | Chairperson Membership Committee (Geological Society of Uganda) | IWCF 1 | Petrophysics | Power BI | Agile Project Management | Solutions Architecture")
    st.markdown("""
<details class='card'>
  <summary style='font-weight:600; font-size:18px;'> About Me</summary>
  <div style='padding-top:10px; font-size:16px;'>
    Dynamic and results-driven Petroleum Engineer with strong expertise in subsurface data interpretation, formation evaluation, drilling planning, data analysis with Python, and technical project execution within the oil and gas sector.

    Demonstrated success in aligning technical solutions with field operations, enhancing reservoir performance, and supporting HSE compliance across upstream operations.

    Skilled in Geolog, Petrel, Python, Numpy, Pandas, Matplotlib, Power BI, Streamlit, Flask and other industry-standard tools to deliver data-driven insights, optimize well planning, and drive operational excellence.

    And oh, I currently use Streamlit for all my frontend stuff and Python for all my backend. But yeah...I am capable of learning anything (try me 😄).
  </div>
</details>
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
    - Digital Oilfield Integration
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
# Certifications
# -----------------------------

st.title("📄 My Certifications")
st.markdown("To view a certificate, you will have to download it first 😹😄 (It is a glitch I intentionally refuse to fix so that you can visit my LinkedIn profile😂😆😹). So please view the certificates here to avoid having to download what you didn't work for 😹 [LinkedIn](https://linkedin.com/in/orachpaulfrancis).")
    
certificates = [
    {"title": "Agile Project Management", "description": "Certified in Agile principles and project lifecycle management.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Agile%20Project%20Management.pdf"},
    {"title": "Agile Scrum Foundation", "description": "Foundational understanding of Agile methodologies and Scrum framework.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Agile%20Scrum%20Foundation.pdf"},
    {"title": "BSG INTERNSHIP CERTIFICATE", "description": "Internship certificate from Big Solutions Group.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/BSG%20INTERNSHIP%20CERTIFICATE%20.pdf"},
    {"title": "Becoming a Solution Architect", "description": "Learning path for becoming a solution architect in Dynamics 365 and Power Platform.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Becoming%20a%20solution%20architect%20for%20Dynamics%20365%20and%20Microsoft%20Power%20Platform.pdf"},
    {"title": "Challenge Project - Microsoft Power Platform", "description": "Hands-on project building Microsoft Power Platform solutions.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Challenge%20project%20-%20Create%20Microsoft%20Power%20Platform%20solutions.pdf"},
    {"title": "Clean, Transform, and Load Data with Power BI", "description": "Power BI data preparation techniques.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Clean%2C%20transform%2C%20and%20load%20data%20with%20Power%20BI.pdf"},
    {"title": "Create a Power BI Model Framework", "description": "Designing robust data models in Power BI.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Create%20a%20Power%20BI%20model%20framework.pdf"},
    {"title": "Design a Semantic Model in Power BI", "description": "Semantic modeling best practices in Power BI.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Design%20a%20semantic%20model%20in%20Power%20BI.pdf"},
    {"title": "Discover Data Analysis", "description": "Introductory course on data analysis principles.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Discover%20Data%20Analysis.pdf"},
    {"title": "Discover Customer Needs", "description": "Analyzing customer requirements as a solution architect.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Discover%20customer%20needs%20as%20a%20Solution%20Architect%20for%20Dynamics%20365%20and%20Microsoft%20Power%20Platform.pdf"},
    {"title": "Effective Leadership", "description": "Certificate in leadership and communication skills.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Effective%20Leadership.pdf"},
    {"title": "GIS for Climate Action", "description": "Using GIS tools in support of climate resilience.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/GIS%20For%20Climate%20Action.pdf"},
    {"title": "Get Data in Power BI", "description": "Importing and connecting to data sources in Power BI.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Get%20Data%20in%20Power%20BI.pdf"},
    {"title": "Get Started With Copilot in Power BI", "description": "Introduction to Microsoft Copilot for Power BI.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Get%20Started%20With%20Copilot%20in%20Power%20BI.pdf"},
    {"title": "Getting Started With Power BI", "description": "Basic introduction to the Power BI ecosystem.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Getting%20Started%20With%20Power%20BI.pdf"},
    {"title": "ICON INTERNSHIP CERTIFICATE", "description": "Internship certification from Icon Geoengineering.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/ICON%20INTERNSHIP%20CERTIFICATE%20.pdf"},
    {"title": "Introduction to Drilling Engineering", "description": "Fundamentals of drilling engineering and wellbore design.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Introduction%20to%20Drilling%20Engineering.pdf"},
    {"title": "Introduction to GitHub", "description": "Version control and collaboration using GitHub.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Introduction%20to%20GitHub.pdf"},
    {"title": "Member Certificate for 5110334", "description": "Membership certificate from Society of Petroleum Engineers International.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Member%20Certificate%20for%205110334.pdf"},
    {"title": "Perform Fit Gap Analysis", "description": "Business analysis for requirement fitment.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Perform%20fit%20gap%20analysis.pdf"},
    {"title": "Propose a Solution as a Solution Architect", "description": "Solution architecture design practices for Power Platform and Dynamics 365.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Propose%20a%20solution%20as%20a%20Solution%20Architect%20for%20Microsoft%20Power%20Platform%20and%20Dynamics%20365.pdf"},
    {"title": "Risk Assessment and Hazard Management", "description": "Training in risk identification and mitigation in industrial environments.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Risk%20Assessment%20and%20Hazard%20Management.pdf"},
    {"title": "SPWLA Membership Appreciation Certificate", "description": "Recognition for active membership in SPWLA.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/SPWLA%20Membership%20Appreciation%20Certificate.pdf"},
    {"title": "SPWLA Membership Card", "description": "Official SPWLA membership ID.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/SPWLA%20Membership%20Card.pdf"},
    {"title": "SPWLA Membership Certificate", "description": "Membership certificate for Society of Petrophysicists and Well Log Analysts.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/SPWLA%20Membership%20Certificate.pdf"},
    {"title": "Spatial Analysis", "description": "Data analysis using spatial relationships in GIS.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Spatial%20Analysis.pdf"},
    {"title": "Strategic Planning", "description": "Planning and execution of organizational strategies.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Strategic%20Planning.pdf"},
    {"title": "Well Testing Crash Course 4", "description": "Short course on well testing analysis techniques.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Well%20Testing%20Crash%20Course%204.pdf"},
    {"title": "Work with Requirements for Microsoft Power Platform", "description": "Gathering and managing requirements for Power Platform and Dynamics 365 solutions.", "url": "https://github.com/ORACHPAULFRANCIS/Personal-Practice-Projects/raw/main/Portfolio/Work%20with%20requirements%20for%20Microsoft%20Power%20Platform%20and%20Dynamics%20365.pdf"},
]

# Sort certificates alphabetically by title
certificates = sorted(certificates, key=lambda x: x["title"])
# Create 3 columns
cols = st.columns(3)

# Distribute certificates evenly across the 3 columns
for idx, cert in enumerate(certificates):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class='card' style='padding:10px; border:1px solid #e6e6e6; border-radius:8px; margin-bottom:10px; background-color:#f9f9f9;'>
        📄 <b>{cert['title']}</b><br>
        {cert['description']}<br>
        <a href="{cert['url']}" target="_blank">View Certificate</a>
        </div>
        """, unsafe_allow_html=True)


# -----------------------------
# Footer
# -----------------------------
st.markdown("""
<hr style="margin-top: 2rem;">
<p style='text-align: center; color: grey; font-size: 0.9rem;'>
© 2025 Orach Paul Francis. Built with ❤️ using Streamlit.
</p>
""", unsafe_allow_html=True)
