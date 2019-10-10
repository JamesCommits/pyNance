# This guide we follow can be found at: dataquest.io/blog/last-fm-api-python/

# We'll learn:
# How to authenticate yourself with an API key
# How to use rate limiting and other techniques to work within the guidelines
#   of an API
# How to use pagination to work with large requests.

# We'll be working with the Last.fm API here. We'll be building a dataset
# of popular artists using their API

# Be sure to read the documentation of the API.  Last.fm doesn't want us
# making thousands of requests per day.  We'll learn a few rate limiting
# strategies to make sure we don't hit their API too much.

######################

# Authenticating with API Keys

# First we'll have to request access to the API to make calls.
# You'll receive an API key which is usually a long string like so:
# 240928348f0234fc092348023942
# Everytime we make a request, we'll use our API key to authenticate ourselves.

######################

# Making our First API Request

# In order to create a dataset of popular artists, we'll be working with
# the chart.getTopArtists endpoint 
# Reference: http://last.fm/api/show/chart.getTopArtists

# Looking at the Last.fm API documentation, we can observe a few things:
    # It looks like there is only one real endpoint, and each "endpoint" is
    # actually specified by using the method parameter.

    # The API can return results in multiple formats - we'll specify JSON so
    # we can leverage what we already know about working with APIs in Python

# Before we start, remember that we need to provide a user-agent header to
# identify ourselves when we make a request.  With the Python requests libary
# we specify headers using the headers parameter with a dictionary of 
# headers like so:

# import requests

# headers = {
#     'user-agent': 'JamesCommits'
# }

# payload = {
#     'api_key': API_KEY,
#     'method': 'chart.gettopartists',
#     'format': 'json'
# }

# r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
# print(r.status_code)

# We should see a status code of '200' for a successful request.

# Before we look at the data returned by our request, let's think about the
# fact that we're going to make many requests during this tutorial.  In those
# requests, a lot of the functionality is going to be the same:

    # We'll use the same URL
    # We'll use the same API key
    # We'll specify JSON as our format
    # We'll use the same headers

# To save ourselves time, we're going to create a function that does alot
# of this work for us. We'll provide the function with a payload
# dictionary, and then we'll add extra keys to that dictionary and pass it with
# our other options to make the request.

# Lets look at what the function looks like.

# def lastfm_get(payload):
#     # define headers and URL
#     headers = {'user-agent': 'USER_AGENT'}
#     url = 'http://ws.audioscrobbler.com/2.0/'

#     # Add API key and format to the payload
#     payload['api_key'] = 'API_KEY'
#     payload['format'] = 'json'

#     response = requests.get(url, headers=headers, params=payload)
#     return response

# Let's see how this simplifies making our earlier request.

# We'll use the json module to print the JSON data in an easier to read
# format. Let's re-use the jprint() function we created in that tutorial
# and print our response from the API.

# The structure of the JSON response is:
    # A dictionary with a single artists key, containing:
        # an @attr key containing a number of attributes about the response
        # an artist key containing a list of artist objects
        