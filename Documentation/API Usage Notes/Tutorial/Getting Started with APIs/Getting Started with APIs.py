import requests

# 41 in Notes
response1 = requests.get("http://api.open-notify.org/this-api-doesnt-exist")

# 47 in Notes
print(response1.status_code)

# 90 in Notes
response2 = requests.get("http://api.open-notify.org/astros.json")


print(response2.status_code)

# 96 in Notes
print(response2.json())

import json

# 144 in Notes
def jprint(obj):
    # Create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# 148 in Notes
jprint(response2.json())

# 168 in Notes
parameters = {
    "lat": 40.0168708,
    "lon": -83.0904697
}

response3 = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

jprint(response3.json())

# 190 in Notes
pass_times = response3.json()['response']

jprint(pass_times)

# 193 in Notes
risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes)


# 198 in Notes

from datetime import datetime

times = []
for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)

