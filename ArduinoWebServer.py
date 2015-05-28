import serial

class ArduinoWebServer:

	def __init__(self, serialPort, serialSpeed, debug = False):

		self.debug = debug
		self.serialPort = serialPort
		self.serialSpeed = serialSpeed

		if self.debug:
			print "[DEBUG] Server has been instantiated."
			print "[DEBUG] Connecting to Arduino..."

		self.serialCom = serial.Serial(serialPort, serialSpeed)

		if self.debug:
			print "[DEBUG] Established connection."

	def run_forever(self):

		if self.debug:
			print "[DEBUG] Server has been started."
			print "[DEBUG] Listening..."

		while 1:
			command = raw_input('')
			# todo change this

			if self.debug:
				print "[DEBUG] New command. " + command

			self.serialCom.write(command)
			res = self.serialCom.readline().rstrip()

			if self.debug:
				print "[DEBUG] Response from Arduino: " + res + '.'


if __name__ == '__main__':
	server = ArduinoWebServer('/dev/cu.HC-06-DevB', 9600, True)
	server.run_forever() 
