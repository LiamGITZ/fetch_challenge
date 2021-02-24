from collections import defaultdict
import types

transactions = []
payers = defaultdict(int)

class transaction:
    def __init__(self, payer, points, timestamp):
        self.payer = payer
        self.points = points
        self.timestamp = timestamp

    def __lt__(self, transaction2):
        return transaction2.timestamp > self.timestamp

    def __eq__(self, transaction2):
        return     self.payer     == transaction2.payer \
               and self.points    == transaction2.points \
               and self.timestamp == transaction2.timestamp

from flask import Flask, request
from datetime import datetime
import bisect

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/add_transaction', methods=['POST'])
def json_example():
    request_data = request.get_json()

    # data validation
    print(request_data)
    if not request_data:
        return('invalid no data', 400)
    elif not 'payer' in request_data or request_data['payer'] == '':
        return('no payer information')
    elif not 'points' in request_data:
        return('no point value', 400)
    elif not 'timestamp' in request_data or request_data['timestamp'] <= 0:
        return('invalid date', 400)
    else:
        given_transaction = transaction(request_data['payer'], request_data['points'], request_data['timestamp'])
        if given_transaction in transactions:
            return('transaction already recorded', 400)
        bisect.insort_right(transactions, given_transaction)
        payers[given_transaction.payer] += given_transaction.points

    date = datetime.utcfromtimestamp(given_transaction.timestamp)
    date_time = date.strftime("%m/%d/%Y, %H:%M:%S")
    return('Recieved Transaction for time: ' + str(date_time))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
