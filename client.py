import urllib
import urllib2
import json
import sys
from collections import OrderedDict
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse

SERVER_NAME = ''
SERVER_PORT = 8000
ADDRESS = "4030 Baring Street, Philadelphia"

# Google maps service request URL and KEY
GOOGLE_API_KEY = "AIzaSyBz9aRVpgQKN9AdgrvPBINK5FQ_rwgbhpA"
GOOGLE_URL = "https://maps.googleapis.com/maps/api/geocode/json" 

# HERE location service request URL and KEYS
APP_ID = "oTT08n7QAeiHNE2DAX1x"
APP_CODE = "Uweq5cyflvvyq5aYLyYc0g"
HERE_URL = "https://geocoder.cit.api.here.com/6.2/geocode.json"

if __name__ == '__main__':

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
	url = HERE_URL + '?' + urllib.urlencode(OrderedDict([
		('app_id',APP_ID),
        ('app_code', APP_CODE),
        ('searchtext', ADDRESS)
		]))
	response = str(urllib2.urlopen(url).read())
	result = json.loads(response.replace('\\n', ''))
	lat = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
	lng = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']
	print lat, lng

