
import streamlit as st
import requests

st.set_page_config(
    page_title="Smart FX | Terminal",
    page_icon="💱",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #090b10;
    color: #e8edf5;
}
[data-testid="stHeader"] {
    background: #090b10;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1400px;
}
h1, h2, h3 {
    color: #f5f7fa !important;
}
p, label {
    color: #a7b0c0;
}
[data-testid="stMetric"] {
    background: #121722;
    border: 1px solid #252d3b;
    padding: 24px;
    border-radius: 14px;
}
[data-testid="stMetricLabel"] {
    color: #9ca8bb;
}
[data-testid="stMetricValue"] {
    color: #d6f5df;
}
.stButton > button {
    background: #d6f5df;
    color: #090b10;
    border: none;
    border-radius: 9px;
    font-weight: 700;
    padding: 10px 22px;
}
.stButton > button:hover {
    background: #b5e8c4;
    color: #090b10;
    border: none;
}
hr {
    border-color: #252d3b;
}
</style>
""", unsafe_allow_html=True)

st.caption("SMART FX  /  FINANCIAL INTELLIGENCE")
st.title("Market Overview")
st.write("USD · EUR · UZS  |  Official exchange rates")
st.divider()

if True:
    try:
        url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        currencies = {
            item["Ccy"]: float(item["Rate"])
            for item in data
            if item["Ccy"] in ["USD", "EUR"]
        }

        col1, col2 = st.columns(2)

        with col1:
            if "USD" in currencies:
                st.metric("🇺🇸 USD / UZS", f'{currencies["USD"]:,.2f} UZS')

        with col2:
            if "EUR" in currencies:
                st.metric("🇪🇺 EUR / UZS", f'{currencies["EUR"]:,.2f} UZS')

        st.caption("Source: Central Bank of Uzbekistan")

    except Exception as e:
        st.error(f"Could not load rates: {e}")

st.divider()
st.caption("SMART FX TERMINAL  •  DATA FOR INFORMATIONAL PURPOSES")

