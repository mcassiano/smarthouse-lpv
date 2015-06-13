import requests
from flask import Flask, request, send_from_directory
app = Flask(__name__, static_url_path='')

local_server = 'http://192.168.42.10:5000/send'

@app.route("/<path:path>", methods = ['GET'])
def admin(path):
	return send_from_directory('/static', path)

@app.route("/getTemp", methods = ['GET'])
def getTemp():
	params = {'message': 'temp'}
	return requests.post(local_server, data = params).text

@app.route("/toggleLed", methods = ['GET'])
def toggleLed():
	params = {'message': 'led %s' % request.args.get('led')}
	return requests.post(local_server, data = params).text

@app.route("/setRGB", methods = ['GET'])
def setRGB():
	blue = request.args.get('blue')
	red = request.args.get('red')
	green = request.args.get('green')

	message = 'rgb %s %s %s' % (red, green, blue)
	params = {'message' : message}

	return requests.post(local_server, data = params).text

@app.route("/getLEDState", methods = ['GET'])
def getLED():
	led = request.args.get('led')
	message = 'led state %s' % led

	params = {'message' : message}

	return requests.post(local_server, data = params).text

if __name__ == "__main__":
	app.debug = True
	app.run(host = '0.0.0.0', port = 80)
