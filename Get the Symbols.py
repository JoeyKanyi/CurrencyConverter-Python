import requests

url = "https://api.apilayer.com/fixer/symbols"

payload = {}
headers= {
  "apikey": "MYvHKS9NStR85B6aWYPKU5oP1viEYvpb"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(result)
