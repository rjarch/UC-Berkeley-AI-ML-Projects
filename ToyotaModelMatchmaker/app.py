import streamlit as st
import requests

st.set_page_config(page_title="Toyota Matchmaker", page_icon="🚗", layout="wide")

# Custom CSS for that Toyota Red branding
st.markdown("""
    <style>
    .stButton>button { 
        width: 100%; border-radius: 8px; background-color: #eb0a1e; color: white; font-weight: bold;
    }
    .stMetric { background-color: #ffffff; padding: 10px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚗 Toyota Model Matchmaker")

# --- SIDEBAR WITH TABS (Reduces Scrolling) ---
with st.sidebar:
    st.header("📋 Your Profile")
    st.write("Complete the sections below:")
    
    # Use Expanders to hide/show groups of inputs
    with st.expander("👤 Personal Details", expanded=True):
        age = st.number_input("Age", 18, 100, 35)
        gender = st.selectbox("Gender", ["Male", "Female", "Non-binary"])
        occ = st.selectbox("Occupation", ["Professional", "Management", "Student", "Skilled Manual"])

    with st.expander("💰 Financials & Family"):
        income = st.number_input("Annual Income ($)", min_value=0, value=50000, step=1000)
        family = st.slider("Family Size", 1, 8, 2)
        area = st.selectbox("Living Area", ["Urban", "Suburban", "Rural"])

    with st.expander("🛣️ Driving Habits"):
        commute = st.number_input("Daily Commute (Miles)", 0, 500, 20)
        fuel = st.radio("Fuel Preference", ["Gasoline", "Hybrid", "Electric"], horizontal=True)
        loyalty = st.select_slider("Brand Loyalty", options=range(1, 11), value=5)

    predict_btn = st.button("Generate My Matches")

# --- MAIN PAGE DISPLAY ---
if predict_btn:
    payload = {
        "age": age, "gender": gender, "income": income, "family_size": family,
        "daily_commute_miles": commute, "loyalty_score": loyalty,
        "occupation": occ, "fuel_preference": fuel, "area": area
    }
    
    try:
        with st.spinner('Calculating your perfect match...'):
            response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        
        if response.status_code == 200:
            results = response.json()["top_recommendations"]
            
            st.header("🏆 Your Top 3 Toyota Recommendations")
            cols = st.columns(3)
            
            icons = ["🥇", "🥈", "🥉"]
            for i, res in enumerate(results):
                with cols[i]:
                    with st.container(border=True):
                        st.subheader(f"{icons[i]} {res['vehicle']}")
                        st.metric("Match Score", f"{res['confidence']*100:.1f}%")
                        st.progress(res['confidence'])
            st.balloons()
        else:
            st.error("API Error. Please check if main.py is running.")
    except Exception as e:
        st.error(f"Connection failed: {e}")
else:
    # A cleaner landing state
    st.info("Fill out the categories in the sidebar and click the button to see your results.")