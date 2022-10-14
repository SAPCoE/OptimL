from flask import Flask
from flask import request
import logging
import os

app = Flask(__name__)

logging.basicConfig(filename='example.log', level=logging.DEBUG)


@app.route('/v1/status')
def status():
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
@app.route('/v1/callGurobi')
def callGurobi():
    print("/ called callGurobi")
    amount = request.args.get('amount')
    if amount is None:
        amount = 1034
    print("amount=" + str(amount))
    return optimizer.make_change_gurobi(int(amount),coins)

@app.route('/v1/callXpress')
def callXpress():
    print("/ called callXpress")
    amount = request.args.get('amount')
    if amount is None:
        amount = 1034
    print("amount=" + str(amount))
    return optimizer.make_change_xpress(int(amount),coins)

@app.route('/v1/callPyomo')
def callPyomo():
    print("/ called callPyomo")
    amount = request.args.get('amount')
    if amount is None:
        amount = 1034
    print("amount=" + str(amount))
    return optimizer.make_change_pyomo(int(amount),coins)

@app.route('/v1/callOptimizer')
def status():
    optOption = os.environ["Optimizer"]
    print(f'{optOption}')
    if amount is None:
        amount = 1034
    print("amount=" + str(amount))
    if optOption == 'Pyomo':
        return optimizer.make_change_pyomo(int(amount),coins)
    if optOption == 'Gurobi':
        return  optimizer.make_change_gurobi(int(amount),coins)
    if optOption == 'Xpress':
        return optimizer.make_change_xpress(int(amount),coins)
    return {'status':'No Optimizer chosen'}

if __name__ == '__main__':
    print(f'{os.environ["greetingmessage"]}')
    print("Serving Started")
    app.run(debug=True, host='0.0.0.0',port=9001)