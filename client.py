import urllib
import urllib2
import sys
from collections import OrderedDict
from service import SERVER_PORT, SERVER_NAME
import httplib

LOCAL_URL = "%s:%s" % (SERVER_NAME, str(SERVER_PORT))

if __name__ == '__main__':
	if len(sys.argv) == 1:
		raise ValueError('Not enough input arguments, use -h as an argument to see a list of arguments that can be used')
	if sys.argv[1] == '-h':
		print "Run the program from the command line as follows: python client.py COMMAND ADDRESS"
		print "Here's a list of possible COMMANDs: GET HEAD POST"
		print "The Address can be something as the following: 4030 Baring Street"
	elif not sys.argv[1] == "GET" and not sys.argv[1] == "POST" and not sys.argv[1] == "HEAD":
		raise ValueError(sys.argv[1] + ' is an invalid command')
	else:
		if len(sys.argv) == 2:
			raise ValueError('Not enough input arguments')
		COMMAND = sys.argv[1]
		ADDRESS = ''
		# Concatenate string arguments to create a single string containing the Address
		for i in range(2,len(sys.argv)):
			if(i == 2):
				ADDRESS = sys.argv[i]
			else:
				ADDRESS = ADDRESS + ' ' + sys.argv[i]

		# Generate the service request url 
		path = '/' + '?' + urllib.urlencode(OrderedDict([
			('location',ADDRESS),
			]))

		# print path
		# Send the service request to server and read the response
		conn = httplib.HTTPConnection(LOCAL_URL, timeout=10)
		conn.request(COMMAND, path)
		r1 = conn.getresponse()
		print r1.read()




