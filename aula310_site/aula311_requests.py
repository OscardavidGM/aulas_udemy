import requests

# http:// ->  porta 80
# https:// -> porta 443

url = 'http://localhost:3333/'

response = requests.get(url)

print(response.text)
