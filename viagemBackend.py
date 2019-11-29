from flask import Flask, jsonify
from playhouse.shortcuts import model_to_dict
from viagem import *

app = Flask(__name__)

@app.route("/")
def inicio():
    return ""

@app.route("/listar_clientes")
def listar_clientes():
    clientes = list(map(model_to_dict, Cliente.select()))
    return jsonify ({'lista' :clientes})

app.run(debug=True, port=4999)