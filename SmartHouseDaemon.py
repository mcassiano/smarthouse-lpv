#!/usr/bin/env python

import sys, time
from daemon import Daemon
from ArduinoConnection import ArduinoConnection

class SmartHouseDaemon(Daemon):

	def run(self):

		while True:
			time.sleep(1)

if __name__ == "__main__":

	daemon = SmartHouseDaemon('/tmp/smarthouse-test.pid')

	if len(sys.argv) >= 2:
		if 'start' == sys.argv[1]:
			connection = ArduinoConnection('/dev/cu.HC-06-DevB', 9600)
			print 'Starting daemon...'
			daemon.start()

		elif 'stop' == sys.argv[1]:
			print 'Stopping daemon...'
			daemon.stop()

		elif 'restart' == sys.argv[1]:
			daemon.restart()

		elif 'arduino' == sys.argv[1]:
			connection = ArduinoConnection('/dev/cu.HC-06-DevB', 9600)

			if 'send' == sys.argv[2]:
				message = sys.argv[3]
				print connection.write_and_get_response(message)

		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)

	else:
		print "usage: %s start|stop|restart|arduino" % sys.argv[0]
		sys.exit(2)