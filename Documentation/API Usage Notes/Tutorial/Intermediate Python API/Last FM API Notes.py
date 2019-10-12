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

# Let's look at the @attr (attributes) key by itself:

# There are almost three million total artists in the results of this API 
# endpoint, and we’re being showing the first 50 artists in a single ‘page’. 
# This technique of spreading the results over multiple pages is called 
# pagination. 

######################

# Working with Paginated Data

# In order to build a dataset with many artists, we need to make an API request
# for each page and then put them together. We can control the pagination of
# our results using two optional parameters specified in the documentation:

    # limit: The number of results to fetch per page (defaults to 50)
    # page: Which page of the results we want to fetch

# Becauser the '@attrs' key gives us the total number of pages, we can use a 
# a 'while' loop and iterate over pages until the page number is equal to the
# last page number

# We can also use the 'limit' parameter to fetch more results in each page -
# we'll fetch 500 results per page so we only need to make ~6,000 calls
# instead of ~60,000

# Let's look at an example of how we would structure that code:

    #   initialize list for results
    #   results = []
    #   set initial page and a high total number
    #   page = 1
    #   total_pages = 99999

    #   while page > total_pages:
    #   simplified request code for this example
    #   r = request.get("endpoint_url", params={"page": page})

    #   append results to list
    #   results.append(r.json())
    
    #   increment the page
    #   page += 1

# As we mentioned a moment ago we need to make almost 6,000 calls to this end 
# point, which means we need to think about rate limiting to comply with the
# comply with the Last.fm API's terms of service. Let's look at a few
# approaches.

######################

# Rate Limiting

# Rate limiting is using code to limit the number of times per second that we
# hit a particular API. Rate limiting will make your code slower, but it's 
# better than getting banned from using the API altogether.

# The easiest way to perform rate limiting is to use Python time.sleep() 
# function.  This function accepts a float specifying a number of seconds to
# wait before proceeding.  For instance, the following code will wait one
# quarter of a second between two print statements:

    #   import time
    
    #   print("one")
    #   time.sleep(0.25)
    #   print("two")

# Because making the API call itself takes some time, we're likely to be
# making two or three calls per second, not the four calls per second that
# sleeping for 0.25s might suggest.  This should be enough to keep us under
# Last.fm's threshold (if we were going to be hitting their API for a number
# of hours, we might choose an even slower rate)

#  Another technique that's useful for rate limiting is using a local database
# to cache the results of any API call, so that if we make the same call
# twice, the second time it reads it from the local cache.  Imagine that
# as you are writing your code, you discover syntax errors and your
# loops fails, and you have to start again.  By using a local cache, you have
# two benefits:

    # You don't make extra API calls that you don't need to.
    # You don't need to wait the extra time to rate limit when reading the
    # repeated calls from the cache.

    # The logic that we could use to combine waiting with a cache looks like
    # the below table:

    #     ||
    #     \/
    #  _____________________
    # |Check whether request|                              _____________
    # |has been previously  | ==========================> |Return cached|
    # |cached.              |                             |   Response  |
    # -----------------------                              -------------
    #     ||
    #     \/
    #  ____________       _________       ______       __________
    # |Request From| ==> |Cache    | ==> | Wait | ==> |Return the|
    # |API         |     |Response |     |      |     | Response |
    # --------------      ---------       ------       ----------

# Creating logic for a local cache is a reasonably complex task, but there's a
# great library called 'requests-cache' which will do all of the work for you
# with only a couple lines of code.

    #  You can install requests-cache using pip:

    #    python -m pip install requests-cache

# Then all we need to do is import the library and invoke the
# 'requests_cache.install_cache()' function, and the library will transparently
# cache new API requests, and use the cache whenever we make a repeated call.

# The last thing we should consider is that our 6,000 requests will likely 
# take about 30 minutes to make, and so we'll print some output in each loop
# so we can see where everything is at.  We'll use an IPython display trick
# to clear the output after each run so things look neater in our 
# notebook.


