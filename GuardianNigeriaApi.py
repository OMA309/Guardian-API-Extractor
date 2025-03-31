import requests
import json
import pandas as pd 

"""
This script fetches news articles related to 'Nigeria' from The Guardian API,
extracts relevant details, and saves them as a CSV file.

Dependencies:
    - requests
    - json
    - pandas

Usage:
    Ensure you have an active API key from The Guardian API.
    Update the API_KEY variable accordingly before running the script.

Functions:
    - call_guardian_api(): Fetches news articles from The Guardian API and extracts
      details such as type, sectionId, publication date, and title.

Output:
    - A CSV file containing the extracted articles is saved to the specified path.

Note:
    - Ensure that the provided CSV path exists before executing the script.
    - Modify the API_KEY and date range as needed.
"""


#Accessing the Guardian API from th endpoint 
API_KEY = "29105801-a25c-4038-943b-0f626d******"
from_date = "2025-01-01"
to_date = "2025-03-30"
q = "Nigeria" 

BASE_ENDPOINT = f'https://content.guardianapis.com/search?q= {q}&from-date={from_date}&to-date={to_date}&api-key={API_KEY}'

# Sending a GET request to the endpoint
response = requests.get (BASE_ENDPOINT)

# Checking if the response was successful
response.status_code
# Assigning a variable to the json output 
Data = response.json()

checkout  = Data['response']['results']

# creating a function that extract just the key:value pairs needed for the project 
def call_guardian_api():
    Nigeria_guardian_api = []
    for Nigeria in checkout:
        Nigeria_guardian_api.append({'type': Nigeria['type'] ,
                            'sectionId':Nigeria['sectionId'] ,
                            'webPublicationDate': Nigeria['webPublicationDate'],
                            'webTitle': Nigeria['webTitle']})
    return Nigeria_guardian_api  
call_guardian_api()
# create a dataframe from the call_guardian_api function
df = pd.DataFrame(call_guardian_api())

# Save to CSV file
CSV_PATH = r'C:\Users\DATA_DISCIPLE\Desktop\PATH\TO\YOUR\DIRECTORY\The_GuardianFileUpdated.csv'

# Attempting to save the DataFrame as a CSV file
try:
    df.to_csv(CSV_PATH, index=False, encoding="utf-8")
    print(f'The CSV file at {CSV_PATH} was created successfully.')
except Exception as e:
    print(f'There was an issue saving the file at {CSV_PATH}. Error: {e}')
      
