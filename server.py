from collections import defaultdict
import types

total_points = 0
transactions = [] # sorted list
used_transactions = [] # currently unused
payers = defaultdict(int)

class Transaction:
    def __init__(self, payer, points, timestamp):
        self.payer = payer
        self.inital_points = points
        self.valid_points = points
        self.timestamp = timestamp

    def __lt__(self, transaction2):
        return transaction2.timestamp > self.timestamp

    def __eq__(self, transaction2):
        return     self.payer            == transaction2.payer \
               and self.inital_points    == transaction2.inital_points \
               and self.timestamp        == transaction2.timestamp



from flask import Flask, request
from datetime import datetime
import bisect
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    global total_points
    request_data = request.get_json()

    # data validation
    if not request_data:
        return('invalid no data', 400)
    elif not 'payer' in request_data or request_data['payer'] == '':
        return('no payer information')
    elif not 'points' in request_data:
        return('no point value', 400)
    elif request_data['points'] <= 0:
        return('invalid amount of points', 400)
    elif not 'timestamp' in request_data or request_data['timestamp'] <= 0:
        return('invalid date', 400)
    else:
        given_transaction = Transaction(request_data['payer'], request_data['points'], request_data['timestamp'])
        if given_transaction in transactions:
            return('transaction already recorded', 400)
        bisect.insort_right(transactions, given_transaction)
        payers[given_transaction.payer] += given_transaction.inital_points
        total_points += given_transaction.inital_points

    date = datetime.utcfromtimestamp(given_transaction.timestamp)
    date_time = date.strftime("%m/%d/%Y, %H:%M:%S")
    return('Recieved Transaction for time: ' + str(date_time))


@app.route('/spend_points', methods=['POST'])
def spend_points():
    global total_points
    global transactions
    global used_transactions

    request_data = request.get_json()
    payment_dict = defaultdict(int)

    if not request_data:
        return('invalid no data', 400)
    elif not 'points' in request_data or request_data['points'] <= 0:
        return('no point value', 400)

    point_goal = request_data['points']
    if total_points >= point_goal:
        total_points -= point_goal
    else:
        return 'not enough funds'

    indx_used = 0
    for transaction in transactions:
        if point_goal == 0:
            break

        if transaction.valid_points > point_goal:
            transaction.valid_points -= point_goal
            payers[transaction.payer] -= point_goal
            payment_dict[transaction.payer] -= point_goal
            point_goal = 0
        else:
            indx_used += 1
            point_goal -= transaction.valid_points
            payers[transaction.payer] -= transaction.valid_points
            payment_dict[transaction.payer] -= transaction.valid_points
            transaction.valid_points = 0

    used_transactions.extend(transactions[:indx_used])
    transactions = transactions[indx_used:]

    # format output
    return_list = []
    for key in payment_dict:
        return_list.append({'payer': key, 'points': payment_dict[key]})
    return json.dumps(return_list)



@app.route('/balance', methods=['GET'])
def get_balance():
    return payers

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')












