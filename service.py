import urllib
import urllib2
import json
from collections import OrderedDict
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse

# Define the Local host server name and port values
SERVER_NAME = 'localhost'
SERVER_PORT = 8000

# Google maps service request URL and KEY
GOOGLE_API_KEY = "AIzaSyBz9aRVpgQKN9AdgrvPBINK5FQ_rwgbhpA"
GOOGLE_URL = "https://maps.googleapis.com/maps/api/geocode/json" 

# HERE location service request URL and KEYS
APP_ID = "oTT08n7QAeiHNE2DAX1x"
APP_CODE = "Uweq5cyflvvyq5aYLyYc0g"
HERE_URL = "https://geocoder.cit.api.here.com/6.2/geocode.json"

# Override the BaseHTTPRquestHandler class to implement the RESTful API protocols
class Geocode_Server(BaseHTTPRequestHandler):

	# GET Porotocol implementation
	def do_GET(self):
		# Parse the input url
		parsed_path = urlparse.urlparse(self.path)
		try:
			arg = parsed_path.query.split('=')

			# If an invalid argument name is passed, return an Error 404
			if arg[0] != 'location':
				self.send_error(404)
				return
			else:
				arg = arg[1]
				# Try a Google Maps service request 
				url = GOOGLE_URL + '?' + urllib.urlencode(OrderedDict([
					('address', arg),
			        ('key', GOOGLE_API_KEY)
					]))
				response = str(urllib2.urlopen(url).read())
				result = json.loads(response.replace('\\n', ''))
				if result['status'] == 'OK':
					lat = result['results'][0]['geometry']['location']['lat']
					lng = result['results'][0]['geometry']['location']['lng']
					message = self.get_message(arg, lat, lng)

				else:
					try:
						# HERE service request 
						url = HERE_URL + '?' + urllib.urlencode(OrderedDict([
							('app_id',APP_ID),
					        ('app_code', APP_CODE),
					        ('searchtext', arg)
							]))
						response = str(urllib2.urlopen(url).read())
						result = json.loads(response.replace('\\n', ''))
						lat = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
						lng = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']
						message = self.get_message(arg, lat, lng)
					except IndexError:
						print "Error, Address not found"

		except IndexError:
			pass

		
		self.set_headers()

		try:
			# Send the message if it exists
			self.wfile.write(message)
		except ValueError:
			pass

	# Implementation of POST protocol
	def do_POST(self):
		self.set_headers()

	# Implementation of HEAD protocol
	def do_HEAD(self):
		self.set_headers()

	def set_headers(self):
		self.send_response(200)
		self.end_headers()		

	# Encodes the latitude and longitude into a JSON message
	def get_message(self, query, lat, lng):
		arg = query.split('+')
		address = ''
		for s in arg:
			address = address + s + ' '
		message = OrderedDict([
			('Address',address),
			('Latitude',str(lat)),
			('Longitude',str(lng))
		])
		return json.dumps(message)

if __name__ == '__main__':
	# Launch Server
	server = HTTPServer((SERVER_NAME,SERVER_PORT), Geocode_Server)

	print "Launching Server....."
	server.serve_forever()



