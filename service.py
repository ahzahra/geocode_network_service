import urllib
import urllib2
import json
import sys
from collections import OrderedDict
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse

SERVER_NAME = ''
SERVER_PORT = 8000
ADDRESS = "4030 Baring Street Philadelphia"

# Google maps service request URL and KEY
GOOGLE_API_KEY = "AIzaSyBz9aRVpgQKN9AdgrvPBINK5FQ_rwgbhpA"
GOOGLE_URL = "https://maps.googleapis.com/maps/api/geocode/json" 

# HERE location service request URL and KEYS
APP_ID = "oTT08n7QAeiHNE2DAX1x"
APP_CODE = "Uweq5cyflvvyq5aYLyYc0g"
HERE_URL = "https://geocoder.cit.api.here.com/6.2/geocode.json"

class Geocode_Server(BaseHTTPRequestHandler):

	def do_GET(self):
		parsed_path = urlparse.urlparse(self.path)
		arg = parsed_path.query.split('=')[1]

		# Try a Google Maps service request test
		url = GOOGLE_URL + '?' + urllib.urlencode(OrderedDict([
			('address', arg),
	        ('key', GOOGLE_API_KEY)
			]))
		response = str(urllib2.urlopen(url).read())
		result = json.loads(response.replace('\\n', ''))
		if result['status'] == 'OK':
			lat = result['results'][0]['geometry']['location']['lat']
			lng = result['results'][0]['geometry']['location']['lng']
			print lat, lng

		else:
			try:
				# HERE service request test
				url = HERE_URL + '?' + urllib.urlencode(OrderedDict([
					('app_id',APP_ID),
			        ('app_code', APP_CODE),
			        ('searchtext', arg)
					]))
				response = str(urllib2.urlopen(url).read())
				result = json.loads(response.replace('\\n', ''))
				lat = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
				lng = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']
				print "Hi"
			except IndexError:
				print "Error"

		
		self.send_response(200)
		self.end_headers()


	def do_POST(self):
		self.send_response(200)
		self.end_headers()


if __name__ == '__main__':
	# Launch Server
	server = HTTPServer((SERVER_NAME,SERVER_PORT), Geocode_Server)

	print "Launching Server....."
	server.serve_forever()

	# Google service request test
	# url = GOOGLE_URL + '?' + urllib.urlencode(OrderedDict([
	# 	('address', ADDRESS),
 #        ('key', GOOGLE_API_KEY)
	# 	]))
	# response = str(urllib2.urlopen(url).read())
	# result = json.loads(response.replace('\\n', ''))
	# if result['status'] == 'OK':
	# 	lat = result['results'][0]['geometry']['location']['lat']
	# 	lng = result['results'][0]['geometry']['location']['lng']
	# 	print lat, lng

	# HERE service request test
	# url = HERE_URL + '?' + urllib.urlencode(OrderedDict([
	# 	('app_id',APP_ID),
 #        ('app_code', APP_CODE),
 #        ('searchtext', ADDRESS)
	# 	]))
	# response = str(urllib2.urlopen(url).read())
	# result = json.loads(response.replace('\\n', ''))
	# lat = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
	# lng = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']
	# print lat, lng

