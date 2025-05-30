import requests
import pandas as pd

url = "https://run.mocky.io/v3/0ff9b004-fb7a-4d8a-9c95-43f96080d0e6" # Using the provided url
response = requests.get(url) # Requests declared in respone variable

if response.status_code == 200: # If fetching becomes successful
    data = response.json()  # we parse the data to JSON format
    print(data) # printing data in JSON Format
else:
    print("Failed to fetch data") # Handling exception

# We have dictionaries as the type of data in the provided url
df = pd.DataFrame(data)
print(df.head())  # Just seeing first few rows of the DataFrame

df.to_csv("assessment.csv")


