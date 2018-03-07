from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)


@app.route("/name", methods=["GET"])
def name():
    """
    Returns your name

    :return: the name Eitan August
    :rtype: String
    """

    data = {
        "name": "Eitan August"
    }
    return jsonify(data)


@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    """
    Returns hello <name> parameter

    :param: String name: Desired name
    :return: Hello there <name>
    :rtype: String
    """
    data = {
        "message": "Hello there " + name,
    }
    return jsonify(data)

@app.route("/distance", methods=["POST"])
def distance():
    """
        Returns hello <name> parameter
        
        :return: The distance between two points
        :rtype: String
        """
    r = request.get_json()
    dist = sqrt((r["a"][0] - r["b"][0]) ** 2 + (r["a"][1] - r["b"][1]) ** 2)
    data = {
        "distance": dist,
        "a": r["a"],
        "b": r["b"]
    }

    return jsonify(data)