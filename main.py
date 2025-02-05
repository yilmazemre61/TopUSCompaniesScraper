import requests
import pandas as pd
from bs4 import BeautifulSoup

# Step 1: Send a request to Wikipedia and get the HTML content
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an error for unsuccessful requests
except requests.exceptions.RequestException as e:
    print(f"Error fetching the page: {e}")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Find all tables and ensure at least one exists
tables = soup.find_all('table')

if not tables:
    print("No tables found on the page.")
    exit()

# Step 3: Extract the first table
table = tables[0]

# Step 4: Extract headers
headers = [header.text.strip() for header in table.find_all('th')]

# Step 5: Extract rows
rows = []
for row in table.find_all('tr')[1:]:  # Skip header row
    columns = row.find_all('td')
    row_data = [col.text.strip() for col in columns]
    if row_data:  # Avoid empty rows
        rows.append(row_data)

# Step 6: Convert to DataFrame
df = pd.DataFrame(rows, columns=headers[:len(rows[0])])  # Ensure column length matches row length

# Step 7: Save to CSV
df.to_csv("TopUSCompanies.csv", index=False)
print("Data saved successfully!")

