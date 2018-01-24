# geocode_network_service
Network service that can resolve latittude and longitude coordinates for a given address using the Google Maps geocoding service. The service provides an appropriate restful API to allow requests.

Requirements: Python 2.7.x, Internet Connection

The network service can be launched by running the following command:
```
$ python service.py
```

In a seperate terminal window, the client to use the service can be used by running the following command:

```
$ python client.py COMMAND ADDRESS
```

where COMMAND is one of GET, HEAD, or POST (RESTful API), and the ADDRESS is the address of the location.

Example use:

```
$ python client.py GET 4030 Baring Street Philadelphia
```

The response to a successful GET request is returned in JSON format. 

# Running the service with your own client

The service responds to the following RESTful commands: GET, HEAD, and POST. To convert an address to its lat and lng values, the GET function should be called with the following url:

```
http://localhost:8000/?location=ADDRESS
```

where ADDRESS is the url encoded address.