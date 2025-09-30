
---

# 🤖 ChainMetrics

Your professional AI-powered crypto advisor with sustainability insights.
Built with **Streamlit**, **CoinGecko API**, and **NLP (NLTK)**.

---

## 📌 Features

* 📊 Live market data (via [CoinGecko API](https://www.coingecko.com/en/api))
* 🌱 Sustainability scoring for eco-friendly investing
* 🧠 Natural language chatbot (ask about trends, profits, or green coins)
* 💡 Easy to extend with more coins or features
* ⚠️ Includes an ethics disclaimer (“Crypto is risky—always DYOR!”)

---

## 🚀 Live Demo

👉 [Try ChainMetrics Online](https://your-demo-link.com) *(replace with your deployed Streamlit link)*

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **Streamlit** – UI framework
* **Requests** – Fetch crypto data
* **NLTK** – Natural Language Processing
* **python-dotenv** – Environment variable management

---

## ⚙️ Configuration

ChainMetrics uses environment variables to make it easy to switch between settings without editing the code.

### 1. Create a `.env` file

In the root directory of the project, create a file named **`.env`** and add the following variables:

```env
# API endpoint for CoinGecko
COINGECKO_URL=https://api.coingecko.com/api/v3/coins/markets

# Comma-separated list of coin IDs
CRYPTO_IDS=bitcoin,ethereum,cardano

# Currency for pricing (usd, eur, kes, etc.)
VS_CURRENCY=usd
```

### 2. Modify as needed

* Add Solana:

  ```env
  CRYPTO_IDS=bitcoin,ethereum,cardano,solana
  ```
* Switch to EUR:

  ```env
  VS_CURRENCY=eur
  ```
* Test custom API endpoints by changing `COINGECKO_URL`.

### 3. Security Note

* Never commit your `.env` file to GitHub.
* Add `.env` to your **.gitignore** file.

---

## 📦 Installation & Setup

```bash
# Clone repository
git clone https://github.com/your-username/chainmetrics.git
cd ChainMetrics

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 🧠 Usage

* Ask questions like:

  * *“Which crypto is trending up?”*
  * *“What’s the most sustainable coin?”*
  * *“Which coin is most profitable to invest in?”*

* The bot analyzes **price trends**, **market cap**, and **sustainability score** to respond.

---

## 📈 Roadmap

* [ ] Add support for more coins dynamically
* [ ] Sentiment analysis from Twitter/Reddit
* [ ] Advanced visualizations (candlestick charts, volume trends)
* [ ] Portfolio tracking

---

## ⚠️ Disclaimer

Crypto is **high-risk**. ChainMetrics provides insights, **not financial advice**.
Always **DYOR (Do Your Own Research)** before investing.

---