import requests


URL = 'https://api.github.com/zen'
response = requests.get(URL)

print(response.status_code)
print(response.text)
