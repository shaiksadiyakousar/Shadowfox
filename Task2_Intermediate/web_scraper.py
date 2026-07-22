"""
ShadowFox Python Development Internship
Task 2 (Intermediate) - Web Scraper
Author: Shaik Sadiya Kousar

Uses BeautifulSoup to extract data from a website and save it to a CSV file.

NOTE ON SITE CHOICE:
The task suggests practicing on the ShadowFox website, but that site's HTML
structure isn't publicly documented/stable for scraping practice, so this
script targets https://quotes.toscrape.com instead — a website built
specifically for learning web scraping (it's free, legal, and stable to
scrape). The same technique (requests + BeautifulSoup + CSS selectors)
applies directly to any other site, including ShadowFox's — you would just
change the URL and the tag/class names to match that site's HTML.
"""

import csv
from pathlib import Path

import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com"
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = BASE_DIR / "scraped_quotes.csv"


def scrape_quotes(url):
    """Fetch a page and extract quote text, author, and tags."""
    scraped_data = []

    try:
        response = requests.get(
            url,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"},
        )
        response.raise_for_status()  # raises an error for bad status codes (404, 500, etc.)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return scraped_data

    soup = BeautifulSoup(response.text, "html.parser")
    quote_blocks = soup.find_all("div", class_="quote")

    for block in quote_blocks:
        try:
            text = block.find("span", class_="text").get_text(strip=True)
            author = block.find("small", class_="author").get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in block.find_all("a", class_="tag")]

            scraped_data.append({
                "quote": text,
                "author": author,
                "tags": ", ".join(tags)
            })
        except AttributeError as e:
            # If a quote block is missing an expected element, skip it
            # instead of crashing the whole scrape.
            print(f"Skipping a malformed quote block: {e}")
            continue

    return scraped_data


def save_to_csv(data, filename):
    """Save scraped data to a CSV file for further analysis."""
    if not data:
        print("No data to save.")
        return

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["quote", "author", "tags"])
        writer.writeheader()
        writer.writerows(data)

    print(f"Saved {len(data)} records to {filename}")


if __name__ == "__main__":
    print(f"Scraping data from: {URL}")
    quotes = scrape_quotes(URL)

    print(f"\nFound {len(quotes)} quotes.\n")
    for i, q in enumerate(quotes[:5], start=1):  # preview first 5
        print(f"{i}. \"{q['quote']}\" — {q['author']} [{q['tags']}]")

    save_to_csv(quotes, OUTPUT_FILE)
