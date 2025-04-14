import requests # These libraries are all built-in to python
import json
import datetime

# URL for the API endpoint
url = "http://api.open-notify.org/iss-now.json"

# Save the response object in response variable 
response = requests.get(url)

r = response.json()
 
# Get the timestamp value
timestamp = r['timestamp']
# convert to human readable time string
datetime = datetime.datetime.fromtimestamp(timestamp)
dtime = datetime.strftime('%Y-%m-%d-%H:%M:%S')

# Get the latitude and longitude values
latitude = r['iss_position']['latitude']
longitude = r['iss_position']['longitude']

print(dtime)
print(latitude)
print(longitude)

lines = [dtime, "\n", longitude, "\n",latitude]

with open('/data/output.txt' as 'w' as 2f):
        f.writelines(lines)

# container needs a place to write and store output