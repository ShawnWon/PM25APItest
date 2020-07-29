import requests #MakingHTTP requests
from datetime import date #Get today's date

URL = "https://api.data.gov.sg/v1/environment/pm25"

today = str(date.today())
response = requests.get(url=URL+"?date="+today)
data = response.json()

for record in data["items"]:
    print("event_time:"+record["update_timestamp"])
    print("timestamp:"+record["timestamp"])
    rec = record["readings"]["pm25_one_hourly"]
    for key in rec:
        print(key+":"+str(rec[key]))
    print()
