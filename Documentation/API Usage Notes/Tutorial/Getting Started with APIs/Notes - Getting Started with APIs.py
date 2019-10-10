# To use an API, you make a request to a remote web server, and retrieve the
# data you need.  

#############

# What is an API?

# An API, or Application Programming Interface, is a server that you can use
# to retrieve and send data to using code.  

# When we want to receive data from an API, we need to make a REQUEST.  
# API requests work in the same way as the rest of the data on the web.
# You make a request to an API server for data, and it responds to your request.

#############

# Making API Requests in Python

# In Python, the most common library for making requests and working with APIs
# is the requests library.  This isn't part of the standard library so we'll
# need to install it to get started.

# We'll install requests using pip:

# python -m pip install requests

#############

# There are many different types of requests.  The most common request being
# a GET request, is used for retrieving data.  

# Because we're just trying to retrieving data our focus will be on making
# GET requests.

# When we make a GET request, the response from the API comes with a response 
# code which tells us whether our request was successful.  This is important
# because they'll tell us if something went wrong or not.

#############

# To make a GET request, we'll use the request.get() function, which requires
# one argument - the URL we want to make the request to.

# We'll start with a non-existing API, so we can see what response codes look
# like.

# The .get() function returns a response object. We can use .status_code on the
# end of our newly created variable to receive the status code for our request.

# We get a '404' status code error here. It's the status code that a server
# returns if it can't find the file we requested.  In this case, we asked
# for 'this-api-doesnt-exist' which surprisingly does not exist!

#############

# API STATUS CODES

# '200' - Everything went okay, and the result has been returned (if any)
# '301' - The server is redirecting you to a different endpoint.  This
#         can happen when a company switches domain names, or an endpoint
#         name has changed.
# '400' - The server thinks you made a bad request. This can happen when you 
#         don't send along the right data, among other things.
# '401' - The server thinks you're not authenticated.  Many APIs require login
#         credentials, so this happens when you don't send the right 
#         credentials to access the API.
# '403' - The resource you're trying to access is forbidden: you don't have the
#         right permissions to see it.
# '404' - The resource you tried to access wasn't found on the server.
# '503' - The server is not ready to handle the request.

# You might notice that all of the status codes that begin with a '4' indicate
# some sort of error.  The first number of status codes indicate their
# category.  You know if your status code starts with a '2' it was successful,
# and if it starts with a '4' or '5' there was an error.

#############

# We'll be working with the Open Notify API - which gives access to data about
# the international space station.

    # This API is great for learning because it doesn't require Authentication

# There will often be multiple APIs available on a particular server.  Each
# of these APIs are commonly called 'endpoints'

    # The first API we'll use will be 'http://api.open-notify.org/astros.json'
    # This API returns data about astronauts currently in space.

# We'll start by making a GET request to the endpoint using the requests
# library.

# We can run the program to see our returned status code of '200' - which
# tells us it was a successful request.

# The documentation for the API tells us we'll get the response in a JSON
# format.  Let's use .json() to see the data we received back from the API

#############

# Working with JSON Data in Python

# JSON (JavaScript Object Notation) is the language of APIs.  JSON is a way
# to encode data structures that ensures they are easily readable by machines.
# JSON is the primary format in which data is passed back and forth to APIs, and
# most API servers will send their responses in JSON format.

# You might have noticed that the JSON output we received from the API looked
# like it contained Python dictionaries, lists, strings and integers.  You can
# think of JSON as being a combination of these objects represented as strings.

# Example JSON text below:

# [
#     {
#         "name": "Sabine",
#         "age": 36,
#         "favorite_foods": ["Pumpkin", "Oatmeal"]
#     },
#     {
#         "name": "Zoe",
#         "age": 40,
#         "favorite_foods": ["Chicken", "Pizza", "Chocolate"]
#     },
#     {
#         "name": "Heidi",
#         "age": 45,
#         "favorite_foods": ["Ceasar Salad"]
#     }
# ]

# We can see in the JSON above, we have a list containing seperate dictionaries
# These dictionaries can include further lists, like favorite foods.

# Python has JSON support with the json package.  It's apart of the standard
# library, so we won't have to install anything to use it.  We can both convert
# lists and dictionaries to JSON, and convert strings to lists in dictionaries.

# In the case of our ISS Pass data, it is a dictionary encoded to a string in
# JSON format.

# The JSON library has two main functions:

# json.dumps() - Takes in a Python object, and converts (dumps) it to a string.
# json.loads() - Takes a JSON string, and converts (loads) it to a Python object

# The .dumps() function is particularly useful as we can use it to print a
# formatted string which makes it easier to understand the JSON output.


#############

# Using an API with Query Parameters

# The API endpoint we used above does not take any parameters. We just send
# a GET request and the API sends back data about the number of people
# currently in space.

# It's very common, however, to have an API endpoint that requires us to 
# specify parameters.  
# An example endpoint for this: http://api.open.notify.org/iss-pass.json
# This endpoint tells us the next times that the ISS will pass over a 
# given location on earth.

# If we look at the documentation, it specifies required lat(latitude) and
# long(longitude)

# We can do this by adding an optional keyword argument, params, to our
# request.  
# We can make a dictionary with these parameters, and then pass them
# into the requests.get function. 

# It's almost always preferable to setup the parameters as a dictionary,
# because requests takes care of some things that come up, like properly
# formatting the query parameters.

# Lets make a request using our new parameters dictionary.  

#############

# Understanding the Pass Times

# The JSON response matches what the documentation specified:

    # A dictionary with three keys
    # The third key, response, contains a list of pass times.
    # Each pass time is a dictionary with risetime (the pass start time)
        # and duration keys.

# Lets extract the pass times from our JSON object. This prints out just the
# results section of the API response.

# Next, we'll use a loop to extract just the five risetime values. This loop
# will iterate through our 'pass_times' response to the API. For d in pass_times
# is referring to each dictionary in the list, and we make time = to the
# key 'risetimes' found in each d dictionary iteration.  

# These times may be difficult to understand - as they are in timestamp
# or epoch format.  The time is measured in the number of seconds since
# Jan 1, 1970.  We can use the Python datetime.fromtimestamp() method to
# convert these into easier to understand times.




