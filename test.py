import requests

transactions = [
{ "payer": "DANNON", "points": 1000, "timestamp": 4 },
{ "payer": "UNILEVER", "points": 200, "timestamp": 2 },
{ "payer": "MILLER COORS", "points": 10000, "timestamp": 3 },
{ "payer": "DANNON", "points": 300, "timestamp": 1 }
]


url_transactions = 'http://127.0.0.1:5000/add_transaction'
url_spend = 'http://127.0.0.1:5000/spend_points'
url_balance = 'http://127.0.0.1:5000/balance'

for transaction in transactions:
        x = requests.post(url_transactions, json = transaction)
        print(x.text)



x = requests.get(url_balance)
print(x.text)
x = requests.post(url_spend, json = { "points": 200 })
print(x.text)
x = requests.post(url_spend, json = { "points": 5000 })
print(x.text)
x = requests.get(url_balance)
print(x.text)




x = requests.post(url_spend, json = { "points": 6300 })
print(x.text)
x = requests.get(url_balance)
print(x.text)

