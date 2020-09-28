import requests


URL = 'https://api.github.com/zen'
response = requests.get(URL)

if response.status_code is 200:
    print(response.text)
else:
    print("Error: ", response.status_code)
