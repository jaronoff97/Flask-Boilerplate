import requests

sample_user = {"latitude" : 42.2561110, "longitude" : -71.0741010, "uid" : "0" , "first_name" : "alex", "last_name" : "iansiti"}
send_url = "http://flask-macoder.rhcloud.com/near"

r = requests.post(send_url, sample_user)
print(r.json())