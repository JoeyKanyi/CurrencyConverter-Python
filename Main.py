# This program converts an amount of money from one currency to another
# The input is the currency from which to be converted, the currency to be converted to and the amount
import requests


def converter(fro, to, amount):

    url = "https://api.apilayer.com/fixer/convert?to=" + \
        to+"&from="+fro+"&amount="+amount

    payload = {}
    headers = {
        "apikey": "MYvHKS9NStR85B6aWYPKU5oP1viEYvpb"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text
    return result


print(converter(fro=input("From: "), to=input("To: "), amount=input("Amount: ")))
