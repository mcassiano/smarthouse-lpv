import serial
from time import sleep

class ArduinoConnection:

	def __init__(self, serialPort, serialSpeed, debug = False):

		self.debug = debug
		self.serialPort = serialPort
		self.serialSpeed = serialSpeed

		try:
			if self.debug:
				print "[DEBUG] [ARDUINO] Server has been instantiated."
				print "[DEBUG] [ARDUINO] Connecting to Arduino..."

			self.serialCom = serial.Serial(serialPort, serialSpeed, timeout = 3)

			if self.debug:
				print "[DEBUG] [ARDUINO] Established connection."

		except:
			if self.debug:
				print "[DEBUG] [ARDUINO] Port already open!"

			self.serialCom = serial.serial_for_url(serialPort, serialSpeed, timeout = 3)
			
			if self.debug:
				print "[DEBUG] [ARDUINO] Established connection."


	def write_and_get_response(self, message):
		self.serialCom.write(message)

		if self.debug:
			print "[DEBUG] [ARDUINO] Written: " + message + '.'
			print "[DEBUG] [ARDUINO] Read: " + res + '.'


	def read(self):
		return self.serialCom.readline().rstrip()

	def close(self):
		self.serialCom.close()