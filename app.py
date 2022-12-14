from flask import Flask
from flask import request
import logging

app = Flask(__name__)

logging.basicConfig(filename='example.log', level=logging.DEBUG)

@app.route('/')
def main():
    print("/ called")

    return 'Container is up & running'

# problem data
coins = {
    'penny': 1,
    'nickel': 5,
    'dime': 10,
    'quarter': 25
}

import optimizer
@app.route('/callGurobi')
def callGurobi():
    print("/ called callGurobi")
    amount = request.args.get('amount')
    if amount is None:
        amount = 1034
    print("amount=" + str(amount))
    return optimizer.make_change_gurobi(int(amount),coins)

@app.route('/callXpress')
def callXpress():
    print("/ called callXpress")
    amount = request.args.get('amount')
    if amount is None:
        amount = 1034
    print("amount=" + str(amount))
    return optimizer.make_change_xpress(int(amount),coins)

@app.route('/callPyomo')
def callPyomo():
    print("/ called callPyomo")
    amount = request.args.get('amount')
    if amount is None:
        amount = 1034
    print("amount=" + str(amount))
    return optimizer.make_change_pyomo(int(amount),coins)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')