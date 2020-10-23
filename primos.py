import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')

def primos():
    limite = 100
    cont = 0 
    primos = []
    while cont < limite:
        if cont%2 == 1:
            primos.append(cont)
        cont +=1
    return primos
print (primos())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
