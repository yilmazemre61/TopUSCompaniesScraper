from bs4 import BeautifulSoup
import requests
import pandas as pd

# Step 1: Send a request to Wikipedia and get the HTML content
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# Step 2: Extract the first table from the page
table = soup.find_all('table')[0]

# Step 3: Extract table headers
table_headers = table.find_all('th')

# Step 4: Create a list of column names from table headers
table_headers_titles = [title.text.strip() for title in table_headers]

# Step 5: Initialize an empty DataFrame with the extracted column names
df = pd.DataFrame(columns=table_headers_titles)

# Step 6: Extract table rows and populate the DataFrame
column_data = table.find_all('tr')  # Get all rows
for row in column_data[1:]:  # Skip the header row
    row_data = row.find_all('td')  # Extract columns from the row
    individual_row_data = [data.text.strip() for data in row_data]  # Clean the text data

    # Append the row data to the DataFrame
    length = len(df)
    df.loc[length] = individual_row_data

# Step 7: Save the DataFrame to a CSV file
df.to_csv("TopUSCompanies.csv", index=False)

