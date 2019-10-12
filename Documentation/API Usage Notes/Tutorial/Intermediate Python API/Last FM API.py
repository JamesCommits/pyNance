import requests
import json

# headers = {
#     'user-agent': 'JamesCommits'
# }

# payload = {
#     'api_key': '32030bd7ae92bd6574669ca1d8857020',
#     'method': 'chart.gettopartists',
#     'format': 'json'
# }

# r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
# print(r.status_code)

# 71 in Notes
def lastfm_get(payload):
    # define headers and URL
    headers = {'user-agent': 'JamesCommits'}
    url = 'http://ws.audioscrobbler.com/2.0/'

    # Add API key and format to the payload
    payload['api_key'] = '32030bd7ae92bd6574669ca1d8857020'
    payload['format'] = 'json'

    response = requests.get(url, headers=headers, params=payload)
    return response

# 90 in Notes
r = lastfm_get({
    'method': 'chart.gettopartists'
})

print(r.status_code)
# 92 in Notes
def jprint(obj):
    # Create a formatted string of the Python JSON object.
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# 101-106 in Notes
jprint(r.json()['artists']['@attr'])

# 203-210 in Notes
import requests_cache

#211-213 in Notes
requests_cache.install_cache()

