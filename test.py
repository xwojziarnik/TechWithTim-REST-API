import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/1", {"likes": 10, "name": "Titanic", "views": 1000000})
print(response.json())

input()

response = requests.put(BASE + "video/1")
print(response.json())
