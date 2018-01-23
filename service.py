import urllib
import urllib2
import json
import sys

API_KEY = "AIzaSyBz9aRVpgQKN9AdgrvPBINK5FQ_rwgbhpA"
URL = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=" + API_KEY


if __name__ == '__main__':
	response = str(urllib2.urlopen(URL).read())

	print response
