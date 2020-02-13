import requests
import json

# Call the API and store the response
url = 'https://hacker-news.firebaseio.com/v0/item/8863.json?print=pretty'
response_obj = requests.get(url)
print(f"Status code: {response_obj.status_code}")

# Explore the data gotten from the response.
response_dict = response_obj.json()
readable_file = '/api_response/hn_response.json'
with open(readable_file, 'w') as r:
    json.dump(response_dict, r, indent=4)
