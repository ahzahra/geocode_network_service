import urllib
import urllib2
import json
import sys

# Google maps service request URL and KEY
API_KEY = "AIzaSyBz9aRVpgQKN9AdgrvPBINK5FQ_rwgbhpA"
URL = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=" + API_KEY


if __name__ == '__main__':
	response = str(urllib2.urlopen(URL).read())
	result = json.loads(response.replace('\\n', ''))
	if result['status'] == 'OK':
		lat = result['results'][0]['geometry']['location']['lat']
		lng = result['results'][0]['geometry']['location']['lng']
		print lat, lng

