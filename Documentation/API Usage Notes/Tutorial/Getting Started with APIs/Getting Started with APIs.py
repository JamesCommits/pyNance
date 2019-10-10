import requests

# 43 in Notes
response1 = requests.get("http://api.open-notify.org/this-api-doesnt-exist")

# 49 in Notes
print(response1.status_code)

# 92 in Notes
response2 = requests.get("http://api.open-notify.org/astros.json")


print(response2.status_code)
import json

# 98 in Notes
print(response2.json())



# 146 in Notes
def jprint(obj):
    # Create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# 150 in Notes
jprint(response2.json())

# 170 in Notes
parameters = {
    "lat": 48.4684781,
    "lon": -123.4153758
}

response3 = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

jprint(response3.json())

# 192 in Notes
pass_times = response3.json()['response']

jprint(pass_times)

# 195 in Notes
risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes)


# 200 in Notes

from datetime import datetime

times = []
for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)

