# Web Scraping: Extracting Largest US Companies from Wikipedia

## Overview
This script scrapes the List of Largest Companies in the United States by Revenue from Wikipedia and saves the data to a CSV file. It uses `requests` to fetch the webpage, `BeautifulSoup` to parse the HTML, and `pandas` to process and save the data.

---

## Features
- Handles errors gracefully: Catches network errors and missing tables.
- Extracts table headers and rows dynamically.
- Ensures correct column-row alignment to avoid mismatched data.
- Saves the data as a CSV file named `TopUSCompanies.csv`.

---

## Prerequisites
Ensure you have the following Python libraries installed:

```bash
pip install requests beautifulsoup4 pandas
