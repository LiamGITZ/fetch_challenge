import requests
import time

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


# new tests
######################################################### 

x = requests.post(url_spend, json = { "points": 6300 })
print(x.text)
x = requests.get(url_balance)
print(x.text)

x = requests.post(url_spend, json = { "points": 1 })
print(x.text)

transactions2 = [
{ "payer": "DANNON", "points": 1000, "timestamp": 5 },
{ "payer": "UNILEVER", "points": 2000, "timestamp": 3 },
{ "payer": "MILLER COORS", "points": 10000, "timestamp": 6 },
{ "payer": "DANNON", "points": 3000, "timestamp": 2 },
{ "payer": "UNILEVER", "points": 2000, "timestamp": 4 }
]

for transaction in transactions2:
        x = requests.post(url_transactions, json = transaction)
        print(x.text)

x = requests.post(url_spend, json = { "points": 2042 })
print(x.text)
x = requests.get(url_balance)
print(x.text)

x = requests.post(url_spend, json = { "points": 42 })
print(x.text)
x = requests.get(url_balance)
print(x.text)

y = { "payer": "UNILEVER", "points": 3000, "timestamp": 1 }
x = requests.post(url_transactions, json = y)
print(x.text)
time.sleep(1)

x = requests.post(url_spend, json = { "points": 2042 })
print(x.text)
x = requests.get(url_balance)
print(x.text)

x = requests.post(url_spend, json = { "points": 42 })
print(x.text)
x = requests.get(url_balance)
print(x.text)

x = requests.post(url_spend, json = { "points": 8000 })
print(x.text)
x = requests.get(url_balance)
print(x.text)

x = requests.post(url_spend, json = { "points": 8832 })
print(x.text)
x = requests.get(url_balance)
print(x.text)

print('here-----------------------')
y = { "payer": "UNILEVER", "points": -3000, "timestamp": 1 }
x = requests.post(url_transactions, json = y)
print(x.text)

y = { "payer": "UNILEVER", "points": 0, "timestamp": 1 }
x = requests.post(url_transactions, json = y)
print(x.text)

x = requests.post(url_spend, json = { "points": 0 })
print(x.text)

x = requests.post(url_spend, json = { "points": -42 })
print(x.text)


x = requests.get(url_balance)
print(x.text)
