#import serial

class ArduinoConnection:

	def __init__(self, serialPort, serialSpeed, debug = False):

		self.debug = debug
		self.serialPort = serialPort
		self.serialSpeed = serialSpeed

		if self.debug:
			print "[DEBUG] [ARDUINO] Server has been instantiated."
			print "[DEBUG] [ARDUINO] Connecting to Arduino..."

		#self.serialCom = serial.Serial(serialPort, serialSpeed)

		if self.debug:
			print "[DEBUG] [ARDUINO] Established connection."

	def write(self, message):
		#self.serialCom.write(message)

		if self.debug:
			print "[DEBUG] [ARDUINO] Written: " + message + '.'

	def read(self):
		#message = self.serialCom.readline().rstrip()
		message = 'Response'

		if self.debug:
			print "[DEBUG] [ARDUINO] Read: " + message + '.'

		return message