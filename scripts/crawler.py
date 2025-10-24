import requests
from bs4 import BeautifulSoup
import pandas as pd

# The URL of the financial highlights page
url = "https://techcombank.com/en/investors/financial-information/highlights"

# Send a request to the webpage
response = requests.get(url)
response.raise_for_status()  # Raise an exception for bad status codes

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the financial highlights
# You would need to inspect the page source to find the correct table identifier
financial_table = soup.find('table') # This is a simplified selector

if financial_table:
    # Use pandas to read the HTML table directly into a DataFrame
    df = pd.read_html(str(financial_table))[0]
    print("Successfully scraped the financial table:")
    print(df.head())
else:
    print("Could not find the financial table on the page.")