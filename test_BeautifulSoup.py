import pandas as pd
import requests
from bs4 import BeautifulSoup

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Use the BeautifulSoup library to scrape data from a webpage

# This is the webpage we will be scraping from (a Netflix stock price history page)
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

# Use the requests library to download the webpage
data = requests.get(url).text
#print(data[:500])

# Use BeautifulSoup to parse the HTML data
soup = BeautifulSoup(data, 'html.parser')
#print(type(soup))

# create a DataFrame to store the scraped data
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"])
print(netflix_data.head())

# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table
    netflix_data = pd.concat([netflix_data,pd.DataFrame({"Date":[date], "Open":[Open], "High":[high], "Low":[low], "Close":[close], "Adj Close":[adj_close], "Volume":[volume]})], ignore_index=True)

# Display the first five rows of the DataFrame
print(netflix_data.head())

# Alternatively, we can use the pandas read_html function to scrape the data
# It returns a list of DataFrames, we take the first one
read_html_pandas_data = pd.read_html(url)
netflix_dataframe = read_html_pandas_data[0]
# Display the first five rows of the DataFrame
print(netflix_dataframe.head())

