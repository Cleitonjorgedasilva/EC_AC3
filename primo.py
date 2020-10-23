import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)
@app.route('/')
def primos():
    limite =  100

    c = 1
    a = 1
    numero = 2
    primos = "0, "
    while a < limite:
        ehprimo = 1
        for i in range(1, numero):
            if numero%i == 0:
                ehprimo = 0
                break
        if (ehprimo):
            primos = primos + str(numero) + ","
            a+=1
        numero +=1

    return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
