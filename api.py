from flask import Flask, request, json
import numpy as np

from engine import load_dispatch

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def engine():
    """
        Function for running engine.py
    """
    request_data = json.loads(request.data)
    n = request_data['n']
    a = np.array(request_data['a'])
    b = np.array(request_data['b'])
    c = np.array(request_data['c'])
    PD = request_data['PD']
    P_min = np.array(request_data['pmin'])
    P_max = np.array(request_data['pmax'])

    [P, C, Total_Cost] = load_dispatch(n, a, b, c, P_min, P_max, PD)

    P = json.dumps(P.tolist())
    C = json.dumps(C.tolist())
    Total_Cost = json.dumps(Total_Cost)

    return {
        'P': P,
        'C': C,
        "Total_Cost": Total_Cost
    }

if __name__ == '__main__':
    app.run( port=5001)
