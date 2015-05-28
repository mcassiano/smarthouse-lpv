#!/usr/bin/env python

import sys, time
from daemon import Daemon
from ArduinoConnection import ArduinoConnection

class SmartHouseDaemon(Daemon):

	def run(self):

		if super(SmartHouseDaemon, self).is_running():
			self.connection = super(SmartHouseDaemon, self).get_connection()
		else:
			connection = ArduinoConnection('/dev/cu.HC-06-DevB', 9600, True)
			super(SmartHouseDaemon, self).set_connection(connection)

		while True:
			time.sleep(1)

	def read_from_arduino(self):
		connection = super(SmartHouseDaemon, self).get_connection()
		return connection.read()

	def write_to_arduino(self, message):
		connection = super(SmartHouseDaemon, self).get_connection()
		connection.write(message)

if __name__ == "__main__":

	daemon = SmartHouseDaemon('/tmp/smarthouse-test.pid')

	if len(sys.argv) >= 2:
		if 'start' == sys.argv[1]:
			print 'Starting daemon...'
			daemon.start()
		elif 'stop' == sys.argv[1]:
			print 'Stopping daemon...'
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		elif 'arduino' == sys.argv[1]:
			if 'send' == sys.argv[2]:
				message = sys.argv[3]
				daemon.write_to_arduino(message)

			if 'read' == sys.argv[2]:
				print daemon.read_from_arduino()

		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)

	else:
		print "usage: %s start|stop|restart|arduino" % sys.argv[0]
		sys.exit(2)