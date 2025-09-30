import os
import requests
import nltk
import streamlit as st
from nltk.tokenize import word_tokenize
from dotenv import load_dotenv

# -------------------------------
# Load environment variables
# -------------------------------
load_dotenv()

COINGECKO_URL = os.getenv("COINGECKO_URL", "https://api.coingecko.com/api/v3/coins/markets")
CRYPTO_IDS = os.getenv("CRYPTO_IDS", "bitcoin,ethereum,cardano")
VS_CURRENCY = os.getenv("VS_CURRENCY", "usd")
API_KEY = os.getenv("COINGECKO_DEMO_API_KEY")

# -------------------------------
# Setup NLTK
# -------------------------------
nltk.download("punkt", quiet=True)

# -------------------------------
# Fetch Live Data from CoinGecko
# -------------------------------
@st.cache_data(ttl=300)  # Cache results for 5 minutes
def fetch_crypto_data():
    params = {
        "vs_currency": VS_CURRENCY,
        "ids": CRYPTO_IDS,
        "order": "market_cap_desc",
        "per_page": len(CRYPTO_IDS.split(",")),
        "page": 1,
        "sparkline": False,
        "price_change_percentage": "24h"
    }

    headers = {}
    if API_KEY:
        # Try query param first
        params["x_cg_demo_api_key"] = API_KEY
        response = requests.get(COINGECKO_URL, params=params)

        # If unauthorized, fallback to header
        if response.status_code == 401:
            params.pop("x_cg_demo_api_key", None)
            headers["x-cg-demo-api-key"] = API_KEY
            response = requests.get(COINGECKO_URL, params=params, headers=headers)
    else:
        response = requests.get(COINGECKO_URL, params=params)

    response.raise_for_status()
    return response.json()

# -------------------------------
# NLP Preprocessing
# -------------------------------
def preprocess_query(query):
    return word_tokenize(query.lower())

# -------------------------------
# Chatbot Logic
# -------------------------------
def chatbot_response(query, crypto_data):
    tokens = preprocess_query(query)

    # Default response
    response = "Hmm 🤔 I’m not sure. Try asking about sustainability, trends, or profitability!"

    # Sustainability scores (demo only)
    sustainability_scores = {"bitcoin": 3, "ethereum": 6, "cardano": 9}
    if any(word in tokens for word in ["sustainable", "eco", "green"]):
        recommend = max(sustainability_scores, key=sustainability_scores.get)
        response = f"🌱 {recommend.capitalize()} is the most sustainable with score {sustainability_scores[recommend]}/10!"

    # Trending (price change in 24h)
    elif any(word in tokens for word in ["trend", "trending", "up"]):
        trending = max(crypto_data, key=lambda x: x.get("price_change_percentage_24h", 0))
        response = f"📈 {trending['name']} is trending up with {trending['price_change_percentage_24h']:.2f}% change today!"

    # Profitable (high market cap + rising)
    elif any(word in tokens for word in ["profit", "profitable", "invest"]):
        high_cap_rising = [
            c for c in crypto_data
            if c.get("market_cap_rank", 999) <= 5 and c.get("price_change_percentage_24h", 0) > 0
        ]
        if high_cap_rising:
            best = high_cap_rising[0]
            response = f"💰 {best['name']} looks profitable: rising and high market cap (${best['market_cap']:,})"
        else:
            response = "💸 No profitable high-market-cap coins at the moment."

    return response

# -------------------------------
# Streamlit App
# -------------------------------
st.title("🤖 ChainMetrics")
st.write("Your professional crypto advisor with sustainability insights!")

# Fetch data
try:
    crypto_data = fetch_crypto_data()
except Exception as e:
    st.error(f"Failed to fetch data from CoinGecko: {e}")
    st.stop()

# Market Snapshot
st.subheader("📊 Market Snapshot")
for coin in crypto_data:
    st.write(f"**{coin['name']}**: ${coin['current_price']} (24h: {coin['price_change_percentage_24h']:.2f}%)")

# User Query
user_query = st.text_input("Ask me something about crypto...")

if user_query:
    bot_reply = chatbot_response(user_query, crypto_data)
    st.success(bot_reply)

# Disclaimer
st.warning("⚠️ Disclaimer: Crypto is risky—always do your own research before investing!")
