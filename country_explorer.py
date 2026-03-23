import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

st.set_page_config(page_title="Country Explorer", page_icon="🌍", layout="centered")

import base64

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg = get_base64("globe.png")

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
    color: #e0e0e0;
}}

/* Animated background */
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{bg}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

@keyframes bgpulse {{
    0%   {{ background-color: #0a0e1a; }}
    100% {{ background-color: #0d1220; }}
}}

/* Spinning globe in header area via pseudo */
[data-testid="stHeader"] {{ background: transparent !important; }}
[data-testid="stToolbar"] {{ display: none; }}

.block-container {{
    padding: 2rem 2rem;
    max-width: 800px;
    background: rgba(10,14,26,0.6);
    backdrop-filter: blur(2px);
    border-radius: 16px;
    margin-top: 1rem;
}}
#MainMenu, footer, header {{ visibility: hidden; }}

h1 {{ color: #ffffff !important; font-weight: 600 !important; }}

.stTextInput > div > div > input {{
    background: #1c1f2e !important;
    border: 1px solid #2e3250 !important;
    border-radius: 8px !important;
    color: #ffffff !important;
    font-size: 1rem !important;
    padding: 0.7rem 1rem !important;
}}
.stTextInput label {{ color: #888 !important; }}

.stSelectbox > div > div {{
    background: #1c1f2e !important;
    border: 1px solid #2e3250 !important;
    color: #fff !important;
    border-radius: 8px !important;
}}

.stButton > button {{
    background: #3a7bd5 !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.5rem 2rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px !important;
}}
.stButton > button:hover {{ background: #2f63b0 !important; }}

.country-title {{
    font-size: 2rem;
    font-weight: 700;
    color: #ffffff;
    margin: 1.5rem 0 1rem 0;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid #3a7bd5;
}}

.row {{
    display: flex;
    align-items: flex-start;
    padding: 10px 12px;
    border-radius: 6px;
    margin-bottom: 4px;
    background: rgba(28,31,46,0.85);
    gap: 1rem;
    transition: background 0.2s;
}}
.row:hover {{ background: rgba(34,38,64,0.95); }}
.key {{
    color: #7a8bb5;
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    min-width: 210px;
    padding-top: 2px;
    font-weight: 600;
}}
.val {{
    color: #e8e8e8;
    font-size: 0.92rem;
    font-weight: 400;
    line-height: 1.5;
}}
</style>
""", unsafe_allow_html=True)

st.title("🌍 Country Explorer")

inp = st.text_input("Enter country name", placeholder="e.g. Japan, Brazil, India...")

if inp and len(inp) >= 2:
    try:
        r = requests.get("https://en.wikipedia.org/w/api.php", params={
            "action": "opensearch", "search": inp, "limit": 5, "format": "json"
        }, timeout=5)
        suggestions = r.json()[1]
        if suggestions:
            inp = st.selectbox("Suggestions", suggestions)
    except Exception:
        pass

if st.button("Search") and inp:
    with st.spinner("Fetching details..."):
        url = f"https://en.wikipedia.org/wiki/{inp.replace(' ', '_')}"
        soup = BeautifulSoup(requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).text, "lxml")
        info = soup.find("table", class_="infobox")

    if not info:
        st.error("No data found. Try the exact country name.")
    else:
        st.markdown(f'<div class="country-title">{inp}</div>', unsafe_allow_html=True)

        for row in info.find_all("tr"):
            header = row.find("th")
            value  = row.find("td")
            if header and value:
                key = re.sub(r'\[.*?\]', '', header.get_text(" ").strip())
                val = re.sub(r'\[.*?\]', '', value.get_text(" ").strip())
                if key and val:
                    st.markdown(
                        f'<div class="row">'
                        f'<div class="key">{key}</div>'
                        f'<div class="val">{val}</div>'
                        f'</div>',
                        unsafe_allow_html=True
                    )

st.markdown("""
<div style="text-align:center; margin-top:3rem; padding-top:1rem;
border-top:1px solid #2e3250; color:#555; font-size:0.78rem;">
    This is a web scraping project created solely by <b style="color:#7a8bb5">@Sujit</b> for educational purpose.<br><br>
    <a href="https://sujit-port-folio.netlify.app/" target="_blank"
    style="color:#3a7bd5; text-decoration:none; font-weight:600;">🔗 Connect with me</a>
</div>
""", unsafe_allow_html=True)