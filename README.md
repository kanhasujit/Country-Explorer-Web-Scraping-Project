# 🌍 Country Explorer

A web scraping project that fetches and displays country information from Wikipedia with a clean, dark-themed interface.

## Live Demo
🔗 [View App](https://country-explorer.streamlit.app/) &nbsp;|&nbsp; 👤 [Portfolio](https://sujit-port-folio.netlify.app/)

---

## Features

- 🔍 **Live search suggestions** powered by Wikipedia OpenSearch API
- 📋 **Full country details** scraped from Wikipedia infoboxes
- ⚡ **Fast parsing** using `lxml`
- 🎨 **Dark themed UI** with hover effects
- 📱 **Responsive layout**

---

## Tech Stack

| Tool | Purpose |
|---|---|
| `Streamlit` | Web interface |
| `requests` | HTTP requests |
| `BeautifulSoup4` | HTML parsing |
| `lxml` | Fast parser |
| `Wikipedia API` | Search suggestions |

---

## Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/country-explorer.git
cd country-explorer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run
python -m streamlit run app.py
```

---

## Project Structure

```
country-explorer/
├── app.py              # Main application
├── requirements.txt    # Dependencies
└── README.md
```

---

## How It Works

```
User types "Ind"
    → Wikipedia OpenSearch API
    → Suggestions: ["India", "Indonesia", ...]
    → User selects "India"
    → Scrape wikipedia.org/wiki/India
    → Parse infobox table
    → Display key-value pairs
```

---

## Deploy on Streamlit Cloud

1. Push repo to GitHub (public)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. New app → select repo → `Country_explorer.py` → Deploy ✅

---

## Disclaimer

This project is created solely by **Sujit** for **educational purposes only**.  
Data is sourced from Wikipedia and belongs to their respective contributors.

---

> Made with ❤️ by [Sujit](https://sujit-port-folio.netlify.app/)
