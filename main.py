from flask import Flask, jsonify
from threading import Thread
app = Flask('');

@app.route('/')
def home():
	return "I'm alive!"

@app.route('/api/add', methods=['GET'])
def add():
	return jsonify({"2 + 2": 2 + 2})

@app.route('/api/add/<int:num>', methods=['GET'])
def addNum(num):
	return jsonify({f"{num} + {num}" : num + num})

@app.route('/api/name/<string:name>', methods=['GET'])
def getName(name):
	return jsonify({"Your name": name})

def run():
	app.run(host='0.0.0.0', port=8080)

t = Thread(target=run)
t.start()