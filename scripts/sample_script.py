import requests
import pandas as pd

print("Sample Script Running...")
response = requests.get("https://jsonplaceholder.typicode.com/posts")
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    print("First 5 rows of fetched data:")
    print(df.head())
else:
    print("Failed to fetch data.")

