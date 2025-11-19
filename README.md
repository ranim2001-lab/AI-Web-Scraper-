# 🔎 Web Scraper – Streamlit + LLM

This project is a simple but powerful **web scraping tool** built with **Streamlit**, using:
- Selenium or Requests for scraping (depending on your configuration)
- BeautifulSoup for HTML parsing
- A local LLM (Ollama) for intelligent content extraction, summarization, and structured parsing

The goal is to scrape any website, clean the HTML content, extract the `<body>`, and let an LLM parse the extracted text based on a user query.

---

## 🚀 Features

### ✔ Web Scraping
- Fetches full HTML content from any website
- Extracts only the `<body>` section
- Cleans the DOM and removes HTML tags
- Displays raw HTML + cleaned text

### 🤖 AI Parsing (Ollama)
- Chunking of large documents
- Natural language instructions for:
  - extracting tables  
  - summarizing  
  - listing titles, dates, items  
  - transforming content into JSON or Markdown  
  - and more...

### 🖥 Streamlit Web UI
- Easy-to-use interface
- Real-time progress messages
- Displays scraping and parsing results clearly

---

## 📁 Project Structure
├── main.py # Streamlit UI
├── scrape.py # Website scraping utilities
├── parse.py # LLM parsing utilities
├── requirements.txt # Python dependencies
└── README.md # Documentation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ranim2001-lab/streamlit-web-scraper.git
cd streamlit-web-scraper

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ (Optional) Install Ollama

If you want to use the local LLM parsing:

https://ollama.com/download

Then pull a model (example):

ollama pull llama3.1

▶️ Run the Streamlit App
streamlit run main.py

