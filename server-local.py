from flask import Flask, request
from ArduinoConnection import ArduinoConnection

app = Flask(__name__)

serialAddress = '/dev/cu.usbmodem1411'

@app.route("/send", methods = ['GET', 'POST'])
def send():

	if request.method == 'POST':
		message = str(request.form['message'])
		connection = ArduinoConnection(serialAddress, 9600)
		connection.write_and_get_response(message)
		res = connection.read()

		return res

	return "{'status': 'invalid-request'}"

if __name__ == "__main__":
	app.debug = True
	app.run(host = '0.0.0.0')