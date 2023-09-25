import requests
from itertools import islice

response = requests.get("http://api.aladhan.com/v1/timingsByCity?city=Bellevue&country=United States&method=8")
timings = response.json()['data']['timings']
first7 = {s: timings[s] for s in list(timings)[:7]}
print(first7)
print('by the grace of ALLAH, we are in the month of ' + response.json()['data']['date']['hijri']['month']['en'])
