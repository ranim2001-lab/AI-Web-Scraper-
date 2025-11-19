from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_website(url):
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        html = driver.page_source
        return html

    finally:
        driver.quit()


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    return str(soup.body) if soup.body else ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for tag in soup(["script", "style"]):
        tag.extract()

    cleaned = soup.get_text(separator="\n")
    cleaned = "\n".join(
        line.strip() for line in cleaned.splitlines() if line.strip()
    )
    return cleaned


def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i: i + max_length]
        for i in range(0, len(dom_content), max_length)
    ]
