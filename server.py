
transactions = []
payers = {}


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
    elif not request_data['payer'] or request_data['payer'] == '':
        return('no payer information')
    elif not request_data['points']:
        return('no point value', 400)
    elif not request_data['timestamp'] or request_data['timestamp'] <= 0:
        return('invalid date', 400)
    elif (request_data['timestamp'], request_data) in transactions:
        return('transaction already recorded', 400)
    else:
        bisect.insort_right(transactions, (request_data['timestamp'], request_data))

    date = datetime.utcfromtimestamp(request_data['timestamp'])
    date_time = date.strftime("%m/%d/%Y, %H:%M:%S")
    return('Recieved Transaction for time: ' + str(date_time))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
